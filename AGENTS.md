# Project Agent Instructions

Project:
UF0323 documentation project.

Main objective:
Create professional training documentation using Zensical.

Rules:

- Follow issue-driven workflow.
- Never modify files without an approved plan.
- Require human approval after planning and before merging pull requests.
- Never commit before validation.
- Use branches and pull requests.
- Keep documentation in Markdown.
- Keep student-facing content accessible from Zensical.
- Keep agent responsibilities separated.
- Keep automation and student documentation separated.

## Política de exploración de archivos

- El `READ_SCOPE` aprobado para el agente es el límite operativo de los
  archivos que puede explorar y leer durante la tarea.
- El agente solo puede ampliar ese alcance cuando el plan enumera
  explícitamente archivos adicionales; no debe asumir que todo el repositorio
  forma parte del alcance.
- Las búsquedas, lecturas y comprobaciones del agente deben permanecer dentro
  del `READ_SCOPE` y no deben incorporar de forma implícita archivos ignorados,
  generados o ajenos a la tarea.
- El `READ_SCOPE` del agente no equivale al alcance funcional del validador:
  son límites distintos y deben documentarse por separado.
- El validador puede necesitar un alcance funcional más amplio para comprobar
  el comportamiento del cambio, pero esa necesidad no autoriza al agente a
  explorar o modificar esos archivos fuera de su `READ_SCOPE`.
- Si la implementación o la validación exige acceder a un archivo fuera del
  alcance aprobado, el agente debe detenerse y comunicarlo en lugar de
  ampliar el alcance por inferencia.

## Fuente de verdad editorial

La guía editorial del proyecto está en:

`EDITORIAL-GUIDE.md`

Reglas para agentes en contenido docente (`docs/`):

- Consultar la guía editorial antes de crear o modificar materiales.
- Respetar el patrón canónico de ejercicios y soluciones definido en la guía.
- No inventar patrones editoriales alternativos sin decisión explícita del
  proyecto.
- Mantener temas autosuficientes, con explicación textual suficiente.
- Acompañar Mermaid, tablas, tabs, código y comandos con contexto didáctico.

## Fuente de verdad pedagógica y de alcance

Para el desarrollo de contenidos docentes, `planificacion/` es la
fuente de verdad operativa para el alcance, la secuenciación, la distribución
horaria y las decisiones pedagógicas ya aprobadas.

Los agentes deben consultar primero los artefactos de `planificacion/`
y no deben reabrir, reinterpretar ni volver a decidir cuestiones ya resueltas
en ellos.

La normativa oficial continúa siendo la fuente legal primaria, pero no debe
reanalizarse cuando la decisión curricular correspondiente ya esté
documentada en los artefactos de planificación.

Si un artefacto de planificación presenta una contradicción, laguna o duda
respecto a la normativa, debe señalarse explícitamente y consultarse la fuente
normativa correspondiente antes de continuar.

## Consulta de normativa

La carpeta `normativa/` contiene las fuentes legales utilizadas por el proyecto.

### Formatos disponibles

Para una misma disposición normativa pueden existir dos representaciones:

- `.pdf` → fuente oficial original y verificable.
- `.txt` → copia operativa de trabajo generada a partir del PDF para facilitar la lectura y el análisis por los agentes.

### Regla de consulta

Cuando exista una versión `.txt` equivalente a un PDF, los agentes deben consultar **preferentemente el archivo `.txt`**.

Ejemplo:

```text
normativa/BOE-A-2011-9930.txt
```

debe utilizarse antes que:

```text
normativa/BOE-A-2011-9930.pdf
```

No debe cargarse un PDF normativo completo en contexto cuando exista una versión `.txt` equivalente.

### Uso del PDF

El PDF debe reservarse para:

- verificar una discrepancia con el TXT;
- comprobar maquetación o estructura visual;
- confirmar referencias de página;
- validar que la extracción textual no ha perdido información;
- resolver dudas de codificación o contenido.

### Trazabilidad

Las copias `.txt` conservan marcas de página con el formato:

```text
===== PÁGINA N =====
```

Estas marcas deben utilizarse para mantener trazabilidad con el PDF original.

### Fuente de verdad

El PDF sigue siendo la **fuente legal oficial**.

El TXT es únicamente una **representación operativa derivada** para facilitar el trabajo de los agentes y reducir el coste de contexto.

En caso de discrepancia entre ambos, prevalece siempre el PDF original.

### Fuente curricular primaria

Para cualquier decisión relativa al currículo del módulo UF0323, la fuente
curricular primaria corresponde a la disposición:

`BOE-A-2011-9930`

Para consulta ordinaria por los agentes debe utilizarse:

`normativa/BOE-A-2011-9930.txt`

El PDF oficial correspondiente:

`normativa/BOE-A-2011-9930.pdf`

queda reservado como fuente legal original para verificación, de acuerdo con
las reglas anteriores.

### Marco normativo general

Los demás documentos de `normativa/` pueden utilizarse para interpretar el
marco general de la Formación Profesional, pero no para reemplazar la
definición curricular anterior.

En particular, no deben utilizarse versiones posteriores de las disposiciones
normativas que redefinan UF0323 o MF0233_2 con otra denominación, duración,
capacidades o contenidos para alterar el currículo adoptado. Deben utilizarse
los TXT normativos propios y señalarse explícitamente las contradicciones.

### Reglas para los agentes

- No reconstruir normativa desde memoria.
- No utilizar blogs, academias, resúmenes o fuentes secundarias como autoridad
  curricular cuando exista una fuente oficial en `normativa/`.
- No modificar capacidades, criterios de evaluación, contenidos o duración
  establecidos por la fuente curricular primaria.
- Si se detecta una aparente contradicción entre documentos normativos, no
  resolverla por inferencia: señalarla explícitamente.
- Las decisiones pedagógicas pueden reorganizar o secuenciar el contenido,
  pero no alterar los requisitos curriculares que deben cubrirse.
