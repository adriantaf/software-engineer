---
id: L22
materia: M18
orden: 22
titulo: Subida de archivos segura
horas: 5
semana: 6
lectura: File Upload Cheat Sheet
evidencia: projects/m18-appsec/findings/005-upload.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Checklist o prueba real en
      `projects/m18-appsec/findings/005-upload.md`: tipo/tamaño, nombre
      aleatorio, fuera de webroot.


      Un .php disfrazado de .jpg es folklore porque sigue pasando.
  - id: s2
    tipo: ejemplo
    titulo: 1. Superficie upload
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'multer|formidable|multipart|upload|createWriteStream' -g
      '!node_modules' | head -30

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Subida de archivos segura" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m18-appsec/findings/005-upload.md
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Checklist o prueba real en
          `projects/m18-appsec/findings/005-upload.md`: tipo/tamaño, nombre
          aleatorio, fuera de webroot.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Checklist / prueba
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/findings/005-upload.md <<'EOF'
      Finding 005 — Upload
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Checklist o prueba real (artefacto:
        `projects/m18-appsec/findings/005-upload.md`).
      - >-
        Ruta almacenamiento (artefacto:
        `projects/m18-appsec/findings/005-upload.md`).
      - 'Commit `docs(m18): L22 subida-de-archivos-segura`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L22 — Subida de archivos segura

**~5.0 h · Semana 6**

Un .php disfrazado de .jpg es folklore porque sigue pasando.

## Objetivo

Checklist o prueba real en `projects/m18-appsec/findings/005-upload.md`: tipo/tamaño, nombre aleatorio, fuera de webroot.

## Pasos

### 1. Superficie upload (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'multer|formidable|multipart|upload|createWriteStream' -g '!node_modules' | head -30
```
### 2. Checklist / prueba (70–90 min)

```bash
cat > projects/m18-appsec/findings/005-upload.md <<'EOF'
# Finding 005 — Upload
## ¿Hay upload hoy?
- ruta / campo:

## Controles
| Control | Sí/No |
|---------|-------|
| Allowlist MIME + magic bytes | |
| Tamaño máximo | |
| Nombre aleatorio (uuid) | |
| Fuera de `public/` / webroot | |
| No ejecutable por el server | |

## Prueba (si aplica)
- archivo: `pocs/evil.jpg.html` o similar
- resultado:
EOF
```

```ts
// multer sketch
const upload = multer({
  storage: multer.diskStorage({
    destination: "/var/agenda/uploads", // fuera de public
    filename: (_req, _file, cb) => cb(null, `${crypto.randomUUID()}`),
  }),
  limits: { fileSize: 2_000_000 },
  fileFilter: (_req, file, cb) => {
    cb(null, ["image/png", "image/jpeg"].includes(file.mimetype));
  },
});
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/005-upload.md
git commit -m "docs(m18): l22 upload checklist"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | File Upload Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Checklist o prueba real (artefacto: `projects/m18-appsec/findings/005-upload.md`).
2. Ruta almacenamiento (artefacto: `projects/m18-appsec/findings/005-upload.md`).
3. Commit `docs(m18): L22 subida-de-archivos-segura`.

## Errores comunes

- Guardar en `public/` con nombre usuario.
- Confiar en extensión.

## Siguiente

[L23 — Deserialización y JSON peligroso](L23-deserializacion-y-json-peligroso.md)
