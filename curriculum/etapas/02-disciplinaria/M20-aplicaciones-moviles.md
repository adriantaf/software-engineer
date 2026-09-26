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

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md). La API debe ser la de tu piloto/SaaS (staging de M19), no mocks eternos.
- **Un** framework: si ya tocaste Flutter en el plan, sigue con Flutter; si tu front web es React, RN puede acortar curva — no cambies a mitad de materia.
- Cada pantalla nueva: commit + captura o nota en `projects/m20-movil/`.
- No embebas API keys de proveedores LLM ni secretos de servidor en el binario; el móvil solo lleva token de **usuario** tras login.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Auth móvil | 6–8 | Login API + secure storage |
| Listas/detalle | 6–8 | Citas + navegación |
| Build | 4–6 | APK/IPA o equivalente |
| Retro | 1 | Dónde NO guardar secretos |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. `mkdir -p projects/m20-movil` y escribe `projects/m20-movil/stack.md`: Flutter **o** RN, versión SDK, URL base de API (staging).
2. Scaffold del proyecto (en subcarpeta `app/` o repo enlazado en `projects/m20-movil/repo-url.md`).
3. Pantalla de login: email/contraseña → `POST` login de tu API; si 401, mensaje claro (no stack trace).
4. Guarda token/sesión con el mecanismo seguro del framework (documenta en `projects/m20-movil/auth-storage.md`).
5. Prueba contra staging HTTPS de M19; anota CORS o certificados si algo falla.
6. Commit inicial con mensaje del estilo `feat(m20): scaffold app + login contra API`.

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

## Temario semanal

### Semana 1 — Scaffold y auth (~20 h)

- Estructura del proyecto, lint, variables de entorno de **build** (solo URL pública de API).
- Pantalla login/registro si tu API lo permite; flujo feliz y errores de validación.
- Secure storage: qué guardas (access token, refresh si aplica) y qué no (contraseña en claro).
- Prueba en emulador y dispositivo real (red local o staging).

### Semana 2 — Lista de citas (~20 h)

- `GET` citas autenticado; paginación simple si la API la tiene.
- UI: fecha, cliente, servicio, estado; pull-to-refresh.
- Respetar roles: staff no ve lo que la API niega (no confiar solo en ocultar UI).

### Semana 3 — Detalle y navegación (~20 h)

- Pantalla detalle de cita; acciones permitidas (cancelar, marcar atendida) solo si la API lo expone.
- Stack de navegación (tabs o drawer mínimo: Citas / Perfil / logout).
- Deep link opcional hacia una cita (preparación para recordatorios futuros).

### Semana 4 — Estados vacío, error y red (~20 h)

- Lista vacía: copy útil (“Aún no hay citas esta semana”).
- Sin red: banner o pantalla con reintento.
- Timeout y 5xx: mensaje humano + log interno en dev.
- Revisión AppSec móvil: no loguear PII ni tokens.

### Semana 5 — Build release y entrega (~20 h)

- Firma Android (keystore fuera del repo) o perfil iOS si aplica.
- Build release instalable; prueba en teléfono de alguien del ICP si puedes.
- Notas de versión en `projects/m20-movil/release-notes.md`.
- Alineación con [producto-saas](../../producto-saas.md): misma cuenta que en web en demo cruzada.

## Lecturas

Canon: documentación oficial de **Flutter** o **React Native** (el stack que elegiste). Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura (docs oficiales) | Enfoque |
|--------|--------------------------|---------|
| 1 | Auth / secure storage de sesión | Login contra tu API |
| 2 | HTTP client, listas, async | Lista de citas |
| 3 | Navegación + detalle | Detalle de cita |
| 4 | Manejo de errores / conectividad | Estados vacío/error |
| 5 | Build release (APK o equivalente) | Instalable en dispositivo real |

**Regla:** misma auth que la web; nada de secretos de API de servidor en el binario.

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
