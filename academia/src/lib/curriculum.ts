import fs from 'node:fs';
import path from 'node:path';
import matter from 'gray-matter';
import { marked } from 'marked';

function resolveRepoRoot(): string {
  const candidates = [process.cwd(), path.resolve(process.cwd(), '..')];
  for (const dir of candidates) {
    if (fs.existsSync(path.join(dir, 'curriculum', 'catalog.json'))) return dir;
  }
  throw new Error('No se encontró curriculum/catalog.json. Ejecuta desde academia/ o la raíz del repo.');
}

export const repoRoot = resolveRepoRoot();
export const curriculumRoot = path.join(repoRoot, 'curriculum');

export type CatalogMateria = {
  id: string;
  slug: string;
  titulo: string;
  etapa: string;
  orden: number;
  semanas: number;
  horas: number;
  analogos: string[];
};

export type CatalogEtapa = {
  id: string;
  orden: number;
  titulo: string;
  slug: string;
  duracionMeses: string;
  objetivo: string;
};

export type Catalog = {
  programa: string;
  fuentes: string[];
  ritmoHorasSemana: number;
  etapas: CatalogEtapa[];
  materias: CatalogMateria[];
};

export type MateriaDoc = {
  id: string;
  titulo: string;
  etapa: string;
  orden: number;
  semanas: number;
  horas: number;
  practicas: { id: string; titulo: string }[];
  proyecto: { id: string; titulo: string } | null;
  bodyHtml: string;
  slug: string;
  filepath: string;
};

let catalogCache: Catalog | null = null;

export function getCatalog(): Catalog {
  if (catalogCache) return catalogCache;
  const raw = fs.readFileSync(path.join(curriculumRoot, 'catalog.json'), 'utf8');
  catalogCache = JSON.parse(raw) as Catalog;
  return catalogCache;
}

export function getEtapa(etapaId: string): CatalogEtapa | undefined {
  return getCatalog().etapas.find((e) => e.id === etapaId);
}

export function getMateriasByEtapa(etapaId: string): CatalogMateria[] {
  return getCatalog()
    .materias.filter((m) => m.etapa === etapaId)
    .sort((a, b) => a.orden - b.orden);
}

export function getMateriaMeta(id: string): CatalogMateria | undefined {
  return getCatalog().materias.find((m) => m.id === id);
}

function etapaFolder(etapaId: string): string {
  const etapa = getEtapa(etapaId);
  if (!etapa) throw new Error(`Etapa desconocida: ${etapaId}`);
  return path.join(curriculumRoot, 'etapas', etapa.slug);
}

export function loadMateria(id: string): MateriaDoc | null {
  const meta = getMateriaMeta(id);
  if (!meta) return null;
  const filepath = path.join(etapaFolder(meta.etapa), `${meta.slug}.md`);
  if (!fs.existsSync(filepath)) return null;
  const raw = fs.readFileSync(filepath, 'utf8');
  const { data, content } = matter(raw);
  const practicas = Array.isArray(data.practicas) ? data.practicas : [];
  const proyecto = data.proyecto ?? null;
  return {
    id: String(data.id ?? meta.id),
    titulo: String(data.titulo ?? meta.titulo),
    etapa: String(data.etapa ?? meta.etapa),
    orden: Number(data.orden ?? meta.orden),
    semanas: Number(data.semanas ?? meta.semanas),
    horas: Number(data.horas ?? meta.horas),
    practicas,
    proyecto,
    bodyHtml: marked.parse(content) as string,
    slug: meta.slug,
    filepath,
  };
}

export function loadMarkdownPage(relativePath: string): { title: string; html: string } {
  const filepath = path.join(curriculumRoot, relativePath);
  const raw = fs.readFileSync(filepath, 'utf8');
  const { data, content } = matter(raw);
  const html = marked.parse(content) as string;
  const title =
    (typeof data.title === 'string' && data.title) ||
    content.match(/^#\s+(.+)$/m)?.[1] ||
    relativePath;
  return { title, html };
}

export function getProgressSeed() {
  const filepath = path.join(repoRoot, 'progress.json');
  return JSON.parse(fs.readFileSync(filepath, 'utf8'));
}

export function totalStats() {
  const cat = getCatalog();
  return {
    materias: cat.materias.length,
    horas: cat.materias.reduce((acc, m) => acc + m.horas, 0),
    semanas: cat.materias.reduce((acc, m) => acc + m.semanas, 0),
  };
}
