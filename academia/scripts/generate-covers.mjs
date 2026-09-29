/**
 * Genera academia/public/covers/Mxx.svg (27 materias).
 * Ejecutar: node scripts/generate-covers.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(__dirname, '../public/covers');

const STAGE = {
  basica: ['#0f766e', '#134e4a'],
  disciplinaria: ['#0369a1', '#0c4a6e'],
  terminal: ['#7c3aed', '#4c1d95'],
};

/** id → etapa + icono SVG (coords 640×360, icono ~200×200 centrado en 320,180) */
const COVERS = {
  M01: {
    etapa: 'basica',
    icon: `<rect x="220" y="95" width="200" height="130" rx="10" fill="none" stroke="#fff" stroke-width="4" opacity="0.92"/>
      <circle cx="238" cy="115" r="5" fill="#fff" opacity="0.7"/><circle cx="256" cy="115" r="5" fill="#fff" opacity="0.7"/>
      <text x="320" y="175" text-anchor="middle" fill="#fff" font-family="ui-monospace,monospace" font-size="28" opacity="0.95">$ git</text>
      <path d="M240 200h160" stroke="#fff" stroke-width="3" opacity="0.5"/>`,
  },
  M02: {
    etapa: 'basica',
    icon: `<text x="320" y="200" text-anchor="middle" fill="#fff" font-family="ui-monospace,monospace" font-size="72" font-weight="700" opacity="0.9">&lt;/&gt;</text>
      <rect x="250" y="130" width="140" height="8" rx="4" fill="#fff" opacity="0.35"/>`,
  },
  M03: {
    etapa: 'basica',
    icon: `<circle cx="260" cy="150" r="22" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <circle cx="380" cy="150" r="22" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <circle cx="320" cy="220" r="22" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <path d="M278 158l32 54M362 158l-32 54M282 150h76" stroke="#fff" stroke-width="3" opacity="0.75"/>`,
  },
  M04: {
    etapa: 'basica',
    icon: `<rect x="240" y="200" width="28" height="60" rx="4" fill="#fff" opacity="0.85"/>
      <rect x="280" y="170" width="28" height="90" rx="4" fill="#fff" opacity="0.7"/>
      <rect x="320" y="140" width="28" height="120" rx="4" fill="#fff" opacity="0.55"/>
      <rect x="360" y="185" width="28" height="75" rx="4" fill="#fff" opacity="0.75"/>
      <path d="M230 260h180" stroke="#fff" stroke-width="3" opacity="0.4"/>`,
  },
  M05: {
    etapa: 'basica',
    icon: `<rect x="235" y="115" width="170" height="130" rx="12" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <rect x="255" y="135" width="130" height="90" rx="6" fill="#fff" opacity="0.15"/>
      <path d="M320 115v-25M280 90h80" stroke="#fff" stroke-width="3" opacity="0.6"/>
      <circle cx="270" cy="180" r="8" fill="#fff" opacity="0.8"/><circle cx="320" cy="180" r="8" fill="#fff" opacity="0.8"/><circle cx="370" cy="180" r="8" fill="#fff" opacity="0.8"/>`,
  },
  M06: {
    etapa: 'basica',
    icon: `<rect x="250" y="120" width="140" height="90" rx="8" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <path d="M250 145h140" stroke="#fff" stroke-width="2" opacity="0.5"/>
      <text x="320" y="175" text-anchor="middle" fill="#fff" font-family="system-ui,sans-serif" font-size="22" opacity="0.85">class</text>
      <rect x="270" y="230" width="100" height="50" rx="6" fill="#fff" opacity="0.25"/>`,
  },
  M07: {
    etapa: 'disciplinaria',
    icon: `<circle cx="240" cy="180" r="18" fill="#fff" opacity="0.9"/>
      <circle cx="320" cy="180" r="18" fill="#fff" opacity="0.75"/>
      <circle cx="400" cy="180" r="18" fill="#fff" opacity="0.6"/>
      <path d="M258 180h44M338 180h44" stroke="#fff" stroke-width="4" opacity="0.5"/>`,
  },
  M08: {
    etapa: 'disciplinaria',
    icon: `<circle cx="250" cy="200" r="14" fill="#fff" opacity="0.85"/>
      <circle cx="320" cy="150" r="14" fill="#fff" opacity="0.85"/>
      <circle cx="390" cy="200" r="14" fill="#fff" opacity="0.85"/>
      <circle cx="320" cy="230" r="14" fill="#fff" opacity="0.7"/>
      <path d="M262 192l50-35M330 157l52 35M330 223l52-28M262 208l50-22" stroke="#fff" stroke-width="3" opacity="0.65"/>`,
  },
  M09: {
    etapa: 'disciplinaria',
    icon: `<ellipse cx="320" cy="145" rx="70" ry="22" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <path d="M250 145v80c0 12 31 22 70 22s70-10 70-22v-80" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <ellipse cx="320" cy="185" rx="70" ry="22" fill="none" stroke="#fff" stroke-width="3" opacity="0.5"/>
      <ellipse cx="320" cy="225" rx="70" ry="22" fill="none" stroke="#fff" stroke-width="3" opacity="0.35"/>`,
  },
  M10: {
    etapa: 'disciplinaria',
    icon: `<circle cx="250" cy="180" r="24" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <circle cx="390" cy="180" r="24" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <circle cx="320" cy="120" r="20" fill="#fff" opacity="0.35"/>
      <path d="M268 172l40-40M352 132l32 40M352 188l32-8M268 188l40-8" stroke="#fff" stroke-width="3" opacity="0.7"/>`,
  },
  M11: {
    etapa: 'disciplinaria',
    icon: `<rect x="230" y="130" width="180" height="28" rx="6" fill="#fff" opacity="0.35"/>
      <rect x="230" y="168" width="180" height="28" rx="6" fill="#fff" opacity="0.5"/>
      <rect x="230" y="206" width="180" height="28" rx="6" fill="#fff" opacity="0.7"/>
      <rect x="230" y="244" width="180" height="28" rx="6" fill="#fff" opacity="0.9"/>`,
  },
  M27: {
    etapa: 'disciplinaria',
    icon: `<rect x="240" y="120" width="160" height="100" rx="8" fill="none" stroke="#fff" stroke-width="4" opacity="0.85"/>
      <text x="320" y="175" text-anchor="middle" fill="#fff" font-family="ui-monospace,monospace" font-size="26" opacity="0.9">0xFF</text>
      <path d="M260 240h120M280 240v40M360 240v40" stroke="#fff" stroke-width="3" opacity="0.6"/>`,
  },
  M12: {
    etapa: 'disciplinaria',
    icon: `<rect x="260" y="110" width="120" height="150" rx="8" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <path d="M285 145h70M285 175h70M285 205h45" stroke="#fff" stroke-width="3" opacity="0.65"/>
      <path d="M370 230l25 25-35 35-25-25z" fill="#fff" opacity="0.4" stroke="#fff" stroke-width="2"/>`,
  },
  M13: {
    etapa: 'disciplinaria',
    icon: `<rect x="240" y="130" width="80" height="55" rx="6" fill="none" stroke="#fff" stroke-width="3" opacity="0.9"/>
      <rect x="320" y="130" width="80" height="55" rx="6" fill="none" stroke="#fff" stroke-width="3" opacity="0.7"/>
      <rect x="280" y="210" width="80" height="55" rx="6" fill="none" stroke="#fff" stroke-width="3" opacity="0.85"/>
      <path d="M280 158h40M360 158h-40M320 185v25" stroke="#fff" stroke-width="2" opacity="0.5"/>`,
  },
  M14: {
    etapa: 'disciplinaria',
    icon: `<path d="M280 140l40 40-40 40-40-40z" fill="#fff" opacity="0.5" stroke="#fff" stroke-width="3"/>
      <path d="M360 140l40 40-40 40-40-40z" fill="#fff" opacity="0.35" stroke="#fff" stroke-width="3"/>
      <path d="M320 200l40 40-40 40-40-40z" fill="#fff" opacity="0.7" stroke="#fff" stroke-width="3"/>`,
  },
  M15: {
    etapa: 'disciplinaria',
    icon: `<path d="M320 110l55 28v42c0 38-55 68-55 68s-55-30-55-68v-42z" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <path d="M295 175l18 18 42-48" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity="0.95"/>`,
  },
  M16: {
    etapa: 'disciplinaria',
    icon: `<rect x="220" y="120" width="200" height="130" rx="10" fill="none" stroke="#fff" stroke-width="4" opacity="0.85"/>
      <rect x="240" y="145" width="160" height="80" rx="6" fill="#fff" opacity="0.12"/>
      <path d="M300 240l20 25 35-45" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="0.8"/>`,
  },
  M17: {
    etapa: 'disciplinaria',
    icon: `<rect x="210" y="105" width="220" height="150" rx="12" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <rect x="210" y="105" width="220" height="32" rx="12" fill="#fff" opacity="0.2"/>
      <circle cx="232" cy="121" r="5" fill="#fff" opacity="0.6"/>
      <rect x="250" y="155" width="70" height="80" rx="4" fill="#fff" opacity="0.25"/>
      <rect x="340" y="155" width="70" height="35" rx="4" fill="#fff" opacity="0.35"/>`,
  },
  M18: {
    etapa: 'disciplinaria',
    icon: `<path d="M320 105l60 30v45c0 42-60 75-60 75s-60-33-60-75v-45z" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <rect x="295" y="165" width="50" height="45" rx="8" fill="none" stroke="#fff" stroke-width="4" opacity="0.85"/>
      <circle cx="320" cy="185" r="6" fill="#fff" opacity="0.9"/>`,
  },
  M19: {
    etapa: 'disciplinaria',
    icon: `<path d="M320 95c-55 0-100 22-100 50 0 20 35 38 85 46v34l15-12 15 12v-34c50-8 85-26 85-46 0-28-45-50-100-50z" fill="none" stroke="#fff" stroke-width="4" opacity="0.85"/>
      <path d="M250 145h140M270 175h100" stroke="#fff" stroke-width="3" opacity="0.4"/>`,
  },
  M20: {
    etapa: 'disciplinaria',
    icon: `<rect x="270" y="105" width="100" height="170" rx="18" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <rect x="295" y="125" width="50" height="8" rx="4" fill="#fff" opacity="0.4"/>
      <circle cx="320" cy="255" r="12" fill="none" stroke="#fff" stroke-width="3" opacity="0.7"/>`,
  },
  M21: {
    etapa: 'terminal',
    icon: `<rect x="220" y="115" width="55" height="150" rx="8" fill="#fff" opacity="0.2" stroke="#fff" stroke-width="3"/>
      <rect x="292" y="115" width="55" height="150" rx="8" fill="#fff" opacity="0.28" stroke="#fff" stroke-width="3"/>
      <rect x="364" y="115" width="55" height="150" rx="8" fill="#fff" opacity="0.36" stroke="#fff" stroke-width="3"/>
      <rect x="228" y="130" width="40" height="28" rx="4" fill="#fff" opacity="0.55"/>
      <rect x="300" y="155" width="40" height="28" rx="4" fill="#fff" opacity="0.55"/>`,
  },
  M22: {
    etapa: 'terminal',
    icon: `<path d="M320 100l-8 45h-45l36 26-14 45 31-24 31 24-14-45 36-26h-45z" fill="#fff" opacity="0.35" stroke="#fff" stroke-width="2"/>
      <rect x="265" y="210" width="110" height="55" rx="8" fill="none" stroke="#fff" stroke-width="3" opacity="0.8"/>
      <path d="M285 235h70M285 252h45" stroke="#fff" stroke-width="2" opacity="0.5"/>`,
  },
  M23: {
    etapa: 'terminal',
    icon: `<circle cx="320" cy="165" r="55" fill="none" stroke="#fff" stroke-width="4" opacity="0.85"/>
      <path d="M280 200c15-35 65-35 80 0M300 150c10 25 30 25 40 0" fill="none" stroke="#fff" stroke-width="3" opacity="0.6"/>
      <circle cx="295" cy="155" r="6" fill="#fff" opacity="0.8"/><circle cx="345" cy="155" r="6" fill="#fff" opacity="0.8"/>`,
  },
  M24: {
    etapa: 'terminal',
    icon: `<path d="M320 100l25 50 55 8-40 38 10 55-50-28-50 28 10-55-40-38 55-8z" fill="#fff" opacity="0.45" stroke="#fff" stroke-width="2"/>
      <circle cx="250" cy="230" r="12" fill="#fff" opacity="0.35"/><circle cx="390" cy="220" r="8" fill="#fff" opacity="0.5"/>`,
  },
  M25: {
    etapa: 'terminal',
    icon: `<rect x="285" y="130" width="70" height="90" rx="10" fill="none" stroke="#fff" stroke-width="4" opacity="0.9"/>
      <path d="M305 130v-18a15 15 0 0115-15h30a15 15 0 0115 15v18" fill="none" stroke="#fff" stroke-width="4" opacity="0.85"/>
      <circle cx="320" cy="175" r="10" fill="#fff" opacity="0.9"/>
      <path d="M320 185v25" stroke="#fff" stroke-width="4" opacity="0.85"/>`,
  },
  M26: {
    etapa: 'terminal',
    icon: `<circle cx="320" cy="180" r="45" fill="none" stroke="#fff" stroke-width="4" opacity="0.85"/>
      <circle cx="250" cy="150" r="18" fill="#fff" opacity="0.4"/>
      <circle cx="390" cy="150" r="18" fill="#fff" opacity="0.4"/>
      <circle cx="320" cy="250" r="18" fill="#fff" opacity="0.4"/>
      <path d="M265 158l45 15M355 158l-45 15M320 225v15" stroke="#fff" stroke-width="3" opacity="0.65"/>`,
  },
};

function svgFor(id, { etapa, icon }) {
  const [from, to] = STAGE[etapa] ?? STAGE.basica;
  const gid = id.replace(/\W/g, '');
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-label="Portada ${id}">
  <defs>
    <linearGradient id="bg-${gid}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="${from}"/>
      <stop offset="100%" stop-color="${to}"/>
    </linearGradient>
    <pattern id="grid-${gid}" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.08"/>
    </pattern>
  </defs>
  <rect width="640" height="360" fill="url(#bg-${gid})"/>
  <rect width="640" height="360" fill="url(#grid-${gid})"/>
  <circle cx="520" cy="80" r="120" fill="#ffffff" opacity="0.06"/>
  <circle cx="100" cy="280" r="90" fill="#ffffff" opacity="0.05"/>
  ${icon}
</svg>
`;
}

fs.mkdirSync(outDir, { recursive: true });
for (const [id, spec] of Object.entries(COVERS)) {
  fs.writeFileSync(path.join(outDir, `${id}.svg`), svgFor(id, spec), 'utf8');
}
console.log(`Wrote ${Object.keys(COVERS).length} covers to ${outDir}`);
