# Glosario de la academia

Siglas y jerga que aparecen en las fichas. En las materias, cada sigla del glosario es un **enlace** a esta página; la **primera vez** en una ficha también verás la expansión entre paréntesis.

Tip: usa el buscador del navegador (`Ctrl+F` / `Cmd+F`) o salta desde cualquier mención en azul.

<h2 id="acid">ACID</h2>

**atomicidad, consistencia, aislamiento, durabilidad.** Garantías clásicas de una transacción en base de datos.

<h2 id="adr">ADR</h2>

**registro de decisión de arquitectura.** Nota corta que documenta una decisión técnica importante, el contexto y las consecuencias.

<h2 id="api">API</h2>

**interfaz de programación de aplicaciones.** Contrato que permite a un programa hablar con otro (p. ej. tu front con tu backend por HTTP).

<h2 id="appsec">AppSec</h2>

**seguridad de aplicaciones.** Práctica de proteger el software: auth, autorización, tests de seguridad, proceso seguro.

<h2 id="bfs">BFS</h2>

**búsqueda en amplitud.** Recorrido de grafos nivel por nivel (útil para caminos más cortos no ponderados).

<h2 id="big-o">Big-O</h2>

**notación de complejidad.** Cómo crece el tiempo/memoria de un algoritmo cuando crecen los datos (peor caso típico).

<h2 id="bst">BST</h2>

**árbol de búsqueda binaria.** Árbol donde izquierda < nodo < derecha; base de muchas estructuras ordenadas.

<h2 id="ci">CI</h2>

**integración continua.** Pipeline automático (tests, lint, audit) que corre en cada push o pull request.

<h2 id="cli">CLI</h2>

**interfaz de línea de comandos.** Programa que se usa desde la terminal (sin interfaz gráfica).

<h2 id="cors">CORS</h2>

**intercambio de recursos de origen cruzado.** Reglas del navegador sobre si un sitio A puede llamar a una API en el dominio B.

<h2 id="crm">CRM</h2>

**gestión de relación con clientes.** Sistema para clientes, contactos y seguimiento. En esta academia el producto es Agenda Ops (citas/ops).

<h2 id="crud">CRUD</h2>

**crear, leer, actualizar y borrar.** Las cuatro operaciones básicas sobre datos. Un CRUD solo no es un producto completo.

<h2 id="csp">CSP</h2>

**Content Security Policy.** Cabecera HTTP que limita qué scripts/recursos puede cargar el navegador (mitiga XSS).

<h2 id="csrf">CSRF</h2>

**falsificación de petición en sitios cruzados.** Engañar al navegador de un usuario autenticado para que haga una acción que él no pidió.

<h2 id="dfs">DFS</h2>

**búsqueda en profundidad.** Recorrido de grafos bajando por una rama antes de volver (útil en muchas exploraciones).

<h2 id="dns">DNS</h2>

**sistema de nombres de dominio.** Traduce nombres (ejemplo.com) a direcciones IP.

<h2 id="dp">DP</h2>

**programación dinámica.** Técnica de algoritmos: resolver subproblemas y reutilizar resultados (memoización / tabla).

<h2 id="dry">DRY</h2>

**no te repitas.** Evitar duplicar la misma lógica en muchos sitios; no significa abstraer demasiado pronto.

<h2 id="er">ER</h2>

**entidad-relación.** Modelo visual de entidades y relaciones antes (o junto) al esquema SQL.

<h2 id="faq">FAQ</h2>

**preguntas frecuentes.** Listado de preguntas y respuestas típicas (en M23: por tenant).

<h2 id="gof">GoF</h2>

**Gang of Four (patrones de diseño).** Libro clásico de patrones (Factory, Strategy, Observer, etc.).

<h2 id="http">HTTP</h2>

**protocolo de transferencia de hipertexto.** Protocolo básico de la web (peticiones y respuestas entre cliente y servidor).

<h2 id="https">HTTPS</h2>

**HTTP sobre TLS.** Versión cifrada de HTTP. En producción tu producto debe ir siempre por HTTPS.

<h2 id="icp">ICP</h2>

**perfil de cliente ideal.** Tipo de cliente al que le encaja tu producto (quién paga y por qué).

<h2 id="idor">IDOR</h2>

**referencia directa insegura a un objeto.** Fallo de autorización: cambias un ID en la URL/API y accedes al recurso de otro usuario o tenant.

<h2 id="ihc">IHC</h2>

**interacción humano-computadora.** Diseño y evaluación de cómo las personas usan la interfaz (usabilidad).

<h2 id="jwt">JWT</h2>

**JSON Web Token.** Token firmado que el cliente envía para probar identidad/sesión. Mal guardado + XSS = robo de sesión.

<h2 id="llm">LLM</h2>

**modelo de lenguaje grande.** Modelo tipo ChatGPT al que llamas por API. Hay que medir costo, calidad y fugas de datos.

<h2 id="mdn">MDN</h2>

**Mozilla Developer Network.** Documentación web de referencia (HTML, CSS, JS, HTTP) — úsala en español cuando exista.

<h2 id="mitm">MITM</h2>

**ataque de intermediario.** Alguien en el medio intercepta o altera la comunicación. TLS mitiga esto en tránsito.

<h2 id="moscow">MoSCoW</h2>

**priorización Must / Should / Could / Wont.** Método de priorización de requisitos: qué es obligatorio, deseable, opcional o fuera de alcance.

<h2 id="mrr">MRR</h2>

**ingreso recurrente mensual.** Dinero de suscripciones que esperas cada mes. Métrica típica de un SaaS.

<h2 id="multi-tenant">multi-tenant</h2>

**varios clientes en un solo sistema.** Una misma app sirve a muchos negocios (tenants) aislados. Clave: tenant_id y cero fugas entre ellos.

<h2 id="mvp">MVP</h2>

**producto mínimo viable.** Primera versión pequeña pero útil para aprender del usuario real, no el producto “completo”.

<h2 id="orm">ORM</h2>

**mapeo objeto-relacional.** Capa que habla SQL desde objetos/clases. Útil, pero debes entender el SQL que genera.

<h2 id="owasp">OWASP</h2>

**proyecto abierto de seguridad en aplicaciones web.** Comunidad y guías de seguridad web. Lo más citado: Top 10 (riesgos frecuentes) y cheat sheets.

<h2 id="paas">PaaS</h2>

**plataforma como servicio.** Hosting donde despliegas la app sin administrar todo el servidor (Render, Fly, Railway, etc.).

<h2 id="pii">PII</h2>

**información de identificación personal.** Datos que identifican a una persona (nombre, teléfono, email, etc.). Trátalos con cuidado.

<h2 id="poc">PoC</h2>

**prueba de concepto.** Experimento corto para validar si una idea técnica o de producto vale la pena.

<h2 id="pr">PR</h2>

**pull request.** Propuesta de cambio en Git (revisión + discusión) antes de fusionar a la rama principal.

<h2 id="rag">RAG</h2>

**generación aumentada por recuperación.** Buscas documentos propios y se los pasas al LLM para responder con ese contexto (en SaaS: por tenant).

<h2 id="rnf">RNF</h2>

**requisitos no funcionales.** Cómo debe comportarse el sistema: seguridad, privacidad, rendimiento, disponibilidad, etc.

<h2 id="saas">SaaS</h2>

**software como servicio.** Producto de software por suscripción en la nube (varios clientes), no un sitio a medida por proyecto.

<h2 id="sdlc">SDLC</h2>

**ciclo de vida del desarrollo de software.** Etapas de construir software (requisitos → diseño → build → test → deploy → operar). Secure SDLC incluye seguridad en todas.

<h2 id="semver">semver</h2>

**versionado semántico.** Versiones MAJOR.MINOR.PATCH (rompiente / feature / fix).

<h2 id="solid">SOLID</h2>

**cinco principios de diseño orientado a objetos.** Guías (S, O, L, I, D) para código más mantenible. En la academia priorizamos S, O y D al inicio.

<h2 id="sql">SQL</h2>

**lenguaje de consulta estructurado.** Lenguaje para preguntar y modificar bases de datos relacionales (PostgreSQL, MySQL, etc.).

<h2 id="sqli">SQLi</h2>

**inyección SQL.** Input del usuario que altera la consulta a la base de datos. Se evita con queries parametrizadas.

<h2 id="srs">SRS</h2>

**especificación de requisitos de software.** Documento que describe qué debe hacer el sistema (funcional) y bajo qué condiciones (no funcional).

<h2 id="ssrf">SSRF</h2>

**falsificación de petición del lado del servidor.** El servidor hace peticiones a URLs internas/externas elegidas por el atacante.

<h2 id="stride">STRIDE</h2>

**modelo de amenazas en 6 categorías.** Checklist de amenazas: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.

<h2 id="tcp">TCP</h2>

**protocolo de control de transmisión.** Transporte confiable de datos entre dos extremos en Internet (base de gran parte de HTTP).

<h2 id="tenant-id">tenant_id</h2>

**identificador del inquilino / negocio.** Campo que marca a qué negocio pertenece cada fila. Sin filtrarlo bien aparece IDOR cross-tenant.

<h2 id="tls">TLS</h2>

**seguridad de la capa de transporte.** Cifrado del canal en red; es lo que hace que HTTPS proteja los datos en tránsito.

<h2 id="udp">UDP</h2>

**protocolo de datagrama de usuario.** Transporte ligero sin garantía de entrega (útil en algunos casos; HTTP clásico usa TCP).

<h2 id="ui">UI</h2>

**interfaz de usuario.** Lo que la persona ve y toca: pantallas, botones, formularios.

<h2 id="uml">UML</h2>

**lenguaje unificado de modelado.** Notación de diagramas (clases, secuencia, casos de uso) para comunicar diseño.

<h2 id="ux">UX</h2>

**experiencia de usuario.** Cómo se siente usar el producto de punta a punta (flujo, claridad, fricción).

<h2 id="vps">VPS</h2>

**servidor virtual privado.** Máquina virtual que administras tú (más control, más responsabilidad de seguridad/ops).

<h2 id="wstg">WSTG</h2>

**OWASP Web Security Testing Guide.** Guía de pruebas de seguridad web de OWASP (base de M25).

<h2 id="xss">XSS</h2>

**cross-site scripting.** Inyectar JavaScript malicioso en páginas que ven otros usuarios (a menudo por HTML sin escapar).
