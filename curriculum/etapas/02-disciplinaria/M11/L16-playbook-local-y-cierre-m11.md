---
id: L16
materia: M11
orden: 16
titulo: Playbook local y cierre M11
horas: 5
semana: 4
lectura: "Ficha M11 proyecto"
evidencia: "playbook.md + README"
---

# L16 — Playbook local y cierre M11

**~5 h · Semana 4**

## Objetivo

Completar `playbook.md` (up/down/backup/restore) y auditar P1–P3.

## Por qué importa

Otro dev debe levantar Agenda Ops local solo con el playbook.

## Conceptos

- runbook.
- handoff M19.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Diagrama Mermaid host→contenedores→volumen. Checklist ficha. Bitácora cierre.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l16 playbook-local-y-cierre-m11"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M11-sistemas-operativos.md | producto-saas.md |
| Catálogo | Entrada M11 | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

1. Playbook completo.
2. P1–P3 verificados.
3. Commit cierre M11.

## Errores comunes

- Playbook sin restore.
- Olvidar usuario no-root en doc.
