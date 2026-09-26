# Roles y least privilege (P3 / L19)

## Roles

| Rol | Uso | Privilegios |
|-----|-----|-------------|
| `agenda` (owner compose) | Migraciones / admin local | Alto (solo máquina de desarrollo) |
| `agenda_app` | Runtime de la app (futuro M17) | `CONNECT` + `SELECT/INSERT/UPDATE` en tablas de negocio |

## Cómo demostrar

1. Conectar como `agenda_app`.
2. `SELECT` / `INSERT` en `citas` → OK.
3. `DROP TABLE citas` o `CREATE TABLE x()` → **debe fallar**.
4. Pegar aquí el error (sin password):

```
(pegar)
```

## Checklist

- [ ] Password de app solo en `.env` (ignorado).
- [ ] Migraciones no se corren con el rol de la app.
- [ ] No hay usuario superuser en strings de conexión de aplicación.
