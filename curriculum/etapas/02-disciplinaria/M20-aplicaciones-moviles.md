---
id: M20
titulo: Aplicaciones móviles
etapa: disciplinaria
orden: 20
semanas: 5
horas: 100
practicas:
  - id: p1
    titulo: "App cliente: login + lista de citas"
  - id: p2
    titulo: Estados vacíos/error + storage seguro de sesión
  - id: p3
    titulo: Build instalable (APK o equivalente)
proyecto:
  id: proj
  titulo: App móvil del CRM conectada al backend
---

# M20 — Aplicaciones móviles

## Por qué existe
El dueño del negocio vive en el teléfono. Misma auth que la web; tokens no en texto plano inseguro.

## Día 1 (2–3 h)
Scaffold Flutter o RN. Pantalla login contra tu API. Si 401, mensaje claro.

## Stack
Flutter (ya lo tocaste) **o** React Native — elige uno.

## Temario
Auth → listas → detalle cita → pulido offline/caché ligero → build.

## Lecturas

Canon: docs oficiales Flutter **o** React Native (el stack que elegiste). Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura (docs oficiales) | Enfoque |
|--------|--------------------------|---------|
| 1 | Auth / secure storage de sesión | Login contra tu API |
| 2 | Listas / networking | Lista de citas |
| 3 | Navegación + detalle | Detalle de cita |
| 4 | Caché / offline ligero (docs del framework) | Estados vacío/error |
| 5 | Build release (APK o equivalente) | Instalable en dispositivo real |

**Regla:** misma auth que la web; nada de secretos de API en el binario.

## Errores comunes
App desconectada del backend real; guardar secretos en el binario.

## Criterios de dominio
- [ ] Misma sesión/auth que la web.
- [ ] Build instalable en un dispositivo real.
