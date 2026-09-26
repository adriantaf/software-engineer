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

El dueño del negocio de servicios — tu ICP de [Agenda Ops](../../producto-saas.md) — no administra citas desde un escritorio todo el día. Vive en WhatsApp y en el teléfono. Una app móvil **cliente** (owner/staff) que habla con la **misma API** que la web demuestra que entiendes auth en cliente móvil, manejo de red inestable y distribución instalable, sin duplicar reglas de negocio en el dispositivo.

No es reemplazar la web admin completa en M17; es el canal móvil mínimo viable: login, lista de citas, detalle, estados claros.

**En resumen:** el dueño vive en el teléfono: misma auth que la web, sesión segura, build instalable.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Elegir **un** stack móvil (Flutter o React Native) y justificarlo en una nota corta.
2. Implementar login contra la API real de Agenda Ops (mismos endpoints que la web).
3. Persistir tokens o sesión con **secure storage** del framework, no en `SharedPreferences` en texto plano para secretos largos.
4. Mostrar lista y detalle de citas con estados de carga, vacío y error (incl. 401 → logout).
5. Manejar red lenta o caída sin crashear (timeouts, reintento razonable, mensajes al usuario).
6. Generar un build instalable (APK Android o equivalente) y probarlo en dispositivo físico.

## Cómo estudiar esta materia (lecciones)

M20 construye la app **cliente** de Agenda Ops contra la API de M17/M19: L01–L20, evidencia en `projects/m20-movil/`.

1. **Un** stack (Flutter **o** RN); no cambies a mitad.
2. API **staging HTTPS** de M19; no mocks eternos.
3. Cada pantalla: commit + captura o nota en `projects/m20-movil/`.
4. Secure storage para tokens; 401 → logout; sin secretos de servidor en el binario.
5. [Cómo estudiar](../../como-estudiar.md) y [producto-saas](../../producto-saas.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Auth / listas / detalle | 10–12 | 4× ~5 h lecciones |
| Estados y red | 4–6 | Vacío, offline, timeouts |
| Build instalable | 4–6 | APK/artefacto en dispositivo real |
| Retro | 1 | Política de logs y storage |

Si un día solo tienes 2 h: **una lección** con UI o build verificable.

## Lecciones

### Semana 1 — Scaffold, login y secure storage (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Stack móvil y scaffold Agenda Ops](M20/L01-stack-movil-y-scaffold-agenda-ops.md) | 5 |
| L02 | [Pantalla login contra API staging](M20/L02-pantalla-login-contra-api-staging.md) | 5 |
| L03 | [Secure storage de token o sesión](M20/L03-secure-storage-de-token-o-sesion.md) | 5 |
| L04 | [Errores de validación y flujo 401](M20/L04-errores-de-validacion-y-flujo-401.md) | 5 |

### Semana 2 — Lista de citas y roles (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Lista de citas autenticada](M20/L05-lista-de-citas-autenticada.md) | 5 |
| L06 | [Pull-to-refresh y paginación simple](M20/L06-pull-to-refresh-y-paginacion-simple.md) | 5 |
| L07 | [Estados de carga en lista](M20/L07-estados-de-carga-en-lista.md) | 5 |
| L08 | [Roles: confiar en la API, no solo en UI](M20/L08-roles-confiar-en-la-api-no-solo-en-ui.md) | 5 |

### Semana 3 — Detalle, navegación y acciones (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Pantalla detalle de cita](M20/L09-pantalla-detalle-de-cita.md) | 5 |
| L10 | [Navegación: tabs o drawer mínimo](M20/L10-navegacion-tabs-o-drawer-minimo.md) | 5 |
| L11 | [Acciones permitidas: cancelar / atendida](M20/L11-acciones-permitidas-cancelar-atendida.md) | 5 |
| L12 | [Deep link opcional a una cita](M20/L12-deep-link-opcional-a-una-cita.md) | 5 |

### Semana 4 — Vacío, error, red y logging (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Lista vacía con copy útil](M20/L13-lista-vacia-con-copy-util.md) | 5 |
| L14 | [Sin red: banner y reintento](M20/L14-sin-red-banner-y-reintento.md) | 5 |
| L15 | [Timeout, 5xx y mensajes humanos](M20/L15-timeout-5xx-y-mensajes-humanos.md) | 5 |
| L16 | [AppSec móvil: no loguear PII ni tokens](M20/L16-appsec-movil-no-loguear-pii-ni-tokens.md) | 5 |

### Semana 5 — Build release y entrega (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L17 | [Firma Android y keystore fuera del repo](M20/L17-firma-android-y-keystore-fuera-del-repo.md) | 5 |
| L18 | [Build release APK o artefacto](M20/L18-build-release-apk-o-artefacto.md) | 5 |
| L19 | [Release notes y demo cruzada con web](M20/L19-release-notes-y-demo-cruzada-con-web.md) | 5 |
| L20 | [Cierre M20 — dominio y README proyecto](M20/L20-cierre-m20-dominio-y-readme-proyecto.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: documentación oficial de **Flutter** o **React Native** (el stack elegido). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Docs oficiales | Enfoque |
|--------|-----------|----------------|---------|
| 1 | L01–L04 | Get started + HTTP + secure storage | Login staging, 401 |
| 2 | L05–L08 | Listas, refresh, async | P1 login+lista |
| 3 | L09–L12 | Navegación, detalle, deep links | Detalle cita |
| 4 | L13–L16 | Errores / conectividad / MASVS logging | P2 estados + storage |
| 5 | L17–L20 | Release build | P3 APK + demo web |

**Regla:** misma auth que la web; nada de secretos de API de servidor en el repositorio móvil.



## Ejemplo — 401 en cliente móvil

```dart
// Flutter (idea): interceptor o wrapper HTTP
if (response.statusCode == 401) {
  await secureStorage.delete(key: 'access_token');
  navigator.pushReplacementNamed('/login');
  return;
}
```

En web guardaste el JWT en cookie HttpOnly o memoria según M18; en móvil el equivalente es **Keychain/Keystore** vía `flutter_secure_storage` o el paquete oficial de RN. No copies el refresh token a logs.



## Prácticas

1. **P1 — Login + lista:** App contra API real; evidencia en `projects/m20-movil/demo-login-lista.md` (capturas o video corto + commit hash).
2. **P2 — Estados + storage:** `projects/m20-movil/auth-storage.md` + capturas de vacío/error/401; código de storage seguro referenciado.
3. **P3 — Build:** APK o artefacto en `projects/m20-movil/build-evidence.md` (comando usado, SHA, dispositivo probado).

## Proyecto útil

**App móvil Agenda Ops** enlazada en `projects/m20-movil/README.md`:

- Repo o submódulo con el código.
- Misma sesión que la web: login en web y comprobar que la app con las mismas credenciales ve las mismas citas (o explicar diferencia si usas roles distintos).
- Objetivo demo: dueño abre el teléfono y ve el día de citas en 10 segundos.

## Errores comunes

- App contra JSON mock que nunca se conecta al backend de M17/M19.
- Guardar JWT en almacenamiento sin cifrar “porque es más fácil”.
- Hardcodear `localhost` en build de release.
- Pantalla de carga infinita sin timeout.
- Reimplementar reglas de negocio en el móvil en vez de confiar en la API (doble fuente de verdad).

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Login+lista:** `projects/m20-movil/demo-login-lista.md` + commits en repo app.
- **P2 — Estados:** `projects/m20-movil/auth-storage.md` + evidencia UI vacío/error.
- **P3 — Build:** `projects/m20-movil/build-evidence.md` con artefacto instalado en dispositivo real.
- **Proyecto — App CRM:** `projects/m20-movil/README.md` con enlace al código y nota de paridad auth con web.

## Criterios de dominio

- [ ] Misma sesión/auth que la web en demo reproducible.
- [ ] Build instalable en un dispositivo real (no solo emulador).
- [ ] Explicas dónde guardas el token y qué pasa en 401.
- [ ] Lista y detalle reflejan la API; sin datos inventados en el cliente.
- [ ] No hay secretos de servidor en el repositorio móvil.
