# Rúbrica de egreso competente (titulación interna)

No es título oficial. Es la meta de dominio de esta academia. Debes cumplir **todas** las evidencias.

## Checklist

- [ ] **Sistema web en producción:** auth, base de datos, roles, tests, CI, deploy HTTPS, backups **con restore probado**.
- [ ] **SRS + diseño** (diagramas + trust boundaries) de un negocio real o simulado serio.
- [ ] **App móvil o desktop** conectada al mismo backend.
- [ ] **AppSec (M18):** threat model + ≥5 hallazgos OWASP corregidos con tests de regresión.
- [ ] **Ciberseguridad aplicada (M25):** security review + tabletop de incidente + hardening prod documentado.
- [ ] **Portfolio de estructuras de datos y algoritmos** (implementación propia + complejidad).
- [ ] **10 conversaciones comerciales** documentadas + al menos 1 piloto pagado o carta de intención.
- [ ] **Video o demo en vivo** explicando arquitectura, trade-offs y amenaza principal **sin tutorial**.
- [ ] **Inglés:** progreso documentado hacia B1 lectura técnica.

## Entregables del proyecto integrador (M26)

1. Repositorio público del producto.
2. Memoria técnica: problema, usuarios, arquitectura, decisiones, métricas, seguridad.
3. URL en producción + instructivo de despliegue + runbook.
4. Suite de tests (backend ≥70% en lógica de negocio) + tests anti-IDOR/XSS básicos.
5. Registro de demos/clientes en `projects/m22-bektor/` / `projects/m26-capstone/`.

## Criterio de “aprobado”

El mentor (o tú con honestidad brutal) solo marca egreso si puedes construir un CRUD con auth + deploy + tests **desde cero en un fin de semana** sin tutorial paso a paso, **y** explicas cómo evitarías el IDOR más obvio.
