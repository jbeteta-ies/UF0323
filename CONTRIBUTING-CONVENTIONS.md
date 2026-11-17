# Convenciones de directorios y nombres de archivo

Documento de referencia breve para mantener una estructura homogénea y revisable en el proyecto.

## Alcance

- Este documento aplica a contribuciones editoriales y técnicas del repositorio.
- No forma parte de la navegación del alumnado en `docs/`.
- La fuente de verdad editorial es `EDITORIAL-GUIDE.md`.

## Estructura de directorios

- `docs/`: contenido formativo visible en Zensical.
- `docs/sesiones/`: sesiones formativas.
- `docs/guiones/`: guiones de trabajo.
- `docs/actividades/`: actividades de aprendizaje.
- `docs/evaluacion/`: criterios e instrumentos de evaluación.
- `docs/recursos/`: materiales y enlaces de apoyo.
- `docs/index.md`, `docs/README.md` y `docs/mapa-del-curso.md`: páginas raíz de
  orientación y mapa del curso.
- `.opencode/`: automatización, agentes y contratos internos (no contenido docente).
- `site/`: salida generada de build (artefacto, no fuente editorial).

## Convenciones de nombres de archivo

- Formato general: minúsculas con guiones (`kebab-case`).
- Sin espacios, tildes ni caracteres especiales en nombres de archivo.
- Páginas índice por sección: `index.md`.
- Bloques secuenciales de contenido: prefijo numérico de dos dígitos.
  - Ejemplo: `01-recursos-y-componentes.md`.
- Mantener coherencia entre nombre de archivo, título visible y navegación en `zensical.toml`.

## Reglas de mantenimiento

- Separar contenido para alumnado (`docs/`) de documentación interna del proyecto (raíz y `.opencode/`).
- Al crear o renombrar páginas en `docs/`, actualizar la navegación en `zensical.toml`.
- Evitar referencias de flujo interno (issues, PR, automatización) en páginas dirigidas al alumnado.

## Convenciones editoriales aplicables a `docs/`

- Antes de editar materiales docentes, revisar `EDITORIAL-GUIDE.md`.
- Mantener temas autosuficientes y con explicación textual suficiente.
- Acompañar Mermaid, tablas, tabs, código y comandos con contexto didáctico.
- Para ejercicios con solución, usar el patrón canónico:

```md
!!! question "Ejercicio N. Título del ejercicio"

    Enunciado del ejercicio.

    ??? success "Solución ejercicio N"

        Desarrollo razonado de la solución.
```

## Validación

- Validador editorial estructural: `./.venv/bin/python scripts/validate_editorial.py`
- Validador canónico del harness: `./.venv/bin/python scripts/validate_zensical_nav.py`
