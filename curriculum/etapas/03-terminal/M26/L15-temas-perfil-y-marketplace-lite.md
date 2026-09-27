---
id: L15
materia: M26
orden: 15
titulo: Temas de perfil y marketplace lite
horas: 5.0
semana: 4
lectura: producto-saas — temas Free/Pro + catálogo
evidencia: projects/m26-capstone/temas-marketplace.md
---

# L15 — Temas de perfil y marketplace lite

**~5 h · Semana 4**

Capstone. Hoy entregas **`projects/m26-capstone/temas-marketplace.md`**.

## Objetivo

- ≥2 temas built-in (1 free, 1 pro/preview) aplicables al perfil/menú público.
- Catálogo con **1 tema de terceros** (Free o Paid listado) instalable por tenant.
- Documentar reparto a creadores; Stripe Connect real = v1.1 (no bloquea egreso).

## Formato de paquete (mínimo)

```
themes/<slug>/
  theme.json   # name, version, author, price_cents, preview
  styles.css   # o tokens
  README.md
```

## Pasos

### 1. Built-in (60–90 min)

Dos temas en el repo de la app; el tenant Free solo instala el free.

### 2. Terceros (60–90 min)

Publica un tema “de terceros” en el catálogo (puede ser tuyo con autor distinto). Instalación por tenant deja evidencia en `temas-marketplace.md`.

### 3. Billing temas (30 min)

Si el tema es Paid: checkout a la **plataforma** (Stripe test). Anota en el doc el % de reparto previsto (Connect = post-egreso).

### 4. Commit

```bash
git add projects/m26-capstone/temas-marketplace.md
git commit -m "docs(m26): l15 temas marketplace lite"
```

## Hecho cuando

1. Dos temas built-in + uno de terceros listado.
2. Un tenant demo con tema instalado distinto al default.
3. Doc de marketplace en git.

## Errores comunes

- Marketplace de apps completo (fuera de alcance).
- Bloquear egreso por Connect/payouts.

## Siguiente

[L16 — Demo interna semana 4 — flujos completos](L16-demo-interna-semana-4-flujos-completos.md)
