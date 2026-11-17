# UF0323 · Aplicaciones informáticas para presentaciones

Repositorio autónomo de la documentación de **UF0323: Aplicaciones
informáticas para presentaciones: gráficas de información**, publicado con
Zensical.

## Estructura

- `docs/`: contenido visible para el alumnado.
- `planificacion/`: planificación Markdown de la unidad.
- `normativa/`: copias operativas y fuentes normativas propias de UF0323.
- `scripts/`: validadores y pruebas del sitio.
- `zensical.toml`: configuración y navegación.

Las sesiones 1–4 están disponibles. Las sesiones 5–7, evaluación y recursos
disponen únicamente de marcadores pendientes; no se inventa contenido.

## Desarrollo y validación

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python scripts/validate_zensical_nav.py
./.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'
./.venv/bin/zensical build --clean --strict
```

La salida `site/` es un artefacto generado y no debe editarse manualmente.
