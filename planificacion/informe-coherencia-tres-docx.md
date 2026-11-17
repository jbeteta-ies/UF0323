# Informe de coherencia de los tres DOCX

## 1. Alcance y método

Este informe corresponde a la issue **#126**. Compara, únicamente en lectura, los
tres DOCX de `planificacion/` con la planificación aprobada disponible en
el alcance de la issue. No completa ni corrige los DOCX.

La extracción se realizó sobre `word/document.xml` dentro de cada paquete DOCX,
conservando el texto visible, los literales de plantilla y los valores vacíos o
`00/00/00`. La trazabilidad de cada afirmación se mantiene mediante el nombre
del archivo y el literal extraído; cuando un campo no aparece cumplimentado se
indica **No consta**. La integridad de los tres paquetes se comprobó además con
`unzip -t`.

### Documentos comparados

| Abreviatura | Archivo | Literal identificativo extraído |
|---|---|---|
| PG | `planificaci-n-general-del-curso-completo.docx` | `PLANIFICACIÓN GENERAL DEL CURSO COMPLETO` |
| PE | `planificaci-n-de-la-evaluaci-n-del-aprendizaje--mod-presencial- (1).docx` | `PLANIFICACIÓN DE LA EVALUACIÓN DEL APRENDIZAJE (MODALIDAD PRESENCIAL)` |
| PD | `programaci-n-did-ctica--mod-presencial-.docx` | `MODELO DE PROGRAMACIÓN DIDÁCTICA (MODALIDAD PRESENCIAL)` |

## 2. Tabla mínima de extracción documental

Los valores siguientes son los que realmente aparecen en los DOCX, no valores
reconstruidos desde la planificación. «No consta» significa que el campo está
vacío, conserva solo un marcador o no ofrece un valor efectivo.

| Aspecto | PG: valor extraído | PE: valor extraído | PD: valor extraído |
|---|---|---|---|
| Solicitud | `L1SFC25/00037` | `L1SFC25/00037` | `L1SFC25/00037` |
| Acción/unidad | `UF0323` | `UF0323` | `UF0323` (también en `CÓDIGO`) |
| Certificado | `ADGG0208 / Actividades administrativas en la relación con el cliente` | El mismo literal | El mismo literal |
| Modalidad | `PRESENCIAL` | `PRESENCIAL` | `PRESENCIAL` |
| Duración | `30` horas | `30` horas | `30` horas |
| Fechas de impartición | `18/11/2026 – 27/11/2026` | `18/11/2026 – 27/11/2026` | `18/11/2026 – 27/11/2026` |
| Centro y dirección | `ACADEMIA BETA`; `TIRANT LO BLANC Nº 26`; Torrent; Valencia | Los mismos valores | Los mismos valores |
| Denominación de módulo | `No consta` como denominación efectiva; aparecen filas `UF0323` y `(Código y denominación del módulo profesional)` | `No consta` como denominación efectiva; aparece `UF0323` y después el marcador `(Código y denominación...)` | `No consta` como denominación efectiva; aparece `UF0323` y el campo `DENOMINACIÓN DEL MÓDULO` |
| Módulo consignado | `No consta` como `UF0323` en el texto extraído de PG | `No consta` como `UF0323` en el texto extraído de PE | `No consta` como `UF0323` en el texto extraído de PD |
| Jornada y horario | `Jornada: Tarde`; `De 16:30 horas a 20:30 horas` | No consta | No consta |
| Unidades/bloques/contenidos | Solo `UF0323`; no constan bloques ni contenidos | Solo `UF0323`; no constan bloques ni contenidos | Plantilla: `Contenidos`; no constan contenidos efectivos |
| Evaluación | `27/11/2026 (examen tipo test; 15/20 preguntas pendientes)` | `Examen final tipo test ... 15/20 preguntas, pendiente`; duración final `2 h`; fecha `27/11/2026` | No consta un instrumento o fecha de evaluación efectiva |
| Actividades e instrumentos | No consta | Marcadores `E1` y `E2`, pero sin denominación, espacio ni duración; fecha `00/00/00` | Plantilla `Estrategias metodológicas, actividades de aprendizaje y recursos didácticos`; No consta desarrollo |
| Espacios | No consta | No consta | Plantilla `Espacios, instalaciones y equipamiento`; No consta desarrollo |
| Referencias normativas | No consta | No consta | No consta; solo aparecen marcadores `R1`, `R2`, `CE 1.1` y `CE 1.2` |
| Campos vacíos, `00/00/00` o marcadores | Modalidad virtual, tutorías, plataforma, estancia y otros módulos: `Pendiente`, `Pendiente – Pendiente` o No consta | Actividades, espacios, duraciones y convocatorias: vacíos; `00/00/00`; marcador de módulo y prueba | Objetivos, resultados, criterios, contenidos, metodología, recursos y espacios: vacíos; `R1`, `R2`, `CE 1.1`, `CE 1.2` |

La extracción no confirma `UF0323` en el texto visible de estos tres paquetes.
La ficha administrativa de planificación lo registra como dato consignado en
los DOCX; por tanto, la discrepancia se conserva como incidencia documental que
requiere comprobación del origen o de la capa no visible, y no se transforma en
un dato extraído en esta tabla.

## 3. Comparación por categorías

### 3.1 Coincidencia

Los tres DOCX coinciden en los datos administrativos visibles: solicitud,
`UF0323`, certificado `ADGG0208`, modalidad presencial, 30 horas, periodo
18/11/2026–27/11/2026, centro Academia Beta y dirección de Torrent/Valencia.
PG añade la jornada de tarde y el horario 16:30–20:30; su ausencia en PE y PD
es una diferencia de cobertura, no una contradicción.

La duración total también coincide con la decisión de planificación: **30 h**.
La distribución aprobada queda documentada fuera de estos DOCX como `3 + 4 +
10 + 4 + 3 + 6 = 30 h`; los DOCX no contienen ese reparto por bloques.

### 3.2 Discrepancia real

- La planificación aprobada identifica la unidad como **UF0323, Aplicaciones
  informáticas para presentaciones: gráficas de información**. Los DOCX no
  ofrecen una denominación efectiva completa del módulo: usan `UF0323` y
  marcadores de plantilla.
- La planificación mantiene abierta la adscripción `MF0233_2` / `UF0323`.
  Los documentos de planificación registran `UF0323`, «Instalación y
  configuración de aplicaciones informáticas», como dato consignado, mientras
  que la procedencia normativa relaciona UF0323 con `MF0233_2`, «Ofimática».
  Este informe **no resuelve** la discrepancia ni la convierte en corrección de
  ningún DOCX.
- No hay en los DOCX contenido efectivo que permita comprobar la cobertura de
  los ocho contenidos oficiales, C1/C2 o sus criterios. La plantilla de PD no
  equivale a cobertura curricular.

### 3.3 Ausencia o diferencia de cobertura

| Elemento que debe contrastarse | Resultado en los tres DOCX |
|---|---|
| Denominación curricular completa de UF0323 | Ausente como denominación efectiva |
| Ocho contenidos y seis bloques B1–B6 | Ausentes |
| C1/C2 y criterios curriculares desarrollados | Ausentes; PD conserva marcadores distintos (`CE 1.1`, `CE 1.2`) |
| Reparto horario por bloques | Ausente |
| Actividades e instrumentos cumplimentados | Ausentes; PE solo deja `E1` y `E2` |
| Dos convocatorias de la prueba final | No constan sus fechas; PE conserva la nota de que deben ser dos fechas diferentes |
| Espacios, metodología, recursos y equipamiento | Ausentes o en plantilla |
| Modalidad virtual, tutorías y pruebas presenciales | Pendientes, vacíos o `No consta` |
| Estancia en empresa u organismo equiparado | No resuelta; PG conserva casillas y fechas pendientes |

### 3.4 Pendiente por diseño

- El examen final será **tipo test el último día, 27/11/2026**, con duración
  final de **2 h** según la confirmación de planificación.
- El número definitivo de preguntas, **15 o 20**, y las preguntas del examen
  quedan pendientes de preparación posterior. No se debe presentar esa elección
  como un valor ya decidido.
- El reparto diario confirmado es de **siete días de 4 h y el último día 2 h**:
  `7 × 4 + 2 = 30 h`. Este reparto no aparece desarrollado en los DOCX.
- La cumplimentación de actividades, instrumentos, espacios, fechas,
  metodología, contenidos y campos pedagógicos se reserva a una fase posterior.

### 3.5 Decisión externa

La verificación formal de la adscripción administrativa del módulo y cualquier
decisión que obligue a escoger entre `UF0323` y `MF0233_2` quedan fuera de este
informe. La decisión operativa del proyecto es conservar **UF0323** como acción
documentada y no alterar los DOCX hasta que exista autorización y resolución
competente.

## 4. Correcciones necesarias, sin ejecutarlas

Estas acciones son necesarias para alcanzar una documentación completa, pero no
se ejecutan en esta issue:

1. Confirmar externamente la identificación del módulo y trasladar, solo tras la
   decisión autorizada, la denominación coherente a los documentos afectados.
2. Completar la denominación curricular, objetivos, resultados, capacidades,
   criterios, contenidos, metodología, recursos y espacios de PD.
3. Cumplimentar en PE las actividades e instrumentos `E1`/`E2`, espacios,
   duraciones, fechas y las dos convocatorias de la prueba final.
4. Completar en PG el calendario de evaluación, modalidad virtual, tutorías,
   pruebas presenciales y la situación de la estancia en empresa, si procede.
5. Preparar y fijar posteriormente si el test tendrá 15 o 20 preguntas.
6. Revisar que el calendario administrativo y el reparto `7 × 4 h + 2 h`
   queden reflejados sin alterar la duración de 30 horas.

No se ha modificado ningún DOCX ni ningún Markdown existente.

## 5. Dictamen

La coherencia administrativa básica es **parcial**: los tres documentos
coinciden en acción, certificado, modalidad, duración, fechas y centro, y PG
aporta el horario. La coherencia de calendario y reparto del proyecto está
definida externamente como 30 horas, con examen el último día, pero no está
desarrollada de forma uniforme en los DOCX.

La coherencia curricular, pedagógica y evaluativa **no puede considerarse
completa**: faltan denominación curricular efectiva, bloques y contenidos,
desarrollo de capacidades y criterios, actividades, instrumentos, espacios y
campos administrativos. Además, permanece sin resolver la discrepancia
`UF0323`/`MF0233_2` y queda pendiente la elección entre 15 y 20 preguntas.

**Dictamen final: no hay coherencia completa de los tres DOCX.** Existe
coincidencia parcial de identificación y duración, con cobertura documental
insuficiente y correcciones pendientes que requieren diseño posterior y, para
la adscripción del módulo, decisión externa.

## 6. Validaciones realizadas

- `unzip -t` ejecutado sobre los tres DOCX: paquetes válidos.
- El nuevo archivo Markdown es el único archivo creado en esta issue.
- Se revisó la extracción trazable de `word/document.xml` y los literales de
  plantilla, vacíos y `00/00/00`.
- Se realizó comprobación de diff para detectar cambios fuera del nuevo informe.
- `git status` se comprobó para verificar que solo figura este archivo nuevo.

### Limitaciones

La comparación se limita al `READ_SCOPE` aprobado y a la extracción textual
visible de los tres DOCX. No se han inspeccionado fuentes fuera de ese alcance,
no se ha reabierto normativa, no se ha validado el renderizado de los DOCX y no
se ha resuelto ninguna decisión administrativa o externa.
