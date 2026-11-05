#!/usr/bin/env node
/**
 * Valida lecciones con formato: pasos (Zod).
 * Uso: node scripts/validate-lessons.mjs [materiaId…]
 * Sin args: valida todas las lecciones en formato pasos.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import matter from 'gray-matter';
import { isPasosFrontmatter, parseLeccionPasos } from '../src/lib/lesson-schema.ts';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '../..');
const etapasRoot = path.join(repoRoot, 'curriculum/etapas');

const filterMaterias = new Set(process.argv.slice(2).map((s) => s.toUpperCase()));

let checked = 0;
let errors = 0;

for (const etapa of fs.readdirSync(etapasRoot)) {
  const etapaDir = path.join(etapasRoot, etapa);
  if (!fs.statSync(etapaDir).isDirectory()) continue;
  for (const entry of fs.readdirSync(etapaDir)) {
    if (!/^M\d{2}$/i.test(entry)) continue;
    if (filterMaterias.size && !filterMaterias.has(entry.toUpperCase())) continue;
    const dir = path.join(etapaDir, entry);
    for (const file of fs.readdirSync(dir).filter((f) => /^L\d{2}-.+\.md$/i.test(f))) {
      const filepath = path.join(dir, file);
      const raw = fs.readFileSync(filepath, 'utf8');
      const { data } = matter(raw);
      if (!isPasosFrontmatter(data)) continue;
      checked += 1;
      try {
        parseLeccionPasos(data);
        console.log(`OK  ${entry}/${file} (${data.pasos?.length ?? 0} pasos)`);
      } catch (e) {
        errors += 1;
        console.error(`FAIL ${entry}/${file}`);
        console.error(e instanceof Error ? e.message : e);
      }
    }
  }
}

if (checked === 0) {
  console.log('Ninguna lección con formato: pasos' + (filterMaterias.size ? ` en ${[...filterMaterias].join(',')}` : ''));
}
if (errors) {
  console.error(`\n${errors} lección(es) inválidas de ${checked} revisadas.`);
  process.exit(1);
}
console.log(`\n${checked} lección(es) válidas.`);
