---
id: L16
materia: M18
orden: 16
titulo: XSS almacenado y escape en plantillas/API
horas: 5
semana: 4
lectura: "DOM XSS + stored XSS"
evidencia: "commit fix + findings/002 actualizado"
---

# L16 — XSS almacenado y escape en plantillas/API

**~5 h · Semana 4**

## Objetivo

Mitigar XSS (escape, sanitización acotada, CSP futura) en el flujo almacenado (notas de cita, perfil).

## Por qué importa

El CRM guarda texto que vuelve a listarse; ahí vive el stored XSS.

## Conceptos

- Sanitizar HTML vs texto plano.
- JSON no implica seguro en `dangerouslySetInnerHTML`.
- Headers X-Content-Type-Options.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Si hay notas/comentarios en citas, prueba almacenamiento. Fix en template/API. Test: payload guardado se muestra escapado.

Tabla P2 en `projects/m18-appsec/findings-table.md` con filas SQLi + XSS (hallazgo → PoC → commit → test).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l16 xss-almacenado-y-escape-en-plantillas-ap"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | XSS Prevention | MDN textContent |

## Hecho cuando

1. ≥2 filas en findings-table.
2. Fix committed.
3. Test o verificación manual repetible.

## Errores comunes

- strip_tags inventado.
- innerHTML con input usuario.

## Siguiente

[L17 — IDOR en citas y recursos por ID](L17-idor-en-citas-y-recursos-por-id.md)
