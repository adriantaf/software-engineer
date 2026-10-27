import { initializeApp, type FirebaseApp } from 'firebase/app';
import {
  browserLocalPersistence,
  browserPopupRedirectResolver,
  getAuth,
  indexedDBLocalPersistence,
  initializeAuth,
  type Auth,
} from 'firebase/auth';
import { getFirestore, type Firestore } from 'firebase/firestore';

export type FirebaseClients = {
  app: FirebaseApp;
  auth: Auth;
  db: Firestore;
};

function readConfig() {
  const apiKey = import.meta.env.PUBLIC_FIREBASE_API_KEY as string | undefined;
  const authDomain = import.meta.env.PUBLIC_FIREBASE_AUTH_DOMAIN as string | undefined;
  const projectId = import.meta.env.PUBLIC_FIREBASE_PROJECT_ID as string | undefined;
  const storageBucket = import.meta.env.PUBLIC_FIREBASE_STORAGE_BUCKET as string | undefined;
  const messagingSenderId = import.meta.env.PUBLIC_FIREBASE_MESSAGING_SENDER_ID as string | undefined;
  const appId = import.meta.env.PUBLIC_FIREBASE_APP_ID as string | undefined;

  if (!apiKey || !authDomain || !projectId || !appId) return null;

  return {
    apiKey,
    authDomain,
    projectId,
    storageBucket: storageBucket || undefined,
    messagingSenderId: messagingSenderId || undefined,
    appId,
  };
}

let clients: FirebaseClients | null | undefined;

function createAuth(app: FirebaseApp): Auth {
  try {
    return initializeAuth(app, {
      persistence: [indexedDBLocalPersistence, browserLocalPersistence],
      popupRedirectResolver: browserPopupRedirectResolver,
    });
  } catch {
    // Ya inicializado (HMR / segunda llamada).
    return getAuth(app);
  }
}

/** null si faltan env (modo solo-local). */
export function getFirebase(): FirebaseClients | null {
  if (clients !== undefined) return clients;
  const config = readConfig();
  if (!config || typeof window === 'undefined') {
    clients = null;
    return clients;
  }
  const app = initializeApp(config);
  clients = { app, auth: createAuth(app), db: getFirestore(app) };
  return clients;
}

export function isFirebaseConfigured(): boolean {
  return readConfig() !== null;
}
