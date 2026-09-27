---
id: L05
materia: M06
orden: 5
titulo: Interfaces y contratos de dominio
horas: 5
semana: 2
lectura: "Handbook TS — Object Types, Interfaces; CC cap. 6"
evidencia: "Interfaces Repositorio/Servicio + segunda implementación fake para tests"
---

# L05 — Interfaces y contratos de dominio

**~5 h · Semana 2**

Las interfaces fijan **contratos**; las clases son reemplazables. Así pruebas y diseño ganan independencia.

## Objetivo

Definir interfaces de repositorio/servicio; implementar versión en memoria y fake/stub para tests de integración ligeros.

## Pasos

### 1. Lectura (60 min)

Handbook: interfaces vs type aliases (cuándo usar cada uno). CC cap. 6 (objetos y estructuras de datos).

### 2. Diseño de contratos (90 min)

Separa:

- `RepositorioLibros` (persistencia)
- `ServicioPrestamo` (casos de uso)

El servicio depende del repositorio por interfaz, no por clase concreta.

### 3. Implementación fake (90 min)

`RepositorioLibrosFake` con contador de llamadas (útil para tests).

### 4. Tests de servicio (60 min)

Mock/fake: verifica que `prestar` llama `guardar` o equivalente.

## Hecho cuando

1. Servicio desacoplado de implementación concreta.
2. ≥2 implementaciones de repositorio (memoria + fake).
3. Tests del servicio sin tocar disco/red.

## Errores comunes

- Interfaz con 20 métodos “por si acaso”.
- `implements` en cadena sin necesidad.

## Siguiente

[L06 — Composición frente a herencia](L06-composicion-frente-a-herencia.md)
