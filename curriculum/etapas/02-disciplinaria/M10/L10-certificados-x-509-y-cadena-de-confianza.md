---
id: L10
materia: M10
orden: 10
titulo: Certificados X.509 y cadena de confianza
horas: 5
semana: 3
lectura: "MDN certificate transparency (idea) + Tanenbaum PKI intro"
evidencia: "labs/certificados.md"
---

# L10 — Certificados X.509 y cadena de confianza

**~5 h · Semana 3**

## Objetivo

Leer subject, SAN, fechas de validez y cadena hasta una CA de confianza del sistema.

## Por qué importa

Renovaciones fallidas y nombres mal emitidos tumban el piloto Agenda Ops en viernes por la tarde.

## Conceptos

- CN/SAN.
- CA intermedia.
- Revocación (CRL/OCSP, idea).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
echo | openssl s_client -showcerts -connect example.com:443 2>/dev/null | openssl x509 -noout -text | head -40
```

Anota algoritmo de firma y fechas. ¿Qué pasa si expira mañana?

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l10 certificados-x-509-y-cadena-de-confianza"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | Digital certificates | openssl x509 man |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. Campos del cert explicados.
2. Plan de renovación (Let's Encrypt u otro) esbozado.
3. Riesgo nombre incorrecto documentado.

## Errores comunes

- Aceptar certificados autofirmados en prod sin proceso.
- Olvidar SAN al emitir para subdominio API.

## Siguiente

[L11 — Lab openssl y pinning conceptual](L11-lab-openssl-y-pinning-conceptual.md)
