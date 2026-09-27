# M17 — Aplicaciones web full-stack (Vitrina MVP)

Carpeta de **evidencia** del piloto web **Vitrina**. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Nace el piloto web: auth real, CRUD de menú/pedidos/categorías, roles owner/staff, pedido por WhatsApp (`wa.me`) con pago al recoger, y base documentada hacia multi-tenant.

## Arranque rápido

```bash
cd projects/m17-vitrina
cp .env.example .env   # cuando exista; nunca lo subas
# Levanta API + Postgres según stack.md
curl -sS http://localhost:3000/health
```

## Estructura esperada

```
projects/m17-vitrina/
├── README.md
├── stack.md                 # stack fijo (L01)
├── .env.example
├── docs/
│   ├── auth.md
│   ├── permisos.md
│   ├── ui-estados.md        # P2
│   ├── integracion-whatsapp.md  # P3 pedido wa.me
│   ├── deploy.md / smoke-test.md
│   ├── owasp-mapa.md
│   ├── adr-tenant-id.md
│   ├── checklist-saas.md
│   └── demo-script.md
├── src/ o apps/             # API + front
├── tests/                   # auth + roles + pedidos
└── scripts/seed.ts
```

## Dominio del piloto

- Menú: categorías + ítems (precio, disponibilidad)
- Pedidos: estados recibido → listo → entregado; cliente (nombre + WhatsApp)
- Perfil público: menú (core); landing opcional
- Pago al recoger (default); checkout online = flag futuro (M26)

## Spec

[producto-saas.md](../../curriculum/producto-saas.md) · [Hilo producto](../../curriculum/hilos/producto.md)
