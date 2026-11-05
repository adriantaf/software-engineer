#!/usr/bin/env node
/**
 * Migra lecciones legacy → formato: pasos (5–8 pasos tipados).
 * Conserva el body Markdown como lectura complementaria.
 *
 * Uso:
 *   node scripts/migrate-lessons-to-pasos.mjs           # todas excepto ya migradas
 *   node scripts/migrate-lessons-to-pasos.mjs M02 M03   # solo esas
 *   node scripts/migrate-lessons-to-pasos.mjs --dry-run
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import matter from 'gray-matter';
import { parseLeccionPasos } from '../src/lib/lesson-schema.ts';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '../..');
const etapasRoot = path.join(repoRoot, 'curriculum/etapas');

const args = process.argv.slice(2);
const dryRun = args.includes('--dry-run');
const filter = new Set(
  args.filter((a) => !a.startsWith('--')).map((a) => a.toUpperCase()),
);

function truncate(s, n) {
  const t = String(s || '').trim();
  if (t.length <= n) return t;
  return `${t.slice(0, n - 1).trim()}…`;
}

function stripMdNoise(s) {
  return String(s || '')
    .replace(/\r/g, '')
    .replace(/^#+\s+/gm, '')
    .trim();
}

/** Parse ## sections (and keep order). */
function parseSections(content) {
  const lines = content.replace(/\r/g, '').split('\n');
  const sections = {};
  let current = '_intro';
  const buf = [];
  const flush = () => {
    sections[current] = buf.join('\n').trim();
    buf.length = 0;
  };
  for (const line of lines) {
    const m = /^(#{2})\s+(.+?)\s*$/.exec(line);
    if (m) {
      flush();
      current = m[2].replace(/[*_`]/g, '').trim();
      continue;
    }
    buf.push(line);
  }
  flush();
  return sections;
}

function findSection(sections, ...names) {
  const keys = Object.keys(sections);
  for (const name of names) {
    const hit = keys.find((k) => k.toLowerCase() === name.toLowerCase());
    if (hit) return sections[hit];
    const soft = keys.find((k) => k.toLowerCase().startsWith(name.toLowerCase()));
    if (soft) return sections[soft];
  }
  return '';
}

function parseSubsteps(pasosBody) {
  if (!pasosBody) return [];
  const parts = pasosBody.split(/\n(?=###\s+)/);
  const out = [];
  for (const part of parts) {
    const m = /^###\s+(.+?)\s*\n([\s\S]*)$/.exec(part.trim());
    if (!m) continue;
    const title = m[1].replace(/\s*\([^)]*\)\s*$/, '').trim();
    const body = m[2].trim();
    const codes = [];
    const re = /```(\w+)?\n([\s\S]*?)```/g;
    let cm;
    while ((cm = re.exec(body))) {
      codes.push({ lang: (cm[1] || 'text').toLowerCase(), code: cm[2].trim() });
    }
    out.push({ title, body, codes });
  }
  return out;
}

function listItems(text) {
  return String(text || '')
    .split('\n')
    .map((l) => l.replace(/^\s*(?:[-*]|\d+\.)\s+/, '').trim())
    .filter((l) => l && !l.startsWith('|') && !l.startsWith('#'));
}

function firstBashCommand(text) {
  const fences = [...String(text).matchAll(/```(?:bash|sh|shell|zsh)?\n([\s\S]*?)```/gi)];
  for (const f of fences) {
    const lines = f[1]
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l && !l.startsWith('#') && !l.startsWith('//'));
    for (const line of lines) {
      // skip prompts / comments / assignments that aren't commands
      if (/^(cd|ls|mkdir|pwd|git|npm|npx|node|cat|echo|grep|find|chmod|touch|mv|cp|rm|pnpm|yarn|docker|curl|wget|python|pip|cargo|go|make|sudo)\b/.test(line)) {
        // take first simple command without heredocs
        if (line.includes('<<') || line.length > 120) continue;
        return line.replace(/^\s*\$\s*/, '');
      }
    }
  }
  return null;
}

function firstCodeFence(text, prefer = ['ts', 'typescript', 'js', 'javascript', 'tsx']) {
  const fences = [...String(text).matchAll(/```(\w+)?\n([\s\S]*?)```/g)];
  for (const lang of prefer) {
    const hit = fences.find((f) => (f[1] || '').toLowerCase() === lang);
    if (hit) return { lang: hit[1] || 'text', code: hit[2].trim() };
  }
  if (fences[0]) return { lang: fences[0][1] || 'text', code: fences[0][2].trim() };
  return null;
}

function slugId(i) {
  return `s${i}`;
}

function buildPasos(data, content) {
  const sections = parseSections(content);
  const objetivo = stripMdNoise(findSection(sections, 'Objetivo'));
  const intro = stripMdNoise(
    findSection(
      sections,
      'Por qué empieza así',
      'Por qué importa',
      'Idea clave',
      'Conceptos',
      'Contexto',
    ) || sections._intro || '',
  );
  // drop the H1/meta lines from intro
  const introClean = intro
    .split('\n')
    .filter((l) => !/^#\s/.test(l) && !/^\*\*~/.test(l) && !/^L\d{2}\s/.test(l))
    .join('\n')
    .trim();

  const pasosBody = findSection(sections, 'Pasos (hazlos en orden)', 'Pasos');
  const substeps = parseSubsteps(pasosBody);
  const hecho = findSection(sections, 'Hecho cuando');
  const errores = findSection(sections, 'Errores comunes');
  const errorItems = listItems(errores).slice(0, 4);
  const hechoItems = listItems(hecho).slice(0, 6);

  const pasos = [];
  let n = 1;

  const cuerpoIntro = [objetivo && `**Objetivo:** ${objetivo}`, introClean]
    .filter(Boolean)
    .join('\n\n');
  pasos.push({
    id: slugId(n++),
    tipo: 'explicacion',
    titulo: 'Qué vas a lograr',
    xp: 10,
    cuerpo:
      cuerpoIntro ||
      `En esta lección trabajas: **${data.titulo}**. Lee con atención y produce la evidencia indicada.`,
  });

  const code = firstCodeFence(pasosBody || content);
  if (code && code.code.length > 8) {
    pasos.push({
      id: slugId(n++),
      tipo: 'ejemplo',
      titulo: substeps[0] ? truncate(substeps[0].title, 70) : 'Ejemplo práctico',
      xp: 10,
      cuerpo: `\`\`\`${code.lang}\n${truncate(code.code, 1400)}\n\`\`\``,
      caption: 'Ejemplo migrado de la lección original — practícalo en tu entorno.',
    });
  } else if (substeps[0]) {
    pasos.push({
      id: slugId(n++),
      tipo: 'ejemplo',
      titulo: truncate(substeps[0].title, 70),
      xp: 10,
      cuerpo: truncate(stripMdNoise(substeps[0].body), 1200) || truncate(substeps[0].title, 200),
    });
  } else {
    pasos.push({
      id: slugId(n++),
      tipo: 'ejemplo',
      titulo: 'Cómo practicar',
      xp: 10,
      cuerpo:
        'Abre la lectura complementaria al final, sigue los pasos en orden y deja evidencia en `projects/`.',
    });
  }

  // Quiz: evidencia
  const evidencia = String(data.evidencia || '').trim();
  pasos.push({
    id: slugId(n++),
    tipo: 'quiz',
    titulo: 'Evidencia de la lección',
    xp: 15,
    variante: 'opcion_multiple',
    pregunta: `Para marcar "${data.titulo}" como hecha, ¿qué cuenta de verdad?`,
    opciones: [
      {
        id: 'a',
        texto: evidencia
          ? truncate(evidencia, 140)
          : 'Dejar evidencia concreta (archivo/commit/ejercicio) según el criterio de la lección',
      },
      { id: 'b', texto: 'Solo leer el título y pasar a la siguiente' },
      { id: 'c', texto: 'Marcar el checkbox sin producir nada' },
    ],
    respuesta: 'a',
    explicacionError:
      'Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en git, no existe.',
    explicacionOk: 'Correcto — evidencia primero.',
  });

  const bash = firstBashCommand(pasosBody || content);
  if (bash) {
    pasos.push({
      id: slugId(n++),
      tipo: 'terminal',
      titulo: 'Comando clave',
      xp: 15,
      enunciado: `Escribe este comando tal cual (es el de práctica de la lección):\n\n\`${bash}\``,
      comandoEsperado: [bash],
      pistas: ['Respeta el orden de los argumentos.', 'Sin prompt `$`.'],
      explicacionError: `Esperado: ${bash}`,
    });
  } else if (errorItems[0]) {
    pasos.push({
      id: slugId(n++),
      tipo: 'quiz',
      titulo: 'Error común',
      xp: 15,
      variante: 'verdadero_falso',
      pregunta: `¿Es buena práctica en esta lección? “${truncate(errorItems[0], 160)}"`,
      opciones: [
        { id: 't', texto: 'Verdadero' },
        { id: 'f', texto: 'Falso' },
      ],
      respuesta: 'f',
      explicacionError: 'Eso figura como error común: evítalo.',
      explicacionOk: 'Bien — ese es un anti-patrón de la lección.',
    });
  } else {
    pasos.push({
      id: slugId(n++),
      tipo: 'quiz',
      titulo: 'Método',
      xp: 15,
      variante: 'verdadero_falso',
      pregunta:
        'Debes producir algo verificable (código, nota, commit) además de leer, antes de dar la lección por hecha.',
      opciones: [
        { id: 't', texto: 'Verdadero' },
        { id: 'f', texto: 'Falso' },
      ],
      respuesta: 't',
      explicacionError: 'Verdadero: práctica deliberada + evidencia.',
      explicacionOk: 'Exacto.',
    });
  }

  // Concept quiz from objetivo / título
  const topic = truncate(String(data.titulo || 'el tema'), 80);
  pasos.push({
    id: slugId(n++),
    tipo: 'quiz',
    titulo: 'Foco de la lección',
    xp: 10,
    variante: 'opcion_multiple',
    pregunta: '¿Cuál describe mejor el foco de esta lección?',
    opciones: [
      {
        id: 'a',
        texto: truncate(objetivo || `Practicar: ${topic}`, 140),
      },
      { id: 'b', texto: 'Instalar herramientas al azar sin evidencia' },
      { id: 'c', texto: 'Saltar a otra materia sin terminar esta' },
    ],
    respuesta: 'a',
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.',
    explicacionOk: 'Correcto.',
  });

  // Extra explanation from second practical step if room
  if (substeps[1] && pasos.length < 7) {
    pasos.push({
      id: slugId(n++),
      tipo: 'explicacion',
      titulo: truncate(substeps[1].title, 70),
      xp: 10,
      cuerpo: truncate(stripMdNoise(substeps[1].body), 1100) || truncate(substeps[1].title, 200),
    });
  }

  if (substeps[2] && pasos.length < 7) {
    const c2 = substeps[2].codes[0];
    if (c2) {
      pasos.push({
        id: slugId(n++),
        tipo: 'ejemplo',
        titulo: truncate(substeps[2].title, 70),
        xp: 10,
        cuerpo: `\`\`\`${c2.lang}\n${truncate(c2.code, 1000)}\n\`\`\``,
      });
    } else {
      pasos.push({
        id: slugId(n++),
        tipo: 'explicacion',
        titulo: truncate(substeps[2].title, 70),
        xp: 10,
        cuerpo: truncate(stripMdNoise(substeps[2].body), 900) || truncate(substeps[2].title, 200),
      });
    }
  }

  // Resumen
  const puntos =
    hechoItems.length > 0
      ? hechoItems.map((x) => truncate(x.replace(/\*\*/g, ''), 180))
      : [
          `Repasaste: ${topic}`,
          evidencia ? `Evidencia: ${truncate(evidencia, 140)}` : 'Deja evidencia en projects/',
          'Sigue al siguiente nodo del camino',
        ];
  pasos.push({
    id: slugId(n++),
    tipo: 'resumen',
    titulo: 'Cierre',
    xp: 10,
    puntos: puntos.slice(0, 5),
    siguiente: 'Continúa en el mapa de la materia o abre la lectura complementaria abajo.',
  });

  // Clamp 5–8
  while (pasos.length > 8) {
    // remove middle explanations preferentially
    const idx = pasos.findIndex((p, i) => i > 1 && i < pasos.length - 1 && p.tipo === 'explicacion');
    if (idx > 0) pasos.splice(idx, 1);
    else pasos.splice(Math.floor(pasos.length / 2), 1);
  }
  while (pasos.length < 5) {
    pasos.splice(pasos.length - 1, 0, {
      id: slugId(900 + pasos.length),
      tipo: 'quiz',
      titulo: 'Comprobación rápida',
      xp: 10,
      variante: 'verdadero_falso',
      pregunta: 'Vale la pena releer el criterio «Hecho cuando» antes de marcar la lección.',
      opciones: [
        { id: 't', texto: 'Verdadero' },
        { id: 'f', texto: 'Falso' },
      ],
      respuesta: 't',
      explicacionError: 'Sí: el criterio evita autoengaño.',
      explicacionOk: 'Correcto.',
    });
  }

  // Re-id sequentially
  pasos.forEach((p, i) => {
    p.id = `s${i + 1}`;
  });

  return pasos;
}

function complementaryBody(content) {
  const trimmed = content.trim();
  return [
    '## Lectura complementaria',
    '',
    'Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.',
    '',
    trimmed,
  ].join('\n');
}

function migrateFile(filepath) {
  const raw = fs.readFileSync(filepath, 'utf8');
  const { data, content } = matter(raw);
  if (data.formato === 'pasos') {
    return { skipped: true, reason: 'already' };
  }

  const pasos = buildPasos(data, content);
  const xpLeccion = Math.min(
    120,
    Math.max(50, Math.round((Number(data.horas) || 2) * 30)),
  );

  const nextData = {
    id: String(data.id),
    materia: String(data.materia || ''),
    orden: Number(data.orden),
    titulo: String(data.titulo),
    horas: Number(data.horas ?? 0),
    semana: Number(data.semana ?? 0),
    lectura: String(data.lectura ?? ''),
    evidencia: String(data.evidencia ?? ''),
    formato: 'pasos',
    xpLeccion,
    pasos,
  };

  // Validate before write
  parseLeccionPasos(nextData);

  const body = complementaryBody(content);
  const out = matter.stringify(body, nextData);
  if (!dryRun) fs.writeFileSync(filepath, out, 'utf8');
  return { skipped: false, pasos: pasos.length };
}

function updateMateriaFicha(fichaPath) {
  if (!fs.existsSync(fichaPath)) return false;
  let text = fs.readFileSync(fichaPath, 'utf8');
  if (text.includes('motor paso a paso') || text.includes('formato Duolingo')) {
    return false;
  }

  const replacement = `## Cómo estudiar esta materia (lecciones)

Esta materia usa el **motor paso a paso** (tipo Duolingo): cada lección son 5–8 pasos cortos con explicación, ejemplos, quizzes y/o retos. Los libros y el detalle largo viven como **lectura complementaria**.

1. Abre el **Camino** en esta ficha y pulsa **Continuar** (respeta el orden).
2. En cada paso: lee o responde → **Comprobar** → feedback inmediato.
3. La lección se marca hecha al completar todos los pasos; la evidencia en \`projects/\` sigue siendo obligatoria.
4. Usa **Repaso diario** para preguntas falladas o ya vistas.
5. Método general: [Cómo estudiar](../../como-estudiar.md).
`;

  if (/## Cómo estudiar esta materia[\s\S]*?(?=\n## )/m.test(text)) {
    text = text.replace(
      /## Cómo estudiar esta materia[\s\S]*?(?=\n## )/m,
      `${replacement}\n`,
    );
  } else if (/## Cómo estudiar[\s\S]*?(?=\n## )/m.test(text)) {
    text = text.replace(/## Cómo estudiar[\s\S]*?(?=\n## )/m, `${replacement}\n`);
  } else {
    // insert after first H1 block
    text = text.replace(/(# [^\n]+\n)/, `$1\n${replacement}\n`);
  }

  if (!dryRun) fs.writeFileSync(fichaPath, text, 'utf8');
  return true;
}

let migrated = 0;
let skipped = 0;
let errors = 0;
const byMateria = {};

for (const etapa of fs.readdirSync(etapasRoot)) {
  const etapaDir = path.join(etapasRoot, etapa);
  if (!fs.statSync(etapaDir).isDirectory()) continue;
  for (const entry of fs.readdirSync(etapaDir)) {
    const mid = entry.match(/^(M\d{2})$/i)?.[1];
    if (!mid) continue;
    if (filter.size && !filter.has(mid.toUpperCase())) continue;

    const dir = path.join(etapaDir, mid);
    byMateria[mid] = { ok: 0, skip: 0, err: 0 };

    // ficha
    const fichas = fs
      .readdirSync(etapaDir)
      .filter((f) => f.startsWith(`${mid}-`) && f.endsWith('.md'));
    for (const f of fichas) {
      updateMateriaFicha(path.join(etapaDir, f));
    }

    for (const file of fs.readdirSync(dir).filter((f) => /^L\d{2}-.+\.md$/i.test(f))) {
      const filepath = path.join(dir, file);
      try {
        const res = migrateFile(filepath);
        if (res.skipped) {
          skipped += 1;
          byMateria[mid].skip += 1;
        } else {
          migrated += 1;
          byMateria[mid].ok += 1;
          console.log(`OK  ${mid}/${file} (${res.pasos} pasos)`);
        }
      } catch (e) {
        errors += 1;
        byMateria[mid].err += 1;
        console.error(`FAIL ${mid}/${file}`);
        console.error(e instanceof Error ? e.message : e);
      }
    }
  }
}

console.log('\n— Resumen —');
for (const [mid, s] of Object.entries(byMateria).sort()) {
  console.log(`${mid}: migradas=${s.ok} skip=${s.skip} err=${s.err}`);
}
console.log(
  `\nTotal migradas=${migrated} omitidas=${skipped} errores=${errors}${dryRun ? ' (dry-run)' : ''}`,
);
if (errors) process.exit(1);
