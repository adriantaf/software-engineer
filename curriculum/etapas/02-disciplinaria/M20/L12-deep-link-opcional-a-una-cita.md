---
id: L12
materia: M20
orden: 12
titulo: Deep link opcional a una cita
horas: 5.0
semana: 3
lectura: Deep linking intro
evidencia: projects/m20-movil/deep-link.md
---

# L12 — Deep link opcional a una cita

**~5.0 h · Semana 3**

Preparación recordatorios WhatsApp futuro.

## Objetivo

Configurar esquema o ruta para abrir detalle desde URL/notificación futura.

## Conceptos clave

- deep link
- routing

## Pasos (hazlos en orden)

### 1. Deep link cita (60–80 min)

```bash
# Android intent-filter / iOS universal link — scheme agendaops://cita/<id>
cat > projects/m20-movil/deep-link.md << 'EOF'
# Deep links
Scheme: agendaops://cita/:id
Prueba: adb shell am start -a android.intent.action.VIEW -d "agendaops://cita/UUID"
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m20-movil/deep-link.md
git commit -m "feat(m20): L12 deep link cita"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Deep linking intro | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m20-movil/deep-link.md` con scheme y comando de prueba.
2. Commit `docs(m20): L12 deep-link-opcional-a-una-cita`.

## Errores comunes

- Deep link sin documentación de prueba.
- Abrir http genérico sin ruta.

## Siguiente

[L13 — Lista vacía con copy útil](L13-lista-vacia-con-copy-util.md)
