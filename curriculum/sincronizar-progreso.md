# Sincronizar progreso (Google + Firebase)

El progreso del plan de estudios puede almacenarse en la nube: **inicie sesión una vez con Google** y, en visitas posteriores (teléfono o computadora), el avance se restaura automáticamente.

Sin configurar Firebase, la aplicación permanece en modo **solo local** (`localStorage`).

## Requisitos (una sola vez)

1. Proyecto en [Firebase Console](https://console.firebase.google.com/).
2. **Authentication → Sign-in method → Google** habilitado.
3. **Firestore Database** (modo producción) con las reglas de [`academia/firestore.rules`](../academia/firestore.rules).
4. En Authentication → Settings → **Authorized domains**: `adriantaf.github.io` (y `localhost` para desarrollo).
5. Project settings → Your apps → Web app → copie la configuración.

## Variables de entorno

Copie [`academia/.env.example`](../academia/.env.example) a `academia/.env` en el entorno local:

```bash
PUBLIC_FIREBASE_API_KEY=...
PUBLIC_FIREBASE_AUTH_DOMAIN=...
PUBLIC_FIREBASE_PROJECT_ID=...
PUBLIC_FIREBASE_STORAGE_BUCKET=...
PUBLIC_FIREBASE_MESSAGING_SENDER_ID=...
PUBLIC_FIREBASE_APP_ID=...
```

En GitHub → Settings → Secrets and variables → Actions, cree secrets con **los mismos nombres**. El flujo de trabajo de Pages los inyecta en el build.

## Uso

1. Abra el plan en el dispositivo móvil o en la laptop.
2. Seleccione **Entrar** (barra superior) o **Iniciar sesión con Google** (menú).
3. Marque lecciones con normalidad; cada guardado se envía a Firestore (con debounce).
4. En el otro dispositivo, con la misma cuenta, al abrir la aplicación se realiza descarga y fusión (pull + merge).

## Fusión

Si ambos dispositivos avanzaron sin conexión: se unen lecciones y prácticas completadas (OR lógico), se conserva el estado más avanzado y los registros semanales por fecha. No se elimina progreso marcado como hecho en un lado.

## Seguridad

- Las claves `PUBLIC_*` son de cliente (habitual en Firebase); la protección real son las **Firestore Rules** por `request.auth.uid`.
- No incluya `.env` en el repositorio.
- Un documento por usuario: `users/{uid}/data/progress`.

## iPhone / aplicación web progresiva (PWA)

En Safari o en la aplicación instalada se utiliza **redirección** de Google (el popup suele fallar). Tras autorizar, regresa al plan y la sesión queda persistida.
