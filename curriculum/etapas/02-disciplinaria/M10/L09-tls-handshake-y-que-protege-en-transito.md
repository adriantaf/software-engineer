---
id: L09
materia: M10
orden: 9
titulo: "TLS: handshake y qué protege en tránsito"
horas: 5
semana: 3
lectura: "Tanenbaum seguridad/TLS selecto + MDN TLS"
evidencia: "labs/tls-handshake.md"
---

# L09 — TLS: handshake y qué protege en tránsito

**~5 h · Semana 3**

## Objetivo

Describir las fases del handshake TLS 1.2/1.3 a alto nivel y listar amenazas que TLS mitiga vs las que no.

## Por qué importa

“Ya tiene HTTPS” no responde por XSS ni por logs con PII; hoy acotas el contrato de TLS.

## Conceptos

- Confidencialidad e integridad en tránsito.
- Certificado de servidor.
- Perfect Forward Secrecy (idea).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
curl -v https://example.com -o /dev/null 2>&1 | rg -i 'TLS|SSL|subject|issuer' || true
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

Tabla: amenaza → ¿TLS ayuda? (eavesdropping, tampering, phishing de dominio).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l09 tls-handshake-y-que-protege-en-transito"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Tanenbaum | TLS intro | MDN Transport Layer Security |

## Hecho cuando

1. Tabla amenaza/mitigación.
2. Salida openssl comentada.
3. Párrafo “qué no protege TLS”.

## Errores comunes

- Creer que TLS autentica al usuario.
- Mezclar TLS con hash de contraseña en DB.

## Siguiente

[L10 — Certificados X.509 y cadena de confianza](L10-certificados-x-509-y-cadena-de-confianza.md)
