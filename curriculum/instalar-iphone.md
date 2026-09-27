# Instalar el plan en el iPhone (PWA)

Este plan es una **PWA**: se puede añadir a la pantalla de inicio y usar muchas fichas **sin red** (después de la primera carga).

No hace falta App Store ni Cordova. El progreso puede sincronizarse entre iPhone y laptop con **Google** (ver [Sincronizar progreso](sincronizar-progreso.md)). Sin login, queda solo en este teléfono (`localStorage`).

## Requisitos

- iPhone con **Safari** (no Chrome/Firefox como navegador principal para “Añadir a inicio”).
- Haber abierto al menos una vez el plan por HTTPS (GitHub Pages).

## Pasos (Safari)

1. Abre el plan en Safari.
2. Toca el botón **Compartir** (cuadrado con flecha hacia arriba).
3. Elige **Añadir a pantalla de inicio**.
4. Nombre sugerido: **Plan** → **Añadir**.
5. Abre el icono: debería verse a pantalla completa (sin barra de URL).

## Offline

- La primera visita cachea CSS/JS/iconos; las páginas se guardan al visitarlas (estrategia red primero).
- Sin red puedes reabrir fichas ya visitadas.
- Si hay versión nueva online, aparece el banner **Actualizar** (o el SW se refresca solo).

## Chrome / PWA se quedó en contenido viejo

Si Safari ya muestra el plan nuevo (p. ej. 27 materias) pero Chrome sigue en el viejo:

1. Toca el banner **Actualizar** si aparece abajo.
2. En Chrome: menú del sitio (candado / info) → **Borrar datos** / permisos del sitio `adriantaf.github.io`.
3. Si instalaste la PWA: desinstálala y vuelve a abrir la URL, o **Instalar** de nuevo.
4. Recarga; el home debe coincidir con Safari (materias y horas del plan).

## Limitaciones (iOS)

- No es una app de la App Store.
- Si iOS necesita espacio, a veces limpia sitios poco usados (reabre online una vez).
- El progreso **no se sincroniza** entre iPhone y laptop (aún). Exporta desde **Progreso** si cambias de dispositivo.

## Android (opcional)

En Chrome: menú → **Instalar aplicación** / **Añadir a la pantalla de inicio**.

## Si algo falla

1. Borra el icono viejo y vuelve a **Añadir a pantalla de inicio**.
2. Confirma que la URL es la de GitHub Pages (HTTPS).
3. Sigue la sección **Chrome / PWA se quedó en contenido viejo** si un navegador no refleja el deploy.
