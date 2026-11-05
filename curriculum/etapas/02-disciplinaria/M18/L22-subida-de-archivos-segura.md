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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un .php disfrazado de .jpg es folklore porque sigue pasando.


      **Objetivo de esta lección:** Checklist o prueba real en
      `projects/m18-appsec/findings/005-upload.md`: tipo/tamaño, nombre
      aleatorio, fuera de webroot.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Superficie upload
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'multer|formidable|multipart|upload|createWriteStream' -g
      '!node_modules' | head -30

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Checklist / prueba
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'multer|formidable|multipart|upload|createWriteStream' -g
      '!node_modules' | head -30

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Subida de archivos segura», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Subida de archivos
          segura
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Checklist o prueba real en
          `projects/m18-appsec/findings/005-upload.md`: tipo/tamaño, nombre
          aleatorio, fuera de webroot.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Confiar en extensión."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
