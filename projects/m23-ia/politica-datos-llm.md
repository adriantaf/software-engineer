# Política de datos LLM (borrador M23)

## Qué SÍ se puede enviar al proveedor

- Texto de FAQ / políticas del **tenant autenticado**
- Preguntas del gold set sin PII

## Qué NUNCA se envía

- Dumps de BD, `.env`, claves Stripe
- Nombres/teléfonos/emails de clientes reales
- Tokens de sesión

## Retención y logs

- Logs locales sin PII; rotación:
- Proveedor: región / retención (llenar tras L07):

## Dueño

Fecha:
