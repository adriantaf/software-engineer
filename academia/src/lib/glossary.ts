/** Términos del glosario: fuente única para la página y el auto-enlace. */

export type GlossaryTerm = {
  /** Ancla en /docs/glosario#id */
  id: string;
  /** Forma canónica que se muestra y se busca (orden: más larga primero al linkear). */
  term: string;
  /** Otras grafías que deben linkear al mismo id. */
  aliases?: string[];
  /** Expansión corta en español (primera mención). */
  expansion: string;
  /** Definición de una línea para el glosario. */
  definition: string;
};

export const GLOSSARY_TERMS: GlossaryTerm[] = [
  {
    id: 'owasp',
    term: 'OWASP',
    expansion: 'proyecto abierto de seguridad en aplicaciones web',
    definition:
      'Comunidad y guías de seguridad web. Lo más citado: Top 10 (riesgos frecuentes) y cheat sheets.',
  },
  {
    id: 'saas',
    term: 'SaaS',
    expansion: 'software como servicio',
    definition:
      'Producto de software por suscripción en la nube (varios clientes), no un sitio a medida por proyecto.',
  },
  {
    id: 'api',
    term: 'API',
    expansion: 'interfaz de programación de aplicaciones',
    definition: 'Contrato que permite a un programa hablar con otro (p. ej. tu front con tu backend por HTTP).',
  },
  {
    id: 'adr',
    term: 'ADR',
    expansion: 'registro de decisión de arquitectura',
    definition: 'Nota corta que documenta una decisión técnica importante, el contexto y las consecuencias.',
  },
  {
    id: 'ci',
    term: 'CI',
    expansion: 'integración continua',
    definition: 'Pipeline automático (tests, lint, audit) que corre en cada push o pull request.',
  },
  {
    id: 'tls',
    term: 'TLS',
    expansion: 'seguridad de la capa de transporte',
    definition: 'Cifrado del canal en red; es lo que hace que HTTPS proteja los datos en tránsito.',
  },
  {
    id: 'https',
    term: 'HTTPS',
    expansion: 'HTTP sobre TLS',
    definition: 'Versión cifrada de HTTP. En producción tu producto debe ir siempre por HTTPS.',
  },
  {
    id: 'http',
    term: 'HTTP',
    expansion: 'protocolo de transferencia de hipertexto',
    definition: 'Protocolo básico de la web (peticiones y respuestas entre cliente y servidor).',
  },
  {
    id: 'idor',
    term: 'IDOR',
    expansion: 'referencia directa insegura a un objeto',
    definition:
      'Fallo de autorización: cambias un ID en la URL/API y accedes al recurso de otro usuario o tenant.',
  },
  {
    id: 'srs',
    term: 'SRS',
    expansion: 'especificación de requisitos de software',
    definition: 'Documento que describe qué debe hacer el sistema (funcional) y bajo qué condiciones (no funcional).',
  },
  {
    id: 'mvp',
    term: 'MVP',
    expansion: 'producto mínimo viable',
    definition: 'Primera versión pequeña pero útil para aprender del usuario real, no el producto “completo”.',
  },
  {
    id: 'xss',
    term: 'XSS',
    expansion: 'cross-site scripting',
    definition: 'Inyectar JavaScript malicioso en páginas que ven otros usuarios (a menudo por HTML sin escapar).',
  },
  {
    id: 'csrf',
    term: 'CSRF',
    expansion: 'falsificación de petición en sitios cruzados',
    definition: 'Engañar al navegador de un usuario autenticado para que haga una acción que él no pidió.',
  },
  {
    id: 'ssrf',
    term: 'SSRF',
    expansion: 'falsificación de petición del lado del servidor',
    definition: 'El servidor hace peticiones a URLs internas/externas elegidas por el atacante.',
  },
  {
    id: 'sqli',
    term: 'SQLi',
    aliases: ['SQL injection'],
    expansion: 'inyección SQL',
    definition: 'Input del usuario que altera la consulta a la base de datos. Se evita con queries parametrizadas.',
  },
  {
    id: 'jwt',
    term: 'JWT',
    expansion: 'JSON Web Token',
    definition: 'Token firmado que el cliente envía para probar identidad/sesión. Mal guardado + XSS = robo de sesión.',
  },
  {
    id: 'stride',
    term: 'STRIDE',
    expansion: 'modelo de amenazas en 6 categorías',
    definition:
      'Checklist de amenazas: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.',
  },
  {
    id: 'sdlc',
    term: 'SDLC',
    expansion: 'ciclo de vida del desarrollo de software',
    definition: 'Etapas de construir software (requisitos → diseño → build → test → deploy → operar). Secure SDLC incluye seguridad en todas.',
  },
  {
    id: 'appsec',
    term: 'AppSec',
    expansion: 'seguridad de aplicaciones',
    definition: 'Práctica de proteger el software: auth, autorización, tests de seguridad, proceso seguro.',
  },
  {
    id: 'rnf',
    term: 'RNF',
    expansion: 'requisitos no funcionales',
    definition: 'Cómo debe comportarse el sistema: seguridad, privacidad, rendimiento, disponibilidad, etc.',
  },
  {
    id: 'crud',
    term: 'CRUD',
    expansion: 'crear, leer, actualizar y borrar',
    definition: 'Las cuatro operaciones básicas sobre datos. Un CRUD solo no es un producto completo.',
  },
  {
    id: 'uml',
    term: 'UML',
    expansion: 'lenguaje unificado de modelado',
    definition: 'Notación de diagramas (clases, secuencia, casos de uso) para comunicar diseño.',
  },
  {
    id: 'llm',
    term: 'LLM',
    expansion: 'modelo de lenguaje grande',
    definition: 'Modelo tipo ChatGPT al que llamas por API. Hay que medir costo, calidad y fugas de datos.',
  },
  {
    id: 'rag',
    term: 'RAG',
    expansion: 'generación aumentada por recuperación',
    definition: 'Buscas documentos propios y se los pasas al LLM para responder con ese contexto (en SaaS: por tenant).',
  },
  {
    id: 'pii',
    term: 'PII',
    expansion: 'información de identificación personal',
    definition: 'Datos que identifican a una persona (nombre, teléfono, email, etc.). Trátalos con cuidado.',
  },
  {
    id: 'icp',
    term: 'ICP',
    expansion: 'perfil de cliente ideal',
    definition: 'Tipo de cliente al que le encaja tu producto (quién paga y por qué).',
  },
  {
    id: 'multi-tenant',
    term: 'multi-tenant',
    aliases: ['multitenant', 'Multi-tenant'],
    expansion: 'varios clientes en un solo sistema',
    definition: 'Una misma app sirve a muchos negocios (tenants) aislados. Clave: tenant_id y cero fugas entre ellos.',
  },
  {
    id: 'tenant-id',
    term: 'tenant_id',
    expansion: 'identificador del inquilino / negocio',
    definition: 'Campo que marca a qué negocio pertenece cada fila. Sin filtrarlo bien aparece IDOR cross-tenant.',
  },
  {
    id: 'dns',
    term: 'DNS',
    expansion: 'sistema de nombres de dominio',
    definition: 'Traduce nombres (ejemplo.com) a direcciones IP.',
  },
  {
    id: 'tcp',
    term: 'TCP',
    expansion: 'protocolo de control de transmisión',
    definition: 'Transporte confiable de datos entre dos extremos en Internet (base de gran parte de HTTP).',
  },
  {
    id: 'udp',
    term: 'UDP',
    expansion: 'protocolo de datagrama de usuario',
    definition: 'Transporte ligero sin garantía de entrega (útil en algunos casos; HTTP clásico usa TCP).',
  },
  {
    id: 'mitm',
    term: 'MITM',
    expansion: 'ataque de intermediario',
    definition: 'Alguien en el medio intercepta o altera la comunicación. TLS mitiga esto en tránsito.',
  },
  {
    id: 'acid',
    term: 'ACID',
    expansion: 'atomicidad, consistencia, aislamiento, durabilidad',
    definition: 'Garantías clásicas de una transacción en base de datos.',
  },
  {
    id: 'er',
    term: 'ER',
    expansion: 'entidad-relación',
    definition: 'Modelo visual de entidades y relaciones antes (o junto) al esquema SQL.',
  },
  {
    id: 'solid',
    term: 'SOLID',
    expansion: 'cinco principios de diseño orientado a objetos',
    definition: 'Guías (S, O, L, I, D) para código más mantenible. En la academia priorizamos S, O y D al inicio.',
  },
  {
    id: 'dry',
    term: 'DRY',
    expansion: 'no te repitas',
    definition: 'Evitar duplicar la misma lógica en muchos sitios; no significa abstraer demasiado pronto.',
  },
  {
    id: 'bfs',
    term: 'BFS',
    expansion: 'búsqueda en amplitud',
    definition: 'Recorrido de grafos nivel por nivel (útil para caminos más cortos no ponderados).',
  },
  {
    id: 'dfs',
    term: 'DFS',
    expansion: 'búsqueda en profundidad',
    definition: 'Recorrido de grafos bajando por una rama antes de volver (útil en muchas exploraciones).',
  },
  {
    id: 'dp',
    term: 'DP',
    expansion: 'programación dinámica',
    definition: 'Técnica de algoritmos: resolver subproblemas y reutilizar resultados (memoización / tabla).',
  },
  {
    id: 'gof',
    term: 'GoF',
    expansion: 'Gang of Four (patrones de diseño)',
    definition: 'Libro clásico de patrones (Factory, Strategy, Observer, etc.).',
  },
  {
    id: 'moscow',
    term: 'MoSCoW',
    expansion: 'priorización Must / Should / Could / Wont',
    definition: 'Método de priorización de requisitos: qué es obligatorio, deseable, opcional o fuera de alcance.',
  },
  {
    id: 'ihc',
    term: 'IHC',
    expansion: 'interacción humano-computadora',
    definition: 'Diseño y evaluación de cómo las personas usan la interfaz (usabilidad).',
  },
  {
    id: 'cli',
    term: 'CLI',
    expansion: 'interfaz de línea de comandos',
    definition: 'Programa que se usa desde la terminal (sin interfaz gráfica).',
  },
  {
    id: 'mrr',
    term: 'MRR',
    expansion: 'ingreso recurrente mensual',
    definition: 'Dinero de suscripciones que esperas cada mes. Métrica típica de un SaaS.',
  },
  {
    id: 'sql',
    term: 'SQL',
    expansion: 'lenguaje de consulta estructurado',
    definition: 'Lenguaje para preguntar y modificar bases de datos relacionales (PostgreSQL, MySQL, etc.).',
  },
  {
    id: 'ui',
    term: 'UI',
    expansion: 'interfaz de usuario',
    definition: 'Lo que la persona ve y toca: pantallas, botones, formularios.',
  },
  {
    id: 'ux',
    term: 'UX',
    expansion: 'experiencia de usuario',
    definition: 'Cómo se siente usar el producto de punta a punta (flujo, claridad, fricción).',
  },
  {
    id: 'mdn',
    term: 'MDN',
    expansion: 'Mozilla Developer Network',
    definition: 'Documentación web de referencia (HTML, CSS, JS, HTTP) — úsala en español cuando exista.',
  },
  {
    id: 'crm',
    term: 'CRM',
    expansion: 'gestión de relación con clientes',
    definition: 'Sistema para clientes, contactos y seguimiento. En esta academia el producto es Agenda Ops (citas/ops).',
  },
  {
    id: 'semver',
    term: 'semver',
    aliases: ['SemVer', 'SEMVER'],
    expansion: 'versionado semántico',
    definition: 'Versiones MAJOR.MINOR.PATCH (rompiente / feature / fix).',
  },
  {
    id: 'csp',
    term: 'CSP',
    expansion: 'Content Security Policy',
    definition: 'Cabecera HTTP que limita qué scripts/recursos puede cargar el navegador (mitiga XSS).',
  },
  {
    id: 'cors',
    term: 'CORS',
    expansion: 'intercambio de recursos de origen cruzado',
    definition: 'Reglas del navegador sobre si un sitio A puede llamar a una API en el dominio B.',
  },
  {
    id: 'big-o',
    term: 'Big-O',
    aliases: ['Big O'],
    expansion: 'notación de complejidad',
    definition: 'Cómo crece el tiempo/memoria de un algoritmo cuando crecen los datos (peor caso típico).',
  },
  {
    id: 'bst',
    term: 'BST',
    expansion: 'árbol de búsqueda binaria',
    definition: 'Árbol donde izquierda < nodo < derecha; base de muchas estructuras ordenadas.',
  },
  {
    id: 'orm',
    term: 'ORM',
    expansion: 'mapeo objeto-relacional',
    definition: 'Capa que habla SQL desde objetos/clases. Útil, pero debes entender el SQL que genera.',
  },
  {
    id: 'paas',
    term: 'PaaS',
    expansion: 'plataforma como servicio',
    definition: 'Hosting donde despliegas la app sin administrar todo el servidor (Render, Fly, Railway, etc.).',
  },
  {
    id: 'vps',
    term: 'VPS',
    expansion: 'servidor virtual privado',
    definition: 'Máquina virtual que administras tú (más control, más responsabilidad de seguridad/ops).',
  },
  {
    id: 'faq',
    term: 'FAQ',
    expansion: 'preguntas frecuentes',
    definition: 'Listado de preguntas y respuestas típicas (en M23: por tenant).',
  },
  {
    id: 'poc',
    term: 'PoC',
    expansion: 'prueba de concepto',
    definition: 'Experimento corto para validar si una idea técnica o de producto vale la pena.',
  },
  {
    id: 'pr',
    term: 'PR',
    aliases: ['PRs'],
    expansion: 'pull request',
    definition: 'Propuesta de cambio en Git (revisión + discusión) antes de fusionar a la rama principal.',
  },
  {
    id: 'wstg',
    term: 'WSTG',
    expansion: 'OWASP Web Security Testing Guide',
    definition: 'Guía de pruebas de seguridad web de OWASP (base de M25).',
  },
];

/** Variantes de búsqueda ordenadas de más larga a más corta (evita que HTTP coma HTTPS). */
export function glossaryMatchList(): { id: string; match: string; term: GlossaryTerm }[] {
  const out: { id: string; match: string; term: GlossaryTerm }[] = [];
  for (const term of GLOSSARY_TERMS) {
    const forms = [term.term, ...(term.aliases ?? [])];
    for (const match of forms) {
      out.push({ id: term.id, match, term });
    }
  }
  out.sort((a, b) => b.match.length - a.match.length);
  return out;
}

export function renderGlossaryMarkdown(): string {
  const lines = [
    '# Glosario de la academia',
    '',
    'Siglas y jerga que aparecen en las fichas. En las materias, cada sigla del glosario es un **enlace** a esta página; la **primera vez** en una ficha también verás la expansión entre paréntesis.',
    '',
    'Tip: usa el buscador del navegador (`Ctrl+F` / `Cmd+F`) o salta desde cualquier mención en azul.',
    '',
  ];
  const sorted = [...GLOSSARY_TERMS].sort((a, b) =>
    a.term.localeCompare(b.term, 'es', { sensitivity: 'base' }),
  );
  for (const t of sorted) {
    // HTML crudo: marked no soporta {#id} de Pandoc.
    lines.push(`<h2 id="${t.id}">${t.term}</h2>`);
    lines.push('');
    lines.push(`**${t.expansion}.** ${t.definition}`);
    lines.push('');
  }
  return lines.join('\n');
}
