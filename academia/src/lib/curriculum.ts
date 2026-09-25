import fs from 'node:fs';
import path from 'node:path';
import matter from 'gray-matter';
import { marked } from 'marked';
import { pathTo } from './paths';
import { addHeadingAnchors, extractToc, linkGlossaryTerms } from './glossary-link';

function resolveRepoRoot(): string {
  const candidates = [process.cwd(), path.resolve(process.cwd(), '..')];
  for (const dir of candidates) {
    if (fs.existsSync(path.join(dir, 'curriculum', 'catalog.json'))) return dir;
  }
  throw new Error('No se encontró curriculum/catalog.json. Ejecuta desde academia/ o la raíz del repo.');
}

export const repoRoot = resolveRepoRoot();
export const curriculumRoot = path.join(repoRoot, 'curriculum');

marked.setOptions({ gfm: true });

/** Páginas de la academia para archivos bajo curriculum/. */
const CURRICULUM_PAGE_ROUTES: Record<string, string> = {
  'INDEX.md': 'docs/index',
  'bibliografia.md': 'docs/bibliografia',
  'glosario.md': 'docs/glosario',
  'como-estudiar.md': 'docs/como-estudiar',
  'filosofia.md': 'docs/filosofia',
  'producto-saas.md': 'docs/producto-saas',
  'equivalencias.md': 'docs/equivalencias',
  'egreso.md': 'egreso',
  'nivel.md': 'nivel',
  'hilos/seguridad.md': 'docs/seguridad',
};

const GITHUB_BLOB =
  'https://github.com/adriantaf/software-engineer/blob/main';

/**
 * Convierte hrefs relativos a .md del currículo en rutas de la web
 * (p. ej. ../../bibliografia.md → /software-engineer/docs/bibliografia).
 */
export function rewriteCurriculumHref(href: string, fromCurriculumFile: string): string {
  if (!href || /^(https?:|mailto:|tel:|data:)/i.test(href)) return href;
  if (href.startsWith('#') || href.startsWith('/')) return href;

  const hashIdx = href.indexOf('#');
  const pathPart = hashIdx >= 0 ? href.slice(0, hashIdx) : href;
  const hash = hashIdx >= 0 ? href.slice(hashIdx) : '';
  if (!pathPart) return href;

  const fromDir = path.dirname(path.join(curriculumRoot, fromCurriculumFile));
  const abs = path.resolve(fromDir, decodeURIComponent(pathPart));
  const curriculumRel = path.relative(curriculumRoot, abs).replace(/\\/g, '/');
  const repoRel = path.relative(repoRoot, abs).replace(/\\/g, '/');

  if (!curriculumRel.startsWith('..')) {
    const route = CURRICULUM_PAGE_ROUTES[curriculumRel];
    if (route) return `${pathTo(route)}${hash}`;

    const materia = curriculumRel.match(/^etapas\/[^/]+\/(M\d{2})-[^/]+\.md$/i);
    if (materia) return `${pathTo(`materia/${materia[1]}`)}${hash}`;

    if (/\.md$/i.test(curriculumRel)) {
      return `${GITHUB_BLOB}/curriculum/${curriculumRel}${hash}`;
    }
  }

  if (!repoRel.startsWith('..') && /\.(md|txt|json)$/i.test(repoRel)) {
    return `${GITHUB_BLOB}/${repoRel}${hash}`;
  }

  return href;
}

function rewriteHtmlHrefs(html: string, fromCurriculumFile: string): string {
  return html.replace(/\bhref=(["'])([^"']+)\1/gi, (_full, quote: string, href: string) => {
    const next = rewriteCurriculumHref(href, fromCurriculumFile);
    return `href=${quote}${next}${quote}`;
  });
}

function renderCurriculumMarkdown(content: string, fromCurriculumFile: string): string {
  let html = marked.parse(content) as string;
  html = rewriteHtmlHrefs(html, fromCurriculumFile);
  html = addHeadingAnchors(html);
  // En el propio glosario no auto-enlazamos (ya están las anclas).
  if (!fromCurriculumFile.replace(/\\/g, '/').endsWith('glosario.md')) {
    html = linkGlossaryTerms(html, { expandFirst: true });
  }
  return html;
}

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
  toc: { id: string; text: string; level: number }[];
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
  const bodyHtml = renderCurriculumMarkdown(content, path.relative(curriculumRoot, filepath));
  return {
    id: String(data.id ?? meta.id),
    titulo: String(data.titulo ?? meta.titulo),
    etapa: String(data.etapa ?? meta.etapa),
    orden: Number(data.orden ?? meta.orden),
    semanas: Number(data.semanas ?? meta.semanas),
    horas: Number(data.horas ?? meta.horas),
    practicas,
    proyecto,
    bodyHtml,
    toc: extractToc(bodyHtml).filter(
      (t) => t.level === 2 && !/^ejemplo\b/i.test(t.text) && !/^d[ií]a\s*1\b/i.test(t.text),
    ),
    slug: meta.slug,
    filepath,
  };
}

export function loadMarkdownPage(relativePath: string): { title: string; html: string } {
  const filepath = path.join(curriculumRoot, relativePath);
  const raw = fs.readFileSync(filepath, 'utf8');
  const { data, content } = matter(raw);
  const html = renderCurriculumMarkdown(content, relativePath.replace(/\\/g, '/'));
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
