// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import AstroPWA from '@vite-pwa/astro';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.dirname(fileURLToPath(import.meta.url));
const base = '/software-engineer/';

// https://astro.build/config
export default defineConfig({
  site: 'https://adriantaf.github.io',
  base,
  integrations: [
    AstroPWA({
      registerType: 'autoUpdate',
      injectRegister: 'auto',
      includeAssets: [
        'favicon.svg',
        'icons/icon-192.png',
        'icons/icon-512.png',
        'icons/apple-touch-icon.png',
      ],
      manifest: {
        name: 'Academia de Egreso Competente',
        short_name: 'Academia',
        description:
          'Plan personal de egreso en ingeniería de software, con fichas, glosario y progreso local.',
        lang: 'es',
        start_url: base,
        scope: base,
        display: 'standalone',
        orientation: 'portrait-primary',
        background_color: '#f3f4f6',
        theme_color: '#1d4ed8',
        icons: [
          {
            src: `${base}icons/icon-192.png`,
            sizes: '192x192',
            type: 'image/png',
            purpose: 'any',
          },
          {
            src: `${base}icons/icon-512.png`,
            sizes: '512x512',
            type: 'image/png',
            purpose: 'any',
          },
          {
            src: `${base}icons/icon-512.png`,
            sizes: '512x512',
            type: 'image/png',
            purpose: 'maskable',
          },
        ],
      },
      workbox: {
        // Precache del build estático (fichas, CSS, JS, iconos).
        globPatterns: ['**/*.{js,css,html,svg,png,ico,webp,woff2,webmanifest}'],
        navigateFallback: `${base}index.html`,
        navigateFallbackDenylist: [/^\/api/],
        cleanupOutdatedCaches: true,
      },
      experimental: {
        // Astro genera rutas con trailing slash + index.html.
        directoryAndTrailingSlashHandler: true,
      },
      devOptions: {
        enabled: false,
      },
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
    server: {
      fs: {
        allow: [root, path.resolve(root, '..')],
      },
    },
  },
});
