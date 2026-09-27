# Sincronizar progreso (Google + Firebase)

El progreso de la academia puede vivir en la nube: **entras una vez con Google** y, en visitas siguientes (iPhone o laptop), se restaura solo.

Sin configurar Firebase, la app sigue en modo **solo local** (`localStorage`).

## Qué necesitas (una vez)

1. Proyecto en [Firebase Console](https://console.firebase.google.com/).
2. **Authentication → Sign-in method → Google** habilitado.
3. **Firestore Database** (modo producción) con las reglas de [`academia/firestore.rules`](../academia/firestore.rules).
4. En Authentication → Settings → **Authorized domains**: `adriantaf.github.io` (y `localhost` para desarrollo).
5. Project settings → Your apps → Web app → copia la config.

## Variables

Copia [`academia/.env.example`](../academia/.env.example) a `academia/.env` en local:

```bash
PUBLIC_FIREBASE_API_KEY=...
PUBLIC_FIREBASE_AUTH_DOMAIN=...
PUBLIC_FIREBASE_PROJECT_ID=...
PUBLIC_FIREBASE_STORAGE_BUCKET=...
PUBLIC_FIREBASE_MESSAGING_SENDER_ID=...
PUBLIC_FIREBASE_APP_ID=...
```

En GitHub → Settings → Secrets and variables → Actions, crea secrets con **los mismos nombres**. El workflow de Pages las inyecta en el build.

## Uso

1. Abre el plan en el móvil o la laptop.
2. Pulsa **Entrar** (header) o **Entrar con Google** (menú).
3. Marca lecciones con normalidad; cada guardado sube a Firestore (debounce).
4. En el otro dispositivo, con la misma cuenta, al abrir la app se hace pull + merge.

## Merge

Si ambos dispositivos avanzaron offline: se unen lecciones/prácticas hechas (OR), estados al más avanzado, check-ins por fecha. No borra progreso “hecho” en un lado.

## Seguridad

- Las keys `PUBLIC_*` son de cliente (normal en Firebase); la protección es **Firestore Rules** por `request.auth.uid`.
- No subas `.env` al repo.
- Un documento por usuario: `users/{uid}/data/progress`.

## iPhone / PWA

En Safari o app instalada se usa **redirect** de Google (el popup suele fallar). Tras autorizar vuelves al plan y la sesión queda guardada.
