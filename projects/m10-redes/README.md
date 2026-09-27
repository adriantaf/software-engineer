# M10 — Redes de computadoras

Carpeta de **evidencia** + labs de red/HTTP/TLS del producto. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Sigues el viaje de una petición (DNS → TCP → TLS → HTTP) y anotas qué puede fallar en **tu** producto (Agenda Ops).

## Arranque rápido

```bash
mkdir -p projects/m10-redes/{labs,tcp-echo,superficie,samples}
cd projects/m10-redes
curl -v https://example.com -o /dev/null 2>&1 | tee labs/curl-example.log
```

## Estructura

```
projects/m10-redes/
├── README.md
├── labs/                 # P1 — bitácoras por semana / tema
├── samples/              # fragmentos curl/openssl (sin secretos)
├── tcp-echo/             # P2 — cliente/servidor TCP
├── superficie/           # P3 — endpoints y datos
├── amenazas-enlace.md    # semana 3
└── amenazas-red.md       # proyecto
```

## Lecciones → artefactos

| Semana | Lecciones | Qué debe existir aquí |
|--------|-----------|------------------------|
| 1 | L01–L04 | `labs/dia1.md`, `labs/semana-01.md`, log curl |
| 2 | L05–L08 | DNS dig, HTTP métodos/status, curl timings |
| 3 | L09–L12 | TLS/certs/openssl, `amenazas-enlace.md` |
| 4 | L13–L16 | cookies, sesiones, CORS, security headers |
| 5 | L17–L20 | `superficie/`, `tcp-echo/`, `amenazas-red.md` |

## Checklist (Evidencia de hecho)

- **P1 — Labs:** `labs/` con curl/DNS/TLS anotados.
- **P2 — TCP:** `tcp-echo/` + diagrama de una request.
- **P3 — Superficie:** `superficie/endpoints.md`.
- **Proyecto — Doc:** `amenazas-red.md` enlazado a M18.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M10-redes.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M10/`
- Plan: `/materia/M10/`
- Bibliografía: `curriculum/bibliografia.md#m10-redes`
- Producto: `curriculum/producto-saas.md`
- Hilo seguridad: `curriculum/hilos/seguridad.md`
