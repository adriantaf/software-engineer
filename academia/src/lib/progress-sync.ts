import {
  GoogleAuthProvider,
  getRedirectResult,
  onAuthStateChanged,
  signInWithPopup,
  signInWithRedirect,
  signOut,
  type User,
} from 'firebase/auth';
import { doc, getDoc, setDoc } from 'firebase/firestore';
import { getFirebase, isFirebaseConfigured } from './firebase';
import {
  loadProgress,
  saveProgress,
  type MateriaProgress,
  type ProgressState,
  type WeeklyCheckIn,
} from './progress-client';

export type SyncStatus = 'disabled' | 'signed_out' | 'syncing' | 'synced' | 'error';

type SyncListener = (info: { status: SyncStatus; user: User | null; message?: string }) => void;

const STATUS_RANK: Record<MateriaProgress['status'], number> = {
  bloqueada: 0,
  disponible: 1,
  en_curso: 2,
  completada: 3,
};

let pushTimer: ReturnType<typeof setTimeout> | undefined;
let currentUser: User | null = null;
let lastStatus: SyncStatus = 'disabled';
let started = false;
const listeners = new Set<SyncListener>();

function emit(status: SyncStatus, message?: string) {
  lastStatus = status;
  for (const fn of listeners) fn({ status, user: currentUser, message });
  window.dispatchEvent(
    new CustomEvent('academia-sync', { detail: { status, user: currentUser, message } }),
  );
}

export function onSyncStatus(fn: SyncListener) {
  listeners.add(fn);
  fn({ status: lastStatus, user: currentUser });
  return () => listeners.delete(fn);
}

export function getSyncUser() {
  return currentUser;
}

function progressDoc(uid: string) {
  const fb = getFirebase();
  if (!fb) return null;
  return doc(fb.db, 'users', uid, 'data', 'progress');
}

function orBoolMap(a: Record<string, boolean> = {}, b: Record<string, boolean> = {}) {
  const out: Record<string, boolean> = { ...a };
  for (const [k, v] of Object.entries(b)) {
    if (v) out[k] = true;
    else if (out[k] === undefined) out[k] = false;
  }
  return out;
}

function mergeMateria(a: MateriaProgress, b: MateriaProgress): MateriaProgress {
  const status =
    STATUS_RANK[a.status] >= STATUS_RANK[b.status] ? a.status : b.status;
  const completadoEn =
    a.completadoEn && b.completadoEn
      ? a.completadoEn >= b.completadoEn
        ? a.completadoEn
        : b.completadoEn
      : a.completadoEn || b.completadoEn;
  return {
    status,
    practicas: orBoolMap(a.practicas, b.practicas),
    lecciones: orBoolMap(a.lecciones, b.lecciones),
    proyecto: !!(a.proyecto || b.proyecto),
    completadoEn: completadoEn ?? null,
  };
}

function mergeCheckIns(a: WeeklyCheckIn[] = [], b: WeeklyCheckIn[] = []): WeeklyCheckIn[] {
  const map = new Map<string, WeeklyCheckIn>();
  for (const c of [...b, ...a]) map.set(c.fecha, c);
  return [...map.values()].sort((x, y) => (x.fecha < y.fecha ? 1 : -1)).slice(0, 52);
}

/** Unión segura local ↔ remoto (un solo estudiante). */
export function mergeProgress(local: ProgressState, remote: ProgressState): ProgressState {
  const localTs = local.updatedAt ?? 0;
  const remoteTs = remote.updatedAt ?? 0;
  const newer = remoteTs > localTs ? remote : local;
  const older = newer === remote ? local : remote;

  const materiaIds = new Set([
    ...Object.keys(local.materias ?? {}),
    ...Object.keys(remote.materias ?? {}),
  ]);
  const materias: Record<string, MateriaProgress> = {};
  for (const id of materiaIds) {
    const a = local.materias[id];
    const b = remote.materias[id];
    if (a && b) materias[id] = mergeMateria(a, b);
    else materias[id] = a ?? b!;
  }

  return {
    ...older,
    ...newer,
    estudiante: newer.estudiante || older.estudiante,
    inicio: older.inicio || newer.inicio,
    horasSemanalesMeta: newer.horasSemanalesMeta || older.horasSemanalesMeta || 20,
    materiaActual: newer.materiaActual || older.materiaActual,
    lastMateriaId: newer.lastMateriaId || older.lastMateriaId,
    lastLeccionId: newer.lastLeccionId || older.lastLeccionId,
    materias,
    notas: newer.notas?.length ? newer.notas : older.notas,
    checkIns: mergeCheckIns(local.checkIns, remote.checkIns),
    updatedAt: Math.max(localTs, remoteTs, Date.now()),
  };
}

export async function pushProgress(state?: ProgressState | null) {
  const fb = getFirebase();
  if (!fb || !currentUser) return;
  const data = state ?? loadProgress();
  if (!data) return;
  const ref = progressDoc(currentUser.uid);
  if (!ref) return;
  const payload = { ...data, updatedAt: data.updatedAt ?? Date.now() };
  await setDoc(ref, { state: payload, updatedAt: payload.updatedAt }, { merge: true });
}

function schedulePush(state: ProgressState) {
  if (!currentUser || !getFirebase()) return;
  if (pushTimer) clearTimeout(pushTimer);
  pushTimer = setTimeout(() => {
    void pushProgress(state)
      .then(() => emit('synced'))
      .catch((e: unknown) => {
        console.warn('[progress-sync] push failed', e);
        emit('error', 'No se pudo subir el progreso');
      });
  }, 300);
}

export async function pullAndMerge() {
  const fb = getFirebase();
  if (!fb || !currentUser) return loadProgress();
  emit('syncing');
  const ref = progressDoc(currentUser.uid);
  if (!ref) return loadProgress();

  try {
    const snap = await getDoc(ref);
    const local = loadProgress();
    const remoteRaw = snap.exists() ? (snap.data()?.state as ProgressState | undefined) : undefined;

    if (!remoteRaw && local) {
      await pushProgress(local);
      emit('synced');
      return local;
    }
    if (remoteRaw && !local) {
      saveProgress({ ...remoteRaw, updatedAt: remoteRaw.updatedAt ?? Date.now() }, { emit: false });
      emit('synced');
      return loadProgress();
    }
    if (remoteRaw && local) {
      const merged = mergeProgress(local, remoteRaw);
      saveProgress(merged, { emit: false });
      await pushProgress(merged);
      emit('synced');
      return merged;
    }
    emit('synced');
    return null;
  } catch (e) {
    console.warn('[progress-sync] pull failed', e);
    emit('error', 'No se pudo sincronizar');
    return loadProgress();
  }
}

/**
 * signInWithRedirect guarda estado en storage del authDomain (p. ej. *.firebaseapp.com).
 * En GitHub Pages (github.io) ese origen es cross-site: Safari/Chrome iOS lo particionan
 * y al volver aparece "missing initial state". Solo es seguro si authDomain == hostname.
 */
function redirectStorageIsFirstParty(): boolean {
  const raw = (import.meta.env.PUBLIC_FIREBASE_AUTH_DOMAIN as string | undefined) || '';
  const authHost = raw.replace(/^https?:\/\//, '').split('/')[0]?.toLowerCase();
  if (!authHost) return false;
  const pageHost = window.location.hostname.toLowerCase();
  return pageHost === authHost || pageHost.endsWith(`.${authHost}`);
}

function preferRedirectSignIn() {
  // Cross-site authDomain (caso Pages + firebaseapp.com): NUNCA redirect.
  if (!redirectStorageIsFirstParty()) return false;

  const ua = navigator.userAgent;
  const standalone =
    window.matchMedia('(display-mode: standalone)').matches ||
    Boolean((navigator as Navigator & { standalone?: boolean }).standalone);
  const mobile = /Android|iPhone|iPad|iPod|Mobile/i.test(ua);
  return mobile || standalone || window.matchMedia('(max-width: 767px)').matches;
}

function isMissingInitialStateError(e: unknown): boolean {
  const code =
    e && typeof e === 'object' && 'code' in e ? String((e as { code: unknown }).code) : '';
  const message =
    e && typeof e === 'object' && 'message' in e ? String((e as { message: unknown }).message) : '';
  return (
    code === 'auth/missing-initial-state' ||
    /missing initial state/i.test(message) ||
    /browserStorage is inaccessible/i.test(message) ||
    /storage-partitioned/i.test(message)
  );
}

function authErrorMessage(e: unknown): string {
  const code =
    e && typeof e === 'object' && 'code' in e ? String((e as { code: unknown }).code) : '';
  if (isMissingInitialStateError(e)) {
    return 'El inicio de sesión por redirección falló en este iPhone (almacenamiento particionado). Reintenta: usamos ventana emergente de Google.';
  }
  if (
    code === 'auth/web-storage-unsupported' ||
    code === 'auth/operation-not-supported-in-this-environment'
  ) {
    return 'Este navegador bloquea el almacenamiento (localStorage/cookies). Sal del modo privado, permite datos del sitio e inténtalo otra vez.';
  }
  if (code === 'auth/popup-blocked') {
    return 'Safari/Chrome bloqueó la ventana de Google. Permite ventanas emergentes para este sitio e inténtalo de nuevo.';
  }
  if (code === 'auth/popup-closed-by-user') {
    return 'Cerraste la ventana de Google antes de terminar. Pulsa Entrar otra vez.';
  }
  if (code === 'auth/unauthorized-domain') {
    return 'Este dominio no está autorizado en Firebase Auth. Añádelo en Authentication → Settings.';
  }
  if (code === 'auth/network-request-failed') {
    return 'Sin conexión o red bloqueada. Revisa datos/Wi‑Fi e inténtalo de nuevo.';
  }
  return 'No se pudo iniciar sesión. Revisa la consola o reintenta.';
}

export async function signInWithGoogle() {
  const fb = getFirebase();
  if (!fb) {
    emit('disabled', 'Firebase no configurado');
    return;
  }
  const provider = new GoogleAuthProvider();
  provider.setCustomParameters({ prompt: 'select_account' });
  emit('syncing');

  const useRedirect = preferRedirectSignIn();

  try {
    if (useRedirect) {
      await signInWithRedirect(fb.auth, provider);
      return;
    }
    // Popup: mantiene el estado en el origen de la app (funciona en github.io + iOS).
    await signInWithPopup(fb.auth, provider);
  } catch (e) {
    console.warn('[progress-sync] sign-in failed', e);

    // Solo reintentar con redirect si el storage del authDomain es first-party.
    // En Pages/iOS el redirect provoca justo "missing initial state".
    if (!useRedirect && redirectStorageIsFirstParty()) {
      try {
        await signInWithRedirect(fb.auth, provider);
        return;
      } catch (e2) {
        console.warn('[progress-sync] redirect fallback failed', e2);
        emit('error', authErrorMessage(e2));
        return;
      }
    }

    emit('error', authErrorMessage(e));
  }
}

export async function signOutGoogle() {
  const fb = getFirebase();
  if (!fb) return;
  await signOut(fb.auth);
}

/** Arranca auth + sync. Idempotente. */
export function startProgressSync() {
  if (started) return;
  started = true;

  if (!isFirebaseConfigured()) {
    emit('disabled');
    return;
  }

  const fb = getFirebase();
  if (!fb) {
    emit('disabled');
    return;
  }

  window.addEventListener('academia-progress', ((e: CustomEvent<ProgressState>) => {
    if (!currentUser) return;
    schedulePush(e.detail);
  }) as EventListener);

  void getRedirectResult(fb.auth)
    .then((result) => {
      if (result?.user) {
        // El merge lo dispara onAuthStateChanged.
        emit('syncing');
      }
    })
    .catch((e) => {
      // Residuo típico tras un redirect fallido en iOS/Pages; no asustar en cada carga.
      if (isMissingInitialStateError(e)) {
        console.warn('[progress-sync] redirect state perdido (esperado en github.io/iOS); usar popup', e);
        return;
      }
      console.warn('[progress-sync] redirect result', e);
      emit('error', authErrorMessage(e));
    });

  onAuthStateChanged(fb.auth, (user) => {
    currentUser = user;
    if (!user) {
      emit('signed_out');
      return;
    }
    void pullAndMerge().then(() => {
      window.dispatchEvent(new CustomEvent('academia-progress'));
    });
  });
}
