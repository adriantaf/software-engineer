import { glossaryMatchList, type GlossaryTerm } from './glossary';
import { pathTo } from './paths';

const SKIP_TAGS = new Set(['a', 'code', 'pre', 'script', 'style', 'kbd', 'samp']);
const NO_EXPAND_TAGS = new Set(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title']);

function escapeRe(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function buildMatcher() {
  const list = glossaryMatchList();
  const parts = list.map(({ match }) => {
    const e = escapeRe(match);
    if (/_/.test(match)) return e;
    if (/[()]/.test(match)) return e;
    return `\\b${e}\\b`;
  });
  const re = new RegExp(`(${parts.join('|')})`, 'g');
  const byMatch = new Map(list.map((x) => [x.match, x]));
  return { re, byMatch };
}

const MATCHER = buildMatcher();

/**
 * Enlaza siglas del glosario. Primera mención en el documento: añade expansión
 * (salvo en títulos). No toca contenido dentro de <a>, <code>, <pre>, etc.
 */
export function linkGlossaryTerms(html: string, options?: { expandFirst?: boolean }): string {
  const expandFirst = options?.expandFirst !== false;
  const base = pathTo('docs/glosario');
  const seen = new Set<string>();
  let skipDepth = 0;
  let headingDepth = 0;

  return html.replace(/<\/?([A-Za-z][\w:-]*)\b[^>]*>|([^<]+)/g, (chunk, tagName?: string, text?: string) => {
    if (tagName) {
      const name = tagName.toLowerCase();
      const closing = chunk.startsWith('</');
      const selfClosing = /\/>$/.test(chunk);
      if (SKIP_TAGS.has(name)) {
        if (closing) skipDepth = Math.max(0, skipDepth - 1);
        else if (!selfClosing) skipDepth += 1;
      }
      if (NO_EXPAND_TAGS.has(name)) {
        if (closing) headingDepth = Math.max(0, headingDepth - 1);
        else if (!selfClosing) headingDepth += 1;
      }
      return chunk;
    }
    if (!text || skipDepth > 0) return chunk;

    return text.replace(MATCHER.re, (raw: string) => {
      const entry = MATCHER.byMatch.get(raw);
      if (!entry) return raw;
      const { id, term } = entry;
      const href = `${base}#${id}`;
      const title = `${term.term}: ${term.expansion}`;
      const link = `<a class="glossary-term" href="${href}" title="${escapeAttr(title)}">${raw}</a>`;
      // En títulos solo enlace (evita "AppSec (…)" dentro del h1).
      if (headingDepth > 0) return link;
      if (!expandFirst || seen.has(id)) return link;
      seen.add(id);
      return `${link} <span class="glossary-expand">(${escapeHtml(term.expansion)})</span>`;
    });
  });
}

function escapeAttr(s: string): string {
  return s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
}

function escapeHtml(s: string): string {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

/** Añade id a h2/h3 para índice de la materia. */
export function addHeadingAnchors(html: string): string {
  return html.replace(/<h([2-3])(\s[^>]*)?>([\s\S]*?)<\/h\1>/gi, (_full, level: string, attrs = '', inner: string) => {
    if (/\sid\s*=/i.test(attrs)) return `<h${level}${attrs}>${inner}</h${level}>`;
    const text = inner.replace(/<[^>]+>/g, '').trim();
    const id = slugifyHeading(text);
    if (!id) return `<h${level}${attrs}>${inner}</h${level}>`;
    return `<h${level}${attrs} id="${id}">${inner}</h${level}>`;
  });
}

export function extractToc(html: string): { id: string; text: string; level: number }[] {
  const toc: { id: string; text: string; level: number }[] = [];
  const re = /<h([2-3])\b[^>]*\bid="([^"]+)"[^>]*>([\s\S]*?)<\/h\1>/gi;
  let m: RegExpExecArray | null;
  while ((m = re.exec(html))) {
    toc.push({
      level: Number(m[1]),
      id: m[2]!,
      text: m[3]!.replace(/<[^>]+>/g, '').trim(),
    });
  }
  return toc;
}

function slugifyHeading(text: string): string {
  return text
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 80);
}

export type { GlossaryTerm };
