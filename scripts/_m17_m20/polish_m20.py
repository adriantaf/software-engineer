"""Build polished M20 BODIES + hecho/errores overrides (M09 depth)."""
from __future__ import annotations

from . import m20_lessons
from ._gen_m20_steps import STEPS
from .polish_common import build_body, default_commit

PROJ = "projects/m20-movil"

HECHO: dict[int, list[str]] = {
    1: [
        f"Existen `{PROJ}/stack-movil.md` y `{PROJ}/repo-url.md`",
        "Scaffold corre en emulador/dispositivo; README enlaza el código",
    ],
    2: [
        f"Login UI contra API documentada en `{PROJ}/demo-login-lista.md`",
        "Errores de red/credenciales visibles",
    ],
    3: [
        f"`{PROJ}/auth-storage.md` + implementación Keychain/Keystore (no texto claro)",
    ],
    4: [
        "401 limpia storage y vuelve a Login; nota en auth-storage.md",
    ],
    5: [
        f"`{PROJ}/demo-login-lista.md` registra lista de citas contra API real (P1)",
    ],
    6: [
        "Pull-to-refresh funciona; paginación o `limit` documentada",
    ],
    7: [
        "Estados loading/error documentados en demo-login-lista.md",
    ],
    8: [
        "Nota RBAC: UI puede ocultar; 403 de API verificado (staff vs owner)",
    ],
    9: [
        "Pantalla detalle de cita navegable desde la lista",
    ],
    10: [
        "Tabs o drawer mínimo con ≥2 destinos",
    ],
    11: [
        "Acciones cancelar/atendida llaman API; 403 manejado",
    ],
    12: [
        f"Existe `{PROJ}/deep-link.md` con scheme y comando de prueba",
    ],
    13: [
        "Empty state con copy útil documentado en demo-login-lista.md",
    ],
    14: [
        "Banner offline + reintento demostrado (modo avión)",
    ],
    15: [
        "Timeouts/5xx muestran mensajes humanos (sin stack traces)",
    ],
    16: [
        f"Existe `{PROJ}/logging-policy.md`; sin logs de tokens/PII en código revisado",
    ],
    17: [
        f"`{PROJ}/build-evidence.md` prep + keystore en `.gitignore`",
    ],
    18: [
        f"`{PROJ}/build-evidence.md` con artefacto release e instalación",
    ],
    19: [
        f"Existe `{PROJ}/release-notes.md` con demo cruzada web↔app",
    ],
    20: [
        f"`{PROJ}/README.md` índice enlaza stack, auth-storage, demo, build, logging, release",
    ],
}

ERRORES: dict[int, list[str]] = {
    1: ["Cambiar Flutter↔RN en semana 3 sin ADR", "Scaffold sin versión de SDK"],
    2: ["Mock eterno que nunca pega a staging", "Hardcodear secrets de prod"],
    3: ["Token en SharedPreferences/AsyncStorage en claro", "Loguear el token"],
    4: ["401 deja la sesión zombie", "Mensajes de error opacos (‘Error’)"],
    5: ["Lista desde JSON local fingiendo API", "Sin auth header/cookie"],
    6: ["Refresh que no vuelve a pedir red", "Paginación infinita sin fin"],
    7: ["Error silencioso (lista vacía falsa)", "Loading eterno"],
    8: ["Ocultar botón y creer que es seguridad", "Ignorar 403 de la API"],
    9: ["Detalle sin id real (solo mock)", "PII extra en la pantalla"],
    10: ["Nav sin destino Cuenta/Logout", "Tres navegadores distintos"],
    11: ["Cambiar estado solo en memoria local", "No manejar 403"],
    12: ["Deep link sin documentación de prueba", "Abrir http genérico sin ruta"],
    13: ["Vacío = pantalla blanca", "Copy técnico (‘array length 0’)"],
    14: ["Crash sin red", "Sin botón reintentar"],
    15: ["Mostrar stack trace al usuario", "Timeout infinito"],
    16: ["`console.log` del Bearer token", "Telemetría con teléfono completo"],
    17: ["Commitear `.jks` / `key.properties`", "Password del keystore en el README"],
    18: ["Solo debug APK como ‘release’", "Artefacto no instalado en dispositivo"],
    19: ["Release notes genéricas sin Agenda Ops", "Demo web y app con datos distintos sin notarlo"],
    20: ["README sin enlaces a evidencias", "Código móvil sin URL/ruta"],
}


def build_bodies() -> dict[int, str]:
    bodies: dict[int, str] = {}
    for i, raw in enumerate(m20_lessons.RAW, 1):
        bodies[i] = build_body(
            orden=i,
            titulo=raw["titulo"],
            horas=float(raw.get("horas", 5)),
            semana=int(raw["semana"]),
            porque=raw["porque"],
            objetivo=raw["objetivo"],
            steps=STEPS[i],
            commit_msg=default_commit("M20", i, raw["titulo"]),
            conceptos=raw.get("conceptos"),
        )
    return bodies


def patched_raw() -> list[dict]:
    out = []
    for i, raw in enumerate(m20_lessons.RAW, 1):
        r = dict(raw)
        r["hecho"] = HECHO[i]
        r["errores"] = ERRORES[i]
        out.append(r)
    return out
