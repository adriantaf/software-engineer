/** Rúbricas de autoevaluación por etapa (checklist formativa). */

export type RubricaItem = {
  id: string;
  label: string;
};

export type EtapaRubrica = {
  titulo: string;
  criterio: string;
  items: RubricaItem[];
};

export const EXAMEN_RUBRICAS: Record<string, EtapaRubrica> = {
  basica: {
    titulo: 'Rúbrica — Etapa Básica',
    criterio:
      'Aprobado formativo si puedes cerrar «Construye» sin tutorial paso a paso. Si no, refuerza M01–M02.',
    items: [
      {
        id: 'b-repo',
        label: 'Repo nuevo con script TS strict (JSON → CSV) que corre en local',
      },
      {
        id: 'b-tests',
        label: '≥5 tests Vitest, incluido caso de archivo faltante',
      },
      {
        id: 'b-commits',
        label: '≥3 commits atómicos con mensajes qué/porqué',
      },
      {
        id: 'b-explica',
        label: 'Puedo explicar sync vs async, Set vs Array, RAM vs disco sin mirar ficha',
      },
      {
        id: 'b-diagnostica',
        label: 'Sé qué decir ante un commit “update stuff” con 20 archivos',
      },
    ],
  },
  disciplinaria: {
    titulo: 'Rúbrica — Etapa Disciplinaria',
    criterio:
      'Si no puedes cerrar el IDOR con test el mismo día, vuelve a M17–M18 antes de Terminal.',
    items: [
      {
        id: 'd-endpoint',
        label: 'Endpoint protegido nuevo + tests 401 e IDOR',
      },
      {
        id: 'd-migracion',
        label: 'Migración DB + plan de rollback escrito',
      },
      {
        id: 'd-owasp',
        label: 'Hallazgo OWASP reproducido en staging local y corregido con test',
      },
      {
        id: 'd-explica',
        label: 'Explico trust boundaries, límites de HTTPS y pirámide de tests de mi repo',
      },
      {
        id: 'd-idor',
        label: 'Diagnóstico + fix claro para GET /api/citas/7 cross-user',
      },
    ],
  },
  terminal: {
    titulo: 'Rúbrica — Etapa Terminal (pre-egreso)',
    criterio:
      'Cumples egreso.md. Si falla seguridad multi-tenant o restore de backup, no hay egreso.',
    items: [
      {
        id: 't-nucleo',
        label: 'Núcleo SaaS: auth + tenancy + deploy HTTPS + tests + backup/restore',
      },
      {
        id: 't-video',
        label: 'Video 10–15 min: arquitectura, multi-tenant, trade-offs, amenaza cross-tenant',
      },
      {
        id: 't-negocio',
        label: 'Resumen de ≥10 demos con aprendizaje de mercado (no vanity metrics)',
      },
      {
        id: 't-seguridad',
        label: 'Aislamiento tenant verificado (manual o test) sin secretos en el repo',
      },
      {
        id: 't-egreso',
        label: 'Checklist de egreso.md enlazada con evidencia en git',
      },
    ],
  },
};

export function getExamenRubrica(etapaId: string): EtapaRubrica | null {
  return EXAMEN_RUBRICAS[etapaId] ?? null;
}
