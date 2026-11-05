import { z } from 'zod';

/** Opción de quiz (opción múltiple / verdadero-falso). */
export const QuizOpcionSchema = z.object({
  id: z.string().min(1),
  texto: z.string().min(1),
});

const PasoBase = {
  id: z.string().min(1),
  titulo: z.string().min(1),
  xp: z.number().int().positive().default(10),
};

export const PasoExplicacionSchema = z.object({
  ...PasoBase,
  tipo: z.literal('explicacion'),
  cuerpo: z.string().min(1),
});

export const PasoEjemploSchema = z.object({
  ...PasoBase,
  tipo: z.literal('ejemplo'),
  cuerpo: z.string().min(1),
  caption: z.string().optional(),
});

export const PasoQuizSchema = z.object({
  ...PasoBase,
  tipo: z.literal('quiz'),
  variante: z.enum(['opcion_multiple', 'verdadero_falso', 'completar']),
  pregunta: z.string().min(1),
  opciones: z.array(QuizOpcionSchema).optional(),
  /** Id de opción, lista de ids, o texto esperado (completar). */
  respuesta: z.union([z.string().min(1), z.array(z.string().min(1)).min(1)]),
  explicacionError: z.string().min(1),
  explicacionOk: z.string().optional(),
  /** Comparación laxa para completar (minúsculas, trim). Default true. */
  normalizar: z.boolean().optional(),
});

export const PasoCodigoTestSchema = z.object({
  nombre: z.string().min(1),
  /** Expresión JS truthy evaluada tras el código del alumno (scope compartido). */
  assert: z.string().min(1),
});

export const PasoCodigoSchema = z.object({
  ...PasoBase,
  tipo: z.literal('codigo'),
  enunciado: z.string().min(1),
  language: z.enum(['javascript', 'typescript']).default('javascript'),
  starter: z.string().optional(),
  tests: z.array(PasoCodigoTestSchema).min(1),
  explicacionError: z.string().optional(),
});

export const PasoTerminalSchema = z.object({
  ...PasoBase,
  tipo: z.literal('terminal'),
  enunciado: z.string().min(1),
  /** Comando(s) aceptados tras normalizar espacios. */
  comandoEsperado: z.union([z.string().min(1), z.array(z.string().min(1)).min(1)]),
  pistas: z.array(z.string()).optional(),
  explicacionError: z.string().min(1),
});

export const PasoProyectoSchema = z.object({
  ...PasoBase,
  tipo: z.literal('proyecto'),
  enunciado: z.string().min(1),
  entregables: z.array(z.string().min(1)).min(1),
  rubrica: z
    .array(
      z.object({
        id: z.string().min(1),
        criterio: z.string().min(1),
      }),
    )
    .min(1),
});

export const PasoResumenSchema = z.object({
  ...PasoBase,
  tipo: z.literal('resumen'),
  puntos: z.array(z.string().min(1)).min(1),
  siguiente: z.string().optional(),
});

export const PasoSchema = z.discriminatedUnion('tipo', [
  PasoExplicacionSchema,
  PasoEjemploSchema,
  PasoQuizSchema,
  PasoCodigoSchema,
  PasoTerminalSchema,
  PasoProyectoSchema,
  PasoResumenSchema,
]);

export const LeccionPasosMetaSchema = z.object({
  id: z.string().min(1),
  materia: z.string().min(1),
  orden: z.number().int().positive(),
  titulo: z.string().min(1),
  horas: z.number().nonnegative(),
  semana: z.number().int().nonnegative(),
  lectura: z.string().optional().default(''),
  evidencia: z.string().optional().default(''),
  formato: z.literal('pasos'),
  xpLeccion: z.number().int().positive().optional(),
  pasos: z.array(PasoSchema).min(5).max(8),
});

/** Frontmatter legacy (sin formato: pasos). */
export const LeccionLegacyMetaSchema = z.object({
  id: z.string().min(1),
  materia: z.string().optional(),
  orden: z.number().int().positive(),
  titulo: z.string().min(1),
  horas: z.number().nonnegative().optional().default(0),
  semana: z.number().int().nonnegative().optional().default(0),
  lectura: z.string().optional().default(''),
  evidencia: z.string().optional().default(''),
  formato: z.literal('pasos').optional(),
});

export type Paso = z.infer<typeof PasoSchema>;
export type PasoExplicacion = z.infer<typeof PasoExplicacionSchema>;
export type PasoEjemplo = z.infer<typeof PasoEjemploSchema>;
export type PasoQuiz = z.infer<typeof PasoQuizSchema>;
export type PasoCodigo = z.infer<typeof PasoCodigoSchema>;
export type PasoTerminal = z.infer<typeof PasoTerminalSchema>;
export type PasoProyecto = z.infer<typeof PasoProyectoSchema>;
export type PasoResumen = z.infer<typeof PasoResumenSchema>;
export type LeccionPasosMeta = z.infer<typeof LeccionPasosMetaSchema>;

export function isPasosFrontmatter(data: unknown): data is LeccionPasosMeta {
  return (
    typeof data === 'object' &&
    data !== null &&
    (data as { formato?: string }).formato === 'pasos'
  );
}

export function parseLeccionPasos(data: unknown): LeccionPasosMeta {
  return LeccionPasosMetaSchema.parse(data);
}

/** Normaliza un comando de terminal para comparar. */
export function normalizeCommand(raw: string): string {
  return raw
    .trim()
    .replace(/\s+/g, ' ')
    .replace(/['"]/g, '')
    .toLowerCase();
}

/** Normaliza respuesta de completar. */
export function normalizeFill(raw: string): string {
  return raw.trim().replace(/\s+/g, ' ').toLowerCase();
}

export function commandMatches(input: string, expected: string | string[]): boolean {
  const got = normalizeCommand(input);
  const list = Array.isArray(expected) ? expected : [expected];
  return list.some((e) => normalizeCommand(e) === got);
}

export function fillMatches(
  input: string,
  expected: string | string[],
  normalizar = true,
): boolean {
  const list = Array.isArray(expected) ? expected : [expected];
  if (normalizar) {
    const got = normalizeFill(input);
    return list.some((e) => normalizeFill(e) === got);
  }
  return list.some((e) => e === input.trim());
}
