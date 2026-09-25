# Instalar el plan en el iPhone (PWA)

Este plan es una **PWA**: se puede añadir a la pantalla de inicio y usar muchas fichas **sin red** (después de la primera carga).

No hace falta App Store ni Cordova. El progreso sigue en este teléfono (`localStorage`).

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

- La primera visita (o un pase por las fichas) **cachea** HTML/CSS/JS e iconos.
- Luego puedes estudiar sin Wi‑Fi/datos las páginas ya cacheadas.
- Si publicamos una versión nueva, al volver online el service worker actualiza solo.

## Limitaciones (iOS)

- No es una app de la App Store.
- Si iOS necesita espacio, a veces limpia sitios poco usados (reabre online una vez).
- El progreso **no se sincroniza** entre iPhone y laptop (aún). Exporta desde **Progreso** si cambias de dispositivo.

## Android (opcional)

En Chrome: menú → **Instalar aplicación** / **Añadir a la pantalla de inicio**.

## Si algo falla

1. Borra el icono viejo y vuelve a **Añadir a pantalla de inicio**.
2. Confirma que la URL es la de GitHub Pages (HTTPS).
3. Abre **Guías → Cómo estudiar** online una vez para refrescar caché.
