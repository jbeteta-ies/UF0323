# Guía editorial del proyecto (fuente de verdad)

Esta guía define las convenciones editoriales y pedagógicas comunes del
repositorio para el material docente del módulo **UF0323**.

- Ámbito principal: contenido formativo en `docs/`.
- Ámbito secundario: revisión editorial de contribuciones internas que afecten
  a la documentación docente.

> Esta guía es la **fuente de verdad editorial** del proyecto. Si aparece una
> discrepancia con otros documentos de proceso, prevalece esta guía para estilo,
> estructura, desarrollo pedagógico y patrón de actividades.
>
> La normativa curricular y los documentos de planificación del proyecto
> continúan siendo las fuentes de verdad para alcance, capacidades, criterios de
> evaluación, contenidos y duración.

---

## 1. Principios generales

### 1.1 Material autosuficiente

Los temas deben poder estudiarse sin depender de una explicación oral adicional
del docente.

El material debe proporcionar el contexto, las explicaciones, los ejemplos y
las relaciones entre conceptos necesarios para que el alumnado pueda construir
una comprensión suficiente del contenido.

Autosuficiente no significa enciclopédico. Debe incluir lo necesario para
alcanzar los objetivos del módulo con el nivel de profundidad adecuado.

### 1.2 La explicación en prosa es la base

El texto explicativo es el elemento principal del material.

Diagramas, tablas, admonitions, tabs, bloques de código, comandos y otros
recursos sirven para apoyar la explicación, no para sustituirla.

No debe considerarse desarrollado un concepto únicamente porque aparezca:

- en una definición;
- en una lista de vocabulario;
- en una tabla;
- en un diagrama;
- en un ejemplo;
- o en un ejercicio.

Los conceptos relevantes deben explicarse y relacionarse dentro del desarrollo
del tema.

### 1.3 Desarrollo conceptual suficiente

Un tema no se considera desarrollado por presentar una colección de
definiciones, vocabulario y ejercicios.

Cuando corresponda, la explicación debe permitir comprender:

- qué es el concepto;
- para qué sirve;
- cómo funciona;
- con qué otros conceptos se relaciona;
- qué consecuencias tiene;
- cómo reconocerlo en una situación real;
- y cómo aplicarlo.

La profundidad dependerá de la importancia del concepto, del nivel del alumnado
y de su función dentro del módulo.

Se evitarán dos extremos:

- explicaciones excesivamente superficiales que conviertan conceptos
  importantes en unas pocas frases;
- desarrollos enciclopédicos que introduzcan detalle innecesario para los
  objetivos del módulo.

### 1.4 Progresión didáctica

Como criterio general, el desarrollo debe avanzar desde lo concreto y conocido
hacia lo abstracto o complejo.

Cuando resulte adecuado, se seguirá una progresión similar a:

**situación o problema → explicación conceptual → relaciones entre conceptos →
ejemplo → aplicación o práctica → comprobación del aprendizaje**

Esta secuencia no obliga a utilizar esos encabezados ni constituye una
plantilla rígida. Debe adaptarse al contenido.

El objetivo es evitar saltos conceptuales y asegurar que el alumnado dispone de
los conocimientos necesarios antes de realizar una actividad.

### 1.5 Recursos con intención pedagógica

Todo recurso editorial debe responder a una necesidad didáctica.

Antes de introducir un diagrama, tabla, tab, admonition, bloque de código u otro
recurso debe poder justificarse qué aporta respecto a una explicación lineal.

No se utilizarán recursos únicamente para hacer la página visualmente más
variada.

---

## 2. Contenido del alumnado y metadatos de planificación

### 2.1 Separación de responsabilidades

Debe distinguirse entre:

1. **contenido destinado al alumnado**, cuyo objetivo es enseñar;
2. **información de planificación y trazabilidad**, cuyo objetivo es garantizar
   coherencia curricular y permitir la revisión del proyecto.

La información de planificación no debe introducir ruido innecesario en la
lectura del alumnado.

### 2.2 Contenido destinado al alumnado

Las páginas docentes deben priorizar:

- explicación;
- ejemplos;
- diagramas cuando sean útiles;
- procedimientos;
- actividades;
- ejercicios;
- comprobaciones;
- y relaciones entre conceptos.

No es obligatorio mostrar al comienzo de cada página una ficha extensa con
prerrequisitos, progresión didáctica, evidencias, instrumentos, capacidades,
criterios y referencias normativas.

### 2.3 Información de planificación

La planificación del tema o unidad debe conservar, cuando corresponda:

- prerrequisitos;
- progresión didáctica;
- capacidades relacionadas;
- criterios de evaluación;
- bloques de contenidos;
- referencia normativa;
- evidencias de aprendizaje;
- instrumentos de evaluación.

Esta información puede mantenerse en documentos de planificación, páginas de
unidad, metadatos o mecanismos equivalentes definidos por el proyecto.

Debe ser verificable sin necesidad de convertirla en contenido principal para
el alumnado.

---

## 3. Trazabilidad curricular operativa

### 3.1 Fuente normativa primaria

La trazabilidad curricular del módulo UF0323 se fundamenta en la fuente
normativa primaria del proyecto:

- `normativa/BOE-A-2011-9930.pdf`

Esta guía no modifica ni sustituye capacidades, criterios de evaluación,
bloques de contenidos ni duración.

### 3.2 Trazabilidad obligatoria

Cuando un tema, práctica, actividad o secuencia tenga relación curricular con
el módulo UF0323, debe poder verificarse su relación con:

1. Capacidad (C).
2. Criterio de evaluación (CE).
3. Bloque de contenidos.
4. Referencia normativa exacta.

Formato mínimo:

- `Capacidad:` Cx
- `Criterio de evaluación:` CEx.y
- `Bloque de contenidos:` nombre del bloque
- `Referencia normativa:` `normativa/BOE-A-2011-9930.pdf`, p. NN y/o apartado
  identificable

Si un elemento cubre varias capacidades o criterios, deben indicarse todos de
forma clara.

No se utilizarán referencias genéricas como «según BOE» sin una referencia
rastreable.

La trazabilidad puede mantenerse fuera del flujo principal de lectura del
alumnado siempre que siga siendo verificable dentro del proyecto.

---

## 4. Organización y legibilidad

### 4.1 Estructura de las páginas

Los encabezados deben reflejar la estructura conceptual del contenido.

Se crearán subsecciones cuando exista un cambio real de idea o sea necesario
reducir la carga cognitiva.

Se evitará tanto:

- un único bloque de texto excesivamente largo;
- como una fragmentación artificial en muchas secciones de unas pocas líneas.

### 4.2 Párrafos y listas

La prosa debe utilizarse para explicar relaciones, causas, funcionamiento y
razonamiento.

Las listas se utilizarán cuando exista una enumeración real, una secuencia o
una comparación que gane claridad mediante ese formato.

No debe sustituirse sistemáticamente la explicación por listas de elementos.

### 4.3 Terminología

Los términos técnicos deben introducirse con contexto suficiente.

Cuando aparezca por primera vez un término que pueda ser desconocido para el
alumnado, debe explicarse antes de depender de él para comprender conceptos
posteriores.

Las abreviaturas y siglas deben desarrollarse cuando aparezcan por primera vez,
salvo que sean de conocimiento previo explícitamente asumido.

---

## 5. Ejemplos

Los ejemplos son un recurso de enseñanza y no deben confundirse con los
ejercicios.

Un ejemplo debe:

- ilustrar un concepto previamente introducido;
- mostrar su aplicación en una situación concreta;
- hacer explícita la relación entre el ejemplo y el concepto;
- evitar introducir complejidad irrelevante.

Cuando un concepto sea abstracto o pueda interpretarse de forma ambigua, debe
valorarse especialmente la inclusión de uno o varios ejemplos.

Después de mostrar cómo se aplica un concepto mediante un ejemplo puede
plantearse una actividad en la que el alumnado deba aplicarlo por sí mismo.

---

## 6. Mermaid y diagramas

### 6.1 Cuándo utilizar diagramas

Debe valorarse el uso de Mermaid cuando la comprensión dependa especialmente
de visualizar:

- relaciones entre componentes;
- arquitecturas;
- jerarquías;
- secuencias;
- procesos;
- flujos de información;
- dependencias;
- estados;
- decisiones.

Cuando una explicación presente varias entidades y comprender el contenido
dependa de entender cómo se relacionan, el autor debe valorar explícitamente si
un diagrama facilitaría la construcción del modelo mental del alumnado.

Esto no implica que todo contenido deba tener un diagrama.

### 6.2 Integración con la explicación

Todo diagrama debe:

- tener un propósito didáctico identificable;
- estar introducido o contextualizado mediante texto;
- ir acompañado de una lectura guiada cuando la interpretación no sea
  inmediata;
- estar conectado con la explicación del tema.

Un diagrama no sustituye la explicación conceptual.

### 6.3 Accesibilidad

- No codificar significado únicamente mediante color.
- Combinar color, cuando se utilice, con texto, etiquetas, formas o relaciones.
- Utilizar etiquetas comprensibles.
- Evitar abreviaturas no explicadas.
- Evitar diagramas innecesariamente complejos.

Si el diagrama resulta más difícil de interpretar que la explicación que
pretende simplificar, debe rediseñarse o eliminarse.

---

## 7. Tablas

Las tablas se utilizarán cuando permitan comparar o estructurar información de
forma más clara que la prosa.

Cada tabla debe:

- tener contexto;
- utilizar encabezados claros y específicos;
- permitir entender qué se está comparando;
- estar acompañada de explicación cuando la interpretación no sea inmediata.

No deben utilizarse tablas para introducir grandes bloques narrativos que se
comprenderían mejor mediante texto lineal.

---

## 8. Tabs

### 8.1 Uso didáctico

Los tabs se utilizarán para presentar **alternativas equivalentes** que permiten
alcanzar un mismo objetivo mediante procedimientos diferentes.

Casos habituales:

- Windows / GNU/Linux / macOS;
- PowerShell / Bash;
- interfaz gráfica / terminal, cuando ambas sean alternativas equivalentes;
- herramientas diferentes que producen un resultado comparable.

### 8.2 Evitar duplicación

La explicación común debe aparecer fuera de los tabs.

Dentro de cada tab debe incluirse principalmente aquello que cambia entre las
alternativas.

No debe repetirse en cada tab la misma explicación conceptual.

### 8.3 Restricciones

No utilizar tabs:

- por motivos meramente estéticos;
- para ocultar contenido esencial;
- para fragmentar artificialmente una explicación;
- cuando las opciones no sean realmente comparables.

Cada tab debe tener una etiqueta clara y permitir identificar qué alternativa
representa.

---

## 9. Admonitions

### 9.1 Principio general

Los admonitions se utilizarán para destacar información que tenga una función
pedagógica específica.

No se utilizarán como decoración ni para encerrar grandes cantidades de
contenido sin una razón clara.

### 9.2 Usos habituales

Según el contexto pueden utilizarse, entre otros:

- `note`: aclaración o información complementaria relevante;
- `tip`: recomendación práctica;
- `warning`: riesgo, precaución o error frecuente;
- `question`: ejercicio autocorregible según el patrón definido en esta guía;
- `success`: solución del ejercicio autocorregible.

Los tipos disponibles deben utilizarse de acuerdo con las capacidades
soportadas por Zensical y la configuración del proyecto.

### 9.3 Ejercicios y soluciones

`question` queda reservado para ejercicios autocorregibles con solución
publicada.

`success`, cuando forma parte de este patrón, contiene la solución razonada y
permanece colapsado inicialmente.

### 9.4 Requisito técnico

El patrón editorial de admonitions depende de que la configuración de Zensical
tenga habilitadas las extensiones necesarias, incluyendo:

```toml
[project.markdown_extensions]
admonition = {}
pymdownx.details = {}
```

La validación estructural del Markdown no sustituye la comprobación del
resultado renderizado.

---

## 10. Código y comandos

Los bloques de código y comandos deben aparecer dentro de un contexto
didáctico.

Cuando corresponda, se indicará:

- qué se pretende conseguir;
- en qué sistema operativo, shell o herramienta se trabaja;
- qué conocimientos o condiciones previas son necesarios;
- qué hace el comando o código relevante;
- qué resultado se espera;
- cómo comprobar que la operación ha funcionado.

No deben incluirse bloques extensos sin explicación.

Cuando existan variantes equivalentes para distintos sistemas o herramientas,
debe valorarse el uso de tabs.

---

## 11. Ejercicios y práctica

La práctica debe integrarse cerca de los conceptos necesarios para resolverla.

No se concentrará sistemáticamente toda la práctica al final del tema salvo que
exista una justificación pedagógica.

Se distinguen cuatro tipos principales.

### 11.1 Ejercicio autocorregible

Objetivo: práctica inmediata con retroalimentación incluida.

Existe una solución esperada y se publica una resolución razonada para que el
alumnado pueda autocorregirse.

### 11.2 Práctica guiada

Objetivo: aprender un procedimiento mediante apoyo gradual.

Puede incluir:

- pasos;
- pistas;
- comprobaciones parciales;
- resultados intermedios.

No necesita una única solución final cerrada.

### 11.3 Caso abierto

Objetivo: analizar, decidir y argumentar.

Puede admitir varias respuestas razonables.

La valoración debe centrarse en la calidad del razonamiento y en los criterios
utilizados.

### 11.4 Actividad evaluable

Objetivo: recoger formalmente evidencias de aprendizaje.

Debe disponer de criterios, rúbrica, lista de cotejo u otro instrumento
explícito de valoración.

Puede no publicar la solución detallada.

### 11.5 Selección del tipo

Usar:

- **ejercicio autocorregible** cuando exista una solución esperada y se publique
  la resolución;
- **práctica guiada** cuando el aprendizaje requiera acompañamiento progresivo;
- **caso abierto** cuando existan varias soluciones razonables;
- **actividad evaluable** cuando la finalidad sea recoger evidencias para
  evaluación formal.

El tipo de actividad debe ser coherente con su finalidad, aunque no sea
necesario convertir esa clasificación interna en un encabezado visible para el
alumnado.

---

## 12. Patrón canónico de ejercicios autocorregibles

El patrón se aplica exclusivamente a ejercicios autocorregibles con solución
publicada.

Plantilla oficial:

```md
!!! question "Ejercicio N. Título del ejercicio"

    Enunciado del ejercicio.

    ??? success "Solución ejercicio N"

        Desarrollo razonado de la solución.
```

Reglas:

1. El ejercicio utiliza `!!! question`.
2. El título sigue el formato `Ejercicio N. ...`.
3. La solución se incluye dentro del ejercicio.
4. La solución utiliza `??? success`.
5. El título sigue `Solución ejercicio N`.
6. La solución permanece oculta por defecto.
7. La solución explica el razonamiento o procedimiento y no únicamente la
   respuesta.
8. Se evitarán anidaciones adicionales de admonitions salvo necesidad
   didáctica clara.

Para prácticas guiadas, casos abiertos y actividades evaluables pueden
utilizarse otros formatos.

---

## 13. Planificación didáctica

La planificación de cada tema o bloque curricular debe permitir conocer, cuando
corresponda:

- `Prerrequisitos:` conocimientos o habilidades previas.
- `Progresión didáctica:` secuencia prevista de aprendizaje.
- `Capacidad:` capacidad o capacidades relacionadas.
- `Criterio de evaluación:` criterios relacionados.
- `Bloque de contenidos:` bloque curricular.
- `Referencia normativa:` fuente exacta verificable.
- `Evidencias de aprendizaje:` resultado observable.
- `Instrumento de evaluación:` mecanismo utilizado para valorar las evidencias.

Esta información pertenece principalmente a la capa de planificación y
trazabilidad del proyecto.

No es necesario reproducirla íntegramente en cada página destinada al
alumnado.

---

## 14. Revisión pedagógica humana

Antes de considerar terminado un material docente debe realizarse una revisión
pedagógica que compruebe:

1. **Trazabilidad curricular**: capacidad, criterio, bloque y referencia
   normativa cuando corresponda.
2. **Desarrollo conceptual**: los conceptos importantes están explicados, no
   simplemente mencionados.
3. **Progresión didáctica**: no existen saltos injustificados.
4. **Autosuficiencia**: el material puede estudiarse sin explicación oral
   imprescindible.
5. **Nivel adecuado**: profundidad y terminología son apropiadas para el
   alumnado.
6. **Ejemplificación**: los conceptos que lo necesitan disponen de ejemplos
   útiles.
7. **Teoría y práctica**: existe un equilibrio adecuado.
8. **Actividades**: el tipo de actividad corresponde con su finalidad.
9. **Consignas**: son claras, accionables y verificables.
10. **Soluciones y pistas**: son razonadas y pedagógicamente útiles cuando
    corresponda.
11. **Recursos visuales**: Mermaid, tablas, tabs, admonitions y código tienen
    una función didáctica real.
12. **Carga cognitiva**: longitud, densidad, fragmentación y ritmo son
    adecuados.
13. **Contenido para el alumnado**: no está contaminado por metadatos internos
    innecesarios.

Superar validadores automáticos no implica superar esta revisión.

---

## 15. Revisión visual con Zensical

Todo cambio significativo en contenido docente debe revisarse en el sitio
renderizado antes de considerarse terminado.

La revisión debe realizarse mediante el entorno Zensical del proyecto, por
ejemplo:

```bash
./.venv/bin/zensical serve
```

Debe comprobarse visualmente, cuando existan:

- jerarquía de encabezados;
- párrafos y listas;
- admonitions;
- soluciones colapsables;
- Mermaid;
- tabs;
- tablas;
- bloques de código;
- navegación;
- enlaces;
- densidad visual general.

La existencia del Markdown correcto no garantiza por sí sola que el resultado
renderizado sea correcto.

Una funcionalidad editorial que dependa de extensiones de Markdown debe
comprobarse también en la configuración de Zensical.

---

## 16. Validación automática del harness

El harness puede comprobar aspectos estructurales y objetivos que puedan
validarse de forma fiable.

El validador editorial `scripts/validate_editorial.py` comprueba, entre otros:

- aplicación de la regla `question/solution` a ejercicios autocorregibles;
- uso reservado de `question`;
- formato `Ejercicio N. ...`;
- presencia de solución;
- uso de `??? success`;
- formato `Solución ejercicio N`;
- coherencia numérica entre ejercicio y solución;
- soluciones situadas fuera de su ejercicio;
- anidaciones adicionales de admonitions cuando puedan detectarse.

Cuando se incorporen nuevas reglas automáticas, estas deben comprobar
propiedades estructurales verificables y no intentar sustituir el juicio
pedagógico.

---

## 17. Qué no valida automáticamente el harness

La validación automática no determina:

- si una explicación es suficientemente clara;
- si un tema tiene la profundidad adecuada;
- si la progresión pedagógica es correcta;
- si el nivel es adecuado para el alumnado;
- si un ejemplo es realmente útil;
- si los ejercicios ayudan a aprender;
- si una solución razona correctamente el procedimiento;
- si existe un buen equilibrio entre teoría y práctica;
- si Mermaid es preferible a una tabla o a texto;
- si un tab aporta claridad;
- si un admonition está pedagógicamente justificado;
- si una página resulta visualmente clara una vez renderizada.

Estos aspectos requieren revisión educativa y humana.

---

## 18. Criterio de finalización de un material

Un tema no se considera terminado únicamente porque:

- exista el archivo Markdown;
- compile;
- supere el validador;
- tenga trazabilidad curricular;
- contenga ejercicios.

Para considerarlo terminado debe superar conjuntamente:

1. **validación técnica**;
2. **validación editorial estructural**;
3. **revisión visual renderizada**;
4. **revisión pedagógica humana**.

El objetivo del proceso no es producir documentación formalmente correcta,
sino material docente que permita aprender.

---

## 19. Relación con la normativa curricular

Esta guía regula la forma editorial, la organización pedagógica y los patrones
de autoría.

No altera requisitos curriculares, capacidades, criterios de evaluación,
contenidos ni duración del módulo.

Estos elementos deben derivarse de la fuente normativa primaria:

`normativa/BOE-A-2011-9930.pdf`