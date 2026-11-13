# Documentación del proyecto · Psicología y Salud

Registro de qué se construyó, con qué criterios y cómo seguir editándolo. Pensado para retomar el trabajo en otra sesión (humana o con Claude) sin reconstruir el contexto.

## 1. Qué es

Un sitio de una sola página (`index.html`) con scrollytelling pedagógico sobre la bibliografía básica del curso **Psicología y Salud** (Ciclo de Formación Integral, Facultad de Psicología, Udelar, Uruguay, 2026). Recorre las 10 unidades del programa en su orden, texto por texto. **No es material oficial de la cátedra** (aviso visible en portada, pie y README, con enlace al formulario anónimo de sugerencias).

Publicación: GitHub Pages, `https://pasquinell.github.io/psico-y-salud/` (repo `Pasquinell/psico-y-salud`, rama `main`, raíz).

Pedido original, en resumen: un solo `index.html` sin build ni dependencias (salvo Google Fonts); barra superior con regla de años y saltos «retrocede / avanza N años»; índice automático; scrollies con diagramas que se arman por pasos; anatomía fija de bloque; **3 preguntas de desarrollo y 20 V/F con justificación desplegable por texto**; desde 2026 el curso evalúa sobre todo con V/F justificando las verdaderas en no más de 4 líneas. Contenido basado sólo en los materiales de estudio provistos (que **no se citan ni se publican**: sólo se nombra a los autores originales). Sin división por parciales: el programa no la indica.

## 2. Archivos

| Ruta | Qué es |
|---|---|
| `index.html` | El sitio publicado (~2 MB). **Se genera** con `trabajo/build.py`. |
| `img/hygieia.jpg` | Gustav Klimt, *Hygieia*, detalle de *La Medicina* (1900-1907). Dominio público, Wikimedia Commons `File:Klimt_Hygieia.jpg` (reescalada a 720 px). Sólo en la portada. |
| `.nojekyll`, `.gitignore`, `README.md` | Publicación. |
| `doc/README.md` | Este archivo. |
| `doc/tools/check.py` | Chequeos estáticos (ver § 8). |
| `doc/tools/figs_preview.py` | Todos los diagramas en estado final, 6 por página → `doc/tools/out/figs_N.html` (`dark`, `in=`, `out=` opcionales). |
| `doc/tools/cdp.mjs` | Chrome headless con scroll real: capturas, errores JS y `scrollWidth` vs `innerWidth`. |
| `trabajo/` | **Fuente de edición, ignorada por git** (ver § 3). |
| `recursos/` | Materiales de entrada (resúmenes con copyright y datos personales, preguntas de años anteriores). **Ignorado por git; nunca publicar ni nombrar en el sitio.** |
| `prompt.md` | Pedido original; ignorado por git porque nombra los materiales de entrada. |

## 3. Cómo se arma `index.html`

`python3 -I trabajo/build.py` concatena, en este orden:

1. `trabajo/parts/00_head.html`: `<head>`, todo el CSS, marcadores de flecha, barra superior, índice.
2. `trabajo/parts/10_intro.html`: portada, cómo usar, mapa del programa (`{{MAPA}}`), gráfico año × orden (`{{VAIVEN}}`, `{{ULEGEND}}`).
3. `trabajo/blocks/*.html` en orden alfabético: `uNN_00_head.html` (encabezado de unidad), `uNN_KK.html` (bloques), `uNN_99_repaso.html` (repaso de unidad).
4. `trabajo/parts/95_cierre.html`: «Cinco hilos» y preguntas integradoras del curso (`#hilos`).
5. `trabajo/parts/99_tail.html`: léxico (`{{LEXICO}}`), pie y todo el JS.

Los marcadores se rellenan desde los atributos de los bloques (mapa y gráfico) y desde `trabajo/lex/*.tsv` (léxico: `término<TAB>año<TAB>autor<TAB>id de bloque<TAB>definición`). Opciones: `units=3,4` (sólo esas unidades) y `out=RUTA`.

**Regla:** mientras exista `trabajo/`, editá ahí y regenerá; no edites `index.html` a mano (se pisaría en el próximo build). Si `trabajo/` se pierde (no está en git), desde ese momento `index.html` pasa a ser la fuente única y se edita directamente; el mapa, el gráfico y el léxico ya están renderizados en él como HTML estático.

`trabajo/SPEC.md` es la especificación con la que se escribieron los bloques (fuentes, reglas de citación, anatomía, reglas de diagramas). Sirve para escribir bloques nuevos con el mismo criterio.

## 4. Estructura del contenido

10 unidades, 50 bloques, 77 scrollies, 1000 V/F, 150 preguntas de desarrollo en bloques + 2 integradoras por repaso + 3 del cierre, 240 términos de léxico. Ids: unidad `uN`, bloque `bN-K`, repaso `rN`.

- **U1** La psicología de la salud: b1-1 Morales Calatayud 2009 · b1-2 Morales Calatayud 2015 + soportes del Instituto de Psicología de la Salud 2010 · b1-3 Piña y Rivera 2006.
- **U2** Concepciones de salud-enfermedad-atención: b2-1 Morales Calatayud 2009 («Una mirada al campo…») · b2-2 De Lellis, Interlandi y Martino 2015 · b2-3 García-Viniegras y González Benítez 2000 + Max-Neef 1986 · b2-4 De Lellis 2010. (De Lellis 2006 no tenía material: sin bloque.)
- **U3** Determinantes: b3-1 Castro 2013 (compl.) · b3-2 De Lellis, Interlandi y Martino 2015 · b3-3 Macri, Vignolo y Sosa Abella 2009 + Vázquez · b3-4 Santana 2012 (compl.) · b3-5 Otero y Zunzunegui s/f · b3-6 OMS, Comisión DSS 2008 + OPS/OMS.
- **U4** Modelos de atención: b4-1 Menéndez 1985 · b4-2 De Lellis 2015 · b4-3 De Lellis, Saforcada y Mozobancyk 2010 · b4-4 OPS 2021 + Gafas, Herrera y Bonilla 2017 · b4-5 Saforcada 1999.
- **U5** Epidemiología: b5-1 Alarcón 2009 + López-Moreno et al. 2000 · b5-2 Benia et al. 2008 + OPS.
- **U6** APS, niveles, promoción: b6-1 Alma-Ata 1978 · b6-2 sector y sistemas de salud (OPS, Saforcada, De Lellis) · b6-3 De Lellis y Berra 2015 + Benia, Macri y Berhier 2008 · b6-4 Vignolo et al. 2011 · b6-5 Ottawa 1986 + Buss 2008 · b6-6 OPS 2007 renovación APS · b6-7 Ley 18.211 + Tomasina y León · b6-8 Tomasina, salud de los trabajadores de la salud (s/f).
- **U7** Accesibilidad y derechos: b7-1 Arias, Ramos y Suárez 2009 · b7-2 Rudolf 2013 · b7-3 Ley 18.335 (2008) · b7-4 Saforcada (barrera psicosociocultural, s/f) · b7-5 Juárez s/f.
- **U8** Calidad y evaluación: b8-1 calidad (Donabedian, Palmer, Grönroos, Llinás 2010, OMS 2020) · b8-2 Salinas y González 2006 + Domínguez et al. 2021 · b8-3 Ley 19.529 (2017) · b8-4 Plan Nacional de Salud Mental 2020-2027 · b8-5 Piñol y Sanz 2004.
- **U9** Relación asistencial: b9-1 Tizón (s/f) · b9-2 Nieto-Munuera 2004 cap. 5 · b9-3 Nieto-Munuera 2004 cap. 7 · b9-4 Moreno-Altamirano 2007 · b9-5 Rodríguez Silva 2006.
- **U10** Intervenciones: b10-1 Martín Alfonso 2003 · b10-2 Fernandes Alves et al. 2009 · b10-3 Buitrago et al. (s/f) · b10-4 Morales Calatayud 2009 (APS) · b10-5 Morales Calatayud 2009 (hospitales) · b10-6 Giménez y Suárez 2017 + Protesoni (s/f) · b10-7 Perea Negreira (s/f).

Secciones de apoyo: portada `#portada`, `#como-usar`, `#mapa` (tabla generada), `#vaiven` (gráfico año × orden del programa, generado; textos s/f en una franja aparte), repasos `r1`…`r10` al final de cada unidad (tarjetas, a veces un `.hilo`, 2 preguntas integradoras), cierre `#hilos` (cinco hilos + 3 preguntas integradoras del curso) y `#lexico` (buscador; chip rojo = año del texto del programa donde aparece el término, no fecha de invención).

### Anatomía de cada bloque

1. `bhead`: número, chips (`.chip.yr` año, autor, `.chip.topic`, `.chip.comp` complementaria), título con `.au` autores.
2. `.cols2`: **Dónde estamos** (`.card.ctx`) y **El problema** (`.card.prob`).
3. `.lectura`: Primera lectura + `.nucleo` (el texto en un párrafo) + `.ideas`.
4. Uno o más `.scrolly`.
5. Recuadros `.call`: `caso` (Caso / observación; los casos inventados con fines didácticos dicen «ilustrativo»), `uy` (Uruguay), `ant` (Anticipación, fechada), `rec` (Recontextualización), `nota`, `warn` (Trampa).
6. `.quotes` «Los autores en sus palabras»: `.mk.lit` ⚑ (literal confiable: sólo redacciones canónicas) o `.mk.sus` ≈ (fiel al sentido; casi todas).
7. `.trampas` (Trampas de examen).
8. `details.preg` (autoevaluación con respuesta modelo).
9. `.desarrollo`: 3 `details.preg.dev` con respuesta de parcial y `p.clave` (qué evalúa, error típico).
10. `.vf`: 20 `li[data-a="V|F"]` con `p.vq` y `details` (justificación). El JS agrega botones V/F, marca acierto, abre la justificación y lleva la cuenta; «Mostrar todas» y «Reiniciar».

## 5. Mecánica (JS en `99_tail.html`)

- **Barra superior:** sección actual = última `[data-title]` cuyo borde superior pasó el 40 % de la pantalla. Año = primer `.chip.yr` de la sección; el punto se mueve sobre la regla 1975-2025 y deja un fantasma en la posición anterior con «↩ retrocede N años» / «→ avanza N años». Sin `data-year` (s/f, secciones generales) el punto no se mueve. Insignia «Unidad N» con el color de la unidad.
- **Scrolly:** paso activo = última `.step` cuyo borde superior está por encima del 58 % de la pantalla (78 % en ≤ 900 px), calculado en cada scroll (rAF), no por orden de llegada de IntersectionObserver. `[data-s="N"]` recibe `.on` si paso ≥ N; `.fade[data-off="N"]` recibe `.off` (atenuado) si paso ≥ N; `.draw` + `pathLength="1"` dibuja el trazo. Clic en una tarjeta fuerza su paso.
- **Invariante:** el `data-s` máximo de un diagrama no supera la cantidad de pasos (lo controla `check.py`).
- Índice automático desde `data-toc` / `data-tema` / `data-u`. Tema oscuro: `prefers-color-scheme` + botón ◐, guardado en `localStorage` (`pys-theme`) dentro de try/catch.
- Móvil (≤ 900 px): diagrama fijo arriba (máx. 50 vh), pasos debajo. A 390 px, `scrollWidth == innerWidth` (verificado).

## 6. Vocabulario SVG

- Cajas: `.box` (tinta), `.boxs` (neutra), `.bg` verde, `.bo` ladrillo, `.bc` ocre, `.bp` ciruela, `.bb` índigo, `.bt` turquesa.
- Líneas: `.ln`, `.lnd` (punteada), `.lg .lo .lc .lp .lb .lt`. Rellenos: `.fg .fo .fc .fp .fb .ft .fi .fi2`, `.wt` (color de tarjeta).
- Texto: base 13 px; `.ti` 15 px negrita; `.sm` 11 px; `.xs` 9,5 px; `.ser` serif itálica; colores `.tG .tO .tC .tP .tB .tT`.
- Animación: `[data-s]`, `.up` (sube al aparecer), `.draw`, `.fade` + `data-off`, `.pulse`.
- Flechas (definidas una sola vez al inicio del `<body>`): `#ar` tinta, `#arg` verde, `#aro` ladrillo, `#arc` ocre, `#arp` ciruela, `#arb` índigo, `#art` turquesa.
- Sólo clases (nada de colores fijos) para que funcione el modo oscuro. viewBox de 600 de ancho.

## 7. Diseño

- Paleta «papel sanitario»: fondo `--paper #f4f1ea`, tarjeta `--card #fffefa`, tinta `--ink #1c211f`; acentos `--green #2e6650` (acento principal y favicon), `--brick`, `--ochre`, `--indigo`, `--plum`, `--teal`, cada uno con su `-soft`. Sin parciales, el color va **por unidad**: `--u1`…`--u10` (el atributo `data-u` define `--uc`). Todo redefinido para oscuro en `prefers-color-scheme` y en `[data-theme="dark"]`.
- Tipografías (Google Fonts, con fallback Georgia / system-ui): **Newsreader** (títulos), **Literata** (cuerpo), **Public Sans** (etiquetas, diagramas, interfaz).
- Favicon: Ψ sobre cuadrado redondeado verde, SVG inline en `data:`.
- Portada: Hygieia de Klimt en marco de arco con crédito; sólo en la portada.

## 8. Cómo verificar (desde la raíz)

```bash
python3 -I trabajo/build.py                    # regenera index.html
python3 -I doc/tools/check.py                  # etiquetas, data-s vs pasos, ids, #enlaces, imágenes,
                                               # 3 desarrollo + 20 V/F por bloque (7-13 V), texto prohibido
python3 -I doc/tools/figs_preview.py [dark]    # diagramas en estado final
google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=1360,2600 \
  --screenshot=doc/tools/out/figs_0.png "file://$PWD/doc/tools/out/figs_0.html"
node doc/tools/cdp.mjs "file://$PWD/index.html" doc/tools/out/d 1400 900 "b6-4:3000"   # escritorio
node doc/tools/cdp.mjs "file://$PWD/index.html" doc/tools/out/m 390 844 "b6-7:3000"    # móvil
```

`check.py` también rechaza menciones a los materiales de entrada (`recursos/`, `.pdf`, `.docx` y la lista sensible de `trabajo/prohibido.txt`, que está fuera de git). Después de tocar un diagrama, mirá su preview: el texto encimado sobre cajas o líneas fue el defecto más frecuente. `figs_preview` muestra todas las capas a la vez (también las que se atenúan con `data-off`).

Estado al cerrar la sesión (nov. 2026): `check.py` sin problemas; 0 errores JS; sin desborde horizontal a 390 px; diagramas revisados en claro (por cada agente) y por muestreo en oscuro.

## 9. Cómo publicar

Ver `../CLAUDE.md`. Resumen: remoto `git@github-pasquinell:Pasquinell/psico-y-salud.git` (nunca `github.com` directo); verificar `git config user.email` = cuenta personal; `git add . && git commit -m "…" && git push`. Pages: Settings → Pages → `main` / raíz. `.gitignore` deja fuera `recursos/`, `fuentes/`, `trabajo/`, `doc/tools/out/` y `prompt.md`.

## 10. Decisiones de contenido generales

- **Fuentes:** sólo los materiales de estudio provistos y las preguntas de exámenes anteriores (estas últimas sólo para calibrar y, en pocos casos marcados abajo, para completar). Nada de búsqueda web salvo la imagen de portada. En el sitio sólo se nombran autores y documentos originales.
- **Temporalidad:** conceptos posteriores a un texto van en recuadros de Anticipación con fecha (p. ej. APS renovada 2007 dentro de Alma-Ata 1978).
- **Años:** el de la cita del programa. Sin año confirmado → `s/f` (chip) y `data-year=""`. Cuando un bloque agrupa textos, el primer chip es el del texto principal.
- **Agrupamientos:** textos muy breves o articulados en el material se agruparon para que los 20 V/F no se repitan (ver § 4 y las notas por unidad).
- **Casos:** cuando el material no trae un caso, algunos recuadros usan escenas inventadas con fines didácticos, rotuladas «ilustrativo» / «hipotético».
- **Pendiente conocido:** las preguntas de exámenes anteriores mencionan contenidos que el material no cubre (p. ej. Castro: teoría del etiquetamiento, Goffman, Freidson; Vázquez: Frenk y Bobadilla). No se agregaron por no poder verificarlos; conviene completarlos con los textos originales.

## 11. Notas por unidad (correcciones al material de entrada, datos no confirmados, diagramas)

## Notas · Unidad 1

### Bloques
- b1-1 · Morales Calatayud (2009) · La psicología y los problemas de salud (ya hecho, modelo).
- b1-2 · Morales Calatayud (2015) · La psicología y el campo de la salud: tensiones, logros y potencialidades. **Agrupa** los «Soportes de nuestra psicología de la salud» del Instituto de Psicología de la Salud (Udelar, 2010): el texto de soportes solo no daba para 20 V/F. Primer chip yr 2015, segundo 2010.
- b1-3 · Piña y Rivera (2006) · Psicología de la salud: algunas reflexiones críticas sobre su qué y su para qué.
- r1 · repaso de la unidad.

### Correcciones al material
- «Calayatud» → Calatayud (todo el material).
- Piña y Rivera: el nacimiento formal es en la primera mitad de los **setenta** (material). Una respuesta de estudiantes en las preguntas de exámenes anteriores dice «sesenta»: es error; se usa como V/F falso.
- Soportes IPS: una respuesta de estudiantes marca como verdadero que el eclecticismo dinámico crítico es «dogmático»; el material dice «antidogmático».

### Datos no confirmados / completados
- Piña y Rivera: el material sólo trae la cita inicial, la tabla de definiciones, los 4 supuestos del «modelo psicológico de salud biológica» y el título del «modelo dos» (sin contenido; las figuras no se extrajeron). Se agregó, con marca ≈, la cita del psicólogo como «educador» (aparece transcripta en la corrección de un parcial 2022). En un recuadro Nota se atribuye el modelo a Ribes (1990) y se mencionan sus tres factores (modulación de estados biológicos, competencias, estilos) como referencia general, no como dato del texto.
- Nombres completos de Piña López y Rivera Icedo: iniciales según cita habitual.
- Año de creación del IPS (2010): según la consigna y preguntas de examen.

### Diagramas
- b1-2 (1): planos del campo de la salud + tres columnas tensiones / logros / potencialidades + saldo.
- b1-2 (2): «edificio» de los soportes del IPS (ser humano, ética y epistemología, teoría, cultura y derechos, destino social).
- b1-3: seis definiciones (1979-1997) → «sin modelo teórico» → lo psicológico como dimensión individualizada entre lo biológico y lo sociocultural → psicólogo educador.

## Notas · Unidad 2

### Bloques
- u2 · encabezado de unidad (con las dos tarjetas de la introducción).
- b2-1 · Morales Calatayud (2009) · Una mirada al campo de la salud y la enfermedad. Incluye la parte histórica del material («Distintas explicaciones a lo largo de la historia», atribuida a Morales) y la sección «Una mirada…» (Virchow, Terris, San Martín, Pérez Lovelle, distribución, disciplinas, salud pública). Dos scrollies.
- b2-2 · De Lellis, Interlandi y Martino (2015) · Introducción a la salud pública como área del conocimiento y de la acción (el programa lo cita como «De Lellis y Martino»; el material nombra a los tres autores). Parte de definiciones de salud, tabla de Moragas y salud como derecho. Dos scrollies.
- b2-3 · García-Viniegras y González Benítez (2000) + Max-Neef (1986). **Agrupados**: García-Viniegras tiene en el material sólo la definición de calidad de vida; no daba para 20 V/F. data-year 2000; chips 2000 y 1986. Dos scrollies.
- b2-4 · De Lellis (2010) · Psicología y políticas públicas saludables.
- r2 · repaso.
- **De Lellis (2006)** «¿Políticas de salud mental o lo mental en las políticas de salud?»: sin material, no se escribió bloque (se menciona en una Nota de b2-4).

### Correcciones al material
- «Leawell y Clarck» → Leavell y Clark.
- «Edward Amory» → Charles-Edward Amory Winslow (definición de salud pública).
- «Safocarda» → Saforcada; «Calayatud» → Calatayud.
- La cita «Concebir las necesidades humanas tan sólo como carencias…» se atribuye en el material a De Ávila (comentarista); es de Max-Neef (1986). Se cita como Max-Neef con ≈.
- OMS: Constitución adoptada en 1946, vigente en 1948 (el programa dice 1948). Se usa 1946 y se explica en Nota.
- De Lellis 2010: el material dice que «a mediados del siglo XIX las enfermedades transmisibles no eran tan frecuentes» y ubica la transición epidemiológica «durante el siglo XIX»; parece errata. El bloque evita fechar esas etapas y lo explica en Nota.

### Datos no confirmados / completados
- Año de la propuesta de Terris: el material dice 1992; otras fuentes del curso dicen 1990 o 1975. Se omite el año en el texto.
- Definición de «Capote y Villar»: el material la rotula «SNIS»; no se pudo confirmar a qué SNIS refiere, se atribuye sólo a Capote y Villar.
- García-Viniegras: además de la definición de calidad de vida (material), se usaron la definición de bienestar psicológico (transcripta en la corrección del parcial 2022), satisfacción como balance expectativas-logros, componentes cognitivo/afectivo y las categorías nivel/modo/estilo de vida (de listas de V/F de estudiantes, coherentes con el artículo). Verificar contra el texto original si se consigue.
- Max-Neef: ejemplos de cada tipo de satisfactor y algunas celdas de la matriz tomados de respuestas de examen coherentes con el original.
- Nombres de pila de coautores (Interlandi, Martino, González Benítez) sólo con inicial.

### Diagramas
- b2-1 (1): explicaciones por época en dos columnas (sobrenatural/idealista vs natural/materialista), dualismo cartesiano, enfoques individual vs colectivo, multicausalidad y DSS.
- b2-1 (2): triada agente-huésped-ambiente con sus componentes, historia natural (Leavell y Clark), «ser humano activo», umbrales de Pérez Lovelle.
- b2-2 (1): escalera de definiciones de Leriche a Saforcada (del estado al proceso).
- b2-2 (2): las siete concepciones de Moragas como barras sobre una línea de tiempo (línea de concepciones por época).
- b2-3 (1): calidad de vida = factores objetivos + subjetivos; bienestar psicológico (cognitivo/afectivo); nivel, modo y estilo de vida.
- b2-3 (2): matriz 9 × 4 de Max-Neef con satisfactores de ejemplo; bienes → satisfactores → necesidades; cinco tipos de satisfactores (exógenos / endógenos).
- b2-4: policía médica → transición → emergentes; respuesta hegemónica vs políticas públicas saludables; formación actual → lineamientos.

## Unidad 3 · Determinantes y determinación social de la salud

### Bloques

| id | Autor | Año | Título |
|---|---|---|---|
| b3-1 | Castro | 2013 | De cómo la sociología construye sus objetos (complementaria) |
| b3-2 | De Lellis, Interlandi y Martino | 2015 | Introducción a la salud pública como área del conocimiento y de la acción |
| b3-3 | Macri, Vignolo y Sosa Abella (+ Vázquez) | 2009 | Salud pública y determinantes de la salud |
| b3-4 | Santana | 2012 | Empleo, condiciones de trabajo y salud (complementaria) |
| b3-5 | Otero y Zunzunegui | s/f | Determinantes sociales de la salud y su influencia en la atención sanitaria |
| b3-6 | OMS, CDSS (+ OPS/OMS) | 2008 | Subsanar las desigualdades en una generación |
| r3 | Repaso | | 6 tarjetas, hilo de 6 hitos, 2 integradoras |

Orden de los bloques: el del material de la unidad (Castro, De Lellis, Macri, Santana, Otero, OPS, OMS).

Agrupaciones y ubicación de contenidos:
- **Vázquez (2008)** no tiene bloque propio: el material sólo trae su definición de determinantes y la de modo de vida. Su definición está en el encabezado de unidad y en b3-3 (chip «Vázquez»), donde Macri y colaboradores la retoman.
- **OPS/OMS «Determinantes sociales de la salud»** se agrupó con el informe de la CDSS en b3-6: es muy breve y 20 V/F propios serían repetitivos. Como se enmarca en la Agenda 2030 (2015), posterior al informe de 2008, va en un recuadro **Anticipación** dentro de b3-6, con 6 V/F propios.
- **Lalonde (1974), Carol Buck (1986), medicina social latinoamericana, Castellanos, eco-epidemiología** van en b3-3, que es donde el material los desarrolla. Lalonde aparece también en b3-2 (historia de la salud pública) y en b3-5 (correspondencia con la CDSS).
- **Dahlgren y Whitehead**: el material describe el modelo de anillos concéntricos sin nombrarlo (en la sección de De Lellis); va en b3-2 como segundo diagrama, y la atribución se menciona sólo en un recuadro Nota.
- **Determinación social**: el material no la desarrolla como concepto aparte (no aparece Breilh). Se trabaja con la medicina social latinoamericana y Castellanos (reproducción social, subordinación de lo biológico a lo social), en el diagrama antes/después de b3-3.
- La introducción de la unidad (enfoque naturalista vs. social, Dubos y McKeown, definiciones de DSS) va en las tarjetas del encabezado `u3`.

### Correcciones al material

- «Luis Castellanos» → **Pedro Luis Castellanos** (así lo nombra la bibliografía del curso).
- «Marx y Engel» → Marx y Engels.
- Quinto eje de la promoción de la salud: «fortalecer la acción inmunitaria» → **acción comunitaria** (Carta de Ottawa, 1986). Se explica en un recuadro Nota de b3-2.
- Illich, *Némesis médica*: el material la ubica «a principios del siglo XX»; es de mediados de los 70. Corregido en el texto y anotado en b3-3.
- «Subsanar las desigualdades de una situación» → «… en una generación» (título del informe).
- Prevención secundaria: el material dice que su objetivo es «evitar su aparición o retardar su progreso»; evitar la aparición es lo propio de la primaria. Se redactó como «detener o retardar su progreso y evitar secuelas».
- Pasteur y los «tratamientos con antibióticos»: se redactó sin esa atribución (microbiología, identificación de agentes, prevención de infecciosas).
- «Mc Keown» → McKeown.

### Datos no confirmados

- Porcentajes de Lalonde (43/27/19/11 %): se atribuyen a Lalonde, como en el material. En la bibliografía también se vinculan a un análisis posterior de Dever (1976). Hay una nota en b3-3 que lo marca como no confirmado. El diagrama dice «donde se concentra el gasto» para el sistema sanitario. Es cualitativo: el material no da cifras de gasto y no se inventaron.
- Otero y Zunzunegui: sin año en el programa (`data-year=""`, chip s/f). Es posterior a 2008 porque explica el informe final de la CDSS.
- Santana: no se usó el nombre de pila porque el material no lo trae.
- Hugo Villar se presenta como médico uruguayo (conocimiento general, no está en el material).
- Eco-epidemiología asociada a Mervyn y Ezra Susser: sólo en una Nota. Sale de las preguntas de exámenes anteriores, no del material principal.
- El viejismo como término «desde 1969» se mantiene sin atribuirlo a un autor.
- Las preguntas de exámenes anteriores mencionan contenidos de Castro que no están en el material de la unidad: niveles de problematización, teoría de la etiquetación, Conrad, Berger y Luckmann, Becker, Scheff, Goffman, Freidson. También mencionan contenidos de Vázquez: Frenk y Bobadilla, cuatro dimensiones (población, ambiente, organización social, genoma), «causas de las causas», multicausalidad difusa. **No se incluyeron**, porque las respuestas de esos archivos son de estudiantes y no se pueden verificar. Es un hueco conocido: conviene completarlos si se consigue el texto original.

### Diagramas (9 scrollies)

1. b3-1 · Cuatro niveles de la perspectiva clásica (macro → micro), interconexión y efecto ideológico de los estilos de vida.
2. b3-2 · Modelos causales: agente→huésped, tríada ecológica con «caja negra», causa/efecto múltiples, DSS 1998 (se atenúa) → DSS 2009.
3. b3-2 · Anillos concéntricos (persona, estilos de vida, redes, condiciones socioeconómicas, culturales y ambientales).
4. b3-3 · Campos de salud de Lalonde con porcentajes, conclusión sobre el gasto, crítica individualista y Carol Buck (las barras se atenúan, el entorno enmarca todo).
5. b3-3 · Antes/después: factores que se suman (se atenúan) → medicina social, Castellanos (general/particular/singular con tiempos de efecto) y eco-epidemiología multinivel.
6. b3-4 · Cadena del trabajo: determinantes económicos y políticos → calidad del empleo → sistema dual → carga (4 %/11 % del PIB; Brasil vs. Reino Unido).
7. b3-5 · Marco conceptual de la CDSS: contexto → posición social → 6 intermedios → exposición, vulnerabilidad, consecuencias → desigualdad.
8. b3-5 · Correspondencia Lalonde → intermedios de la CDSS (el ambiente se desdobla) y demanda → accesibilidad → utilización con sus determinantes.
9. b3-6 · Diagnóstico de la Comisión, tres principios de acción, actores y meta.

## Unidad 4 · Modelos de atención en salud — notas

### Bloques

| id | autor | año | título | notas |
|---|---|---|---|---|
| `u4` (encabezado) | — | — | Modelos de atención en salud | Las tarjetas resumen la introducción de la unidad: paradigma (Kuhn), campo (Bourdieu), Capra, y «¿qué es un modelo de atención?» (definición y dimensiones de análisis, sin autor). |
| `b4-1` | Menéndez | 1985 | El modelo médico dominante y las limitaciones y posibilidades de los modelos antropológicos | 2 scrollies. |
| `b4-2` | De Lellis | 2015 | Un nuevo paradigma en salud mental: ejes de la transformación | 2 scrollies. Aquí se desarrollan Kuhn, Capra y Bourdieu (el material los cita a través de De Lellis). |
| `b4-3` | De Lellis, Saforcada y Mozobancyk | 2010 | Salud pública: perspectiva holística, psicología y paradigmas | 1 scrolly. |
| `b4-4` | OPS · Gafas, Herrera y Bonilla | 2021 · 2017 | Modelos de atención en salud · Modelo de atención integral de salud vs. calidad asistencial en el primer nivel | **Agrupados**: los dos textos son muy breves en el material (una página cada uno) y tratan el mismo tema (modelo de atención integral, APS, primer nivel); por separado, 20 V/F cada uno habrían sido repetitivos. `data-year="2021"` (primer texto del programa); el chip de 2017 va como chip simple. La definición general de «modelo de atención» (introducción de la unidad) se usa en el paso 1 del diagrama y en V/F 1-3. |
| `b4-5` | Saforcada | 1999 | Análisis de las concepciones y prácticas en salud | 1 scrolly. Va último por el orden del programa, aunque es anterior a 4.3. |
| `r4` | — | — | Repaso | 5 tarjetas, hilo de 6, 2 integradoras. |

Orden de bloques = orden del programa (Menéndez, De Lellis 2015, De Lellis et al. 2010, OPS 2021 + Gafas 2017, Saforcada 1999).

### Correcciones al material de entrada

- «Bordieu» → **Bourdieu**; «Khun» → **Kuhn**; «Mozanbyck» → **Mozobancyk**; «monovolantes» → **monovalentes**.
- «Ebing, Magnam» → **Krafft-Ebing, Magnan**; el material los pone como referentes de la «psicología positivista»: se escribió **psiquiatría positivista** (ambos fueron psiquiatras).
- «Kuhn, 1971»: es la fecha de la traducción castellana (original 1962). Se aclara en la nota de 4.2.
- «Política médica» de Peter Frank → **policía médica** de Johann Peter Frank (nombre del programa histórico; algunas versiones dicen «política»). Nota en 4.3.
- Gafas et al.: «Alma Ata (1979)» → **1978**. La frase sobre los lineamientos de la OMS de 1998 está corrompida en el material («instituyeron a las instituciones sanitarias y la población»); se redactó sin el año: «la OMS tuvo que formular nuevos lineamientos metodológicos».
- Saforcada: el material ubica «Modelo salubrista» en la columna de la medicina clínica; por coherencia con el resto («salubrista más que sanitarista» en la medicina social) se asignó lo salubrista a la línea social. «S XV – fines del siglo SVII» → siglos XV a XVII.
- Menéndez: el material usa «(DSS)» (determinantes sociales de la salud) al describir el modelo de 1985; por temporalidad se escribió «producción social y económica de la enfermedad».
- La cita sobre APS está fechada «Menéndez, 1988» (posterior al texto del programa): va en un recuadro Anticipación, no en las citas del bloque.

### Datos no confirmados

- Ficha de la OPS: no nombra el país. Las siglas (SNIS, RIISS) y el «Acuerdo N.° 918 del Órgano Ejecutivo en el Ramo de Salud» (8/4/2022) sugieren **El Salvador**; se dice en la nota como probable. La fecha del acuerdo (2022) es posterior al año del programa (2021).
- Gafas et al.: el material nombra sólo a «Gafas, Herrera»; el programa agrega Bonilla.
- Menéndez: los límites de la antropología médica (campesinado indígena, dicotomía tradicional/moderno, desatención del perfil epidemiológico y de la causalidad estructural) no están en el material de la unidad; se tomaron de preguntas de examen del texto original y coinciden con el título del artículo. No se usaron otras afirmaciones de esas preguntas (Banco Mundial 1980, etc.).
- Saforcada: la mención de otras medicinas (ayurvédica, china) viene de preguntas de examen del capítulo, no del material.
- De Lellis et al.: la cifra de 40-50 % de consultas prevenibles es del texto; se presenta como estimación de los autores.
- Conocimiento general agregado (seguro): CDPD de la ONU, 2006; Ley 19.529 de Salud Mental de Uruguay, 2017 (recuadro `uy` en 4.2); Ley 18.211 (2007) que crea el SNIS uruguayo (recuadro `uy` en 4.4); Menéndez antropólogo argentino radicado en México.
- Lista «Otras alternativas al MMH» (medicinas personalizadas, holísticas, fitoterapia…): sin autor en el material; va en una nota de 4.1 sin atribuirla a Menéndez.

### Diagramas (7)

1. `b4-1` A — Rasgos estructurales del MMH (6 grupos alrededor del núcleo) y, abajo, sus 5 funciones (curativa, control, normalización, legitimación, reproducción). 7 pasos.
2. `b4-1` B — Crisis del MMH (costos/eficacia, legitimidad) → modelo antropológico alternativo vs. adaptación sin cambio; abajo límites y posibilidades de la antropología médica. El MMH se atenúa (`data-off="4"`). 6 pasos.
3. `b4-2` A — Momentos de un paradigma según Kuhn (6, en serpentina, con retorno), Capra (cultura) y campo de Bourdieu (4 capitales en tensión). 6 pasos.
4. `b4-2` B — Ejes de transformación en salud mental: 6 filas antes/después; cada rasgo del modelo asistencialista-tutelar se atenúa (`data-off`) cuando aparece su reemplazo. 7 pasos.
5. `b4-3` — Plano distal (balanza asertivo/integrativo que se inclina), plano proximal (IR vs. SE, excluyentes, flecha «revolución»), línea de tiempo de ambos paradigmas y las 4 situaciones esterilizantes. 7 pasos.
6. `b4-4` — Círculos persona-familia-comunidad sobre la base APS; a la derecha definición general, definición OPS y lucha contra la fragmentación; abajo el primer nivel de Gafas (el «hombre enfermo» se atenúa). 7 pasos.
7. `b4-5` — Comparación IR vs. SE por 5 dimensiones (salud, objeto, disciplinas, valoración, prioridad); en el último paso la columna IR se atenúa y aparece la salida ecológico-sistémica. 6 pasos.

## Unidad 5 · Aportes de la epidemiología

### Bloques

| id | autores | año | título |
|---|---|---|---|
| b5-1 | Alarcón · López-Moreno, Garrido-Latorre y Hernández-Ávila | 2009 · 2000 | Epidemiología: concepto, usos y perspectivas · Desarrollo histórico de la epidemiología |
| b5-2 | Benia, De Mucio, León, Caviglia y Alegretti · OPS | 2008 · s/f | Situación epidemiológica del Uruguay · Una mirada a la salud de los uruguayos y las uruguayas en el largo plazo |
| r5 | repaso | | |

Agrupación: el material presenta a los autores articulados («los autores de la unidad están articulados a lo largo del módulo»). Se armaron dos bloques: concepto + historia (Alarcón y López-Moreno et al.) y Uruguay (Benia et al. y OPS). Los conceptos básicos sin autor explícito (epidemia, endemia, pandemia, red causal, caja negra, ecoepidemiología, enfoque de riesgo, prevalencia/incidencia, tipos de estudio) y la epidemiología social de Breilh van en b5-1. `data-year` de b5-1 = 2009 (Alarcón, primero en el programa); de b5-2 = 2008 (Benia).

### Correcciones al material

- «Robert Storss (1840)» → Robert Storrs (se aclara en un recuadro Nota).
- «ambiente malsano (misma)» → miasmas.
- «Sussmilch» → Süssmilch.
- «la población de 15 años se reduce a la mitad» se interpretó como la proporción de menores de 15 años.
- «La esperanza de vida se multiplicó en el último siglo» se redactó como «creció mucho».
- La línea de pobreza «por debajo del acceso a 3,5 canastas básicas» no se reprodujo (formulación dudosa).

### Datos no confirmados

- Año del informe de la OPS «Una mirada a la salud de los uruguayos y las uruguayas»: no figura; usa datos hasta 2018. Chip `s/f`.
- El material dice que el informe aporta a la «Estrategia Nacional de Desarrollo Uruguay 2025»; la estrategia suele citarse como «Uruguay 2050». Se omitió el año.
- Las cifras (65 % sobrepeso, +42 %/+66 % cáncer, +107 % Alzheimer, FNR 181 → 7.835, suicidio 15-20/100.000, etc.) se reproducen sin verificar.
- Afirmaciones sobre consumo de sustancias (marihuana «la más consumida por los jóvenes») no se usaron en V/F por ambiguas.
- Las etapas de la epidemiología se fechan como en el material (1.ª: s. XIX; 2.ª: inicios del s. XX–70; 3.ª: desde los 70; ¿4.ª? Diez Roux).

### Diagramas (4)

1. b5-1 · Concepto, objeto, usos y enfoques: etimología → objeto (López-Moreno) → descriptiva/analítica → cuatro usos (Alarcón) → tres enfoques.
2. b5-1 · Línea de tiempo vertical del desarrollo histórico (Antigüedad → ¿4.ª etapa?).
3. b5-2 · Transición demográfica (izquierda) y epidemiológica (derecha), causas de muerte (Benia) y escenario 2050 (OPS); «transmisibles» se atenúa con `data-off`.
4. b5-2 · Bifurcaciones de los determinantes de las ENT y del modelo de atención hacia 2050 (OPS) y los once ejes.

## Unidad 6 · Estrategia APS, niveles, promoción y prevención, APS renovada

### Bloques

| id | autores | año | título |
|---|---|---|---|
| b6-1 | OMS | 1978 | Declaración de Alma-Ata |
| b6-2 | OPS · Saforcada · De Lellis | 2007 (Saforcada 1999) | Sector salud, sistema total de salud y tipos de sistemas |
| b6-3 | De Lellis y Berra · Benia, Macri y Berhier | 2015 · 2008 | El legado de la APS · APS: vigencia y renovación |
| b6-4 | Vignolo, Vacarezza, Álvarez y Sosa | 2011 | Niveles de atención, de prevención y APS |
| b6-5 | OMS · Buss | 1986 · 2008 | Carta de Ottawa · Una introducción al concepto de promoción de la salud |
| b6-6 | OPS | 2007 | La renovación de la APS en las Américas |
| b6-7 | Ley 18.211 · Tomasina y León (+ Plan de prestaciones en salud mental 2011, Ley 19.529) | 2007 | Sistema Nacional Integrado de Salud |
| b6-8 | Tomasina | s/f | La salud de los trabajadores de la salud |
| r6 | repaso | | |

Agrupación: textos articulados en el material se agruparon por tema. De Lellis aparece en dos lugares (contexto de Alma-Ata y tipos de sistemas en b6-2; legado/APS selectiva en b6-3). La salud mental en el SNIS (plan 2011, Ley 19.529) va dentro de b6-7. El texto de Tomasina sobre salud de los trabajadores de la salud está al final del material de la unidad y es un tema distinto: se armó como bloque propio (b6-8), sin año.

### Correcciones al material

- «Alma-Ata, en ese momento capital de la URSS» → ciudad de la Unión Soviética (era capital de la RSS de Kazajistán). Nota en b6-1.
- Cronología de promoción: «1988: Alma Ata» → 1978; «Sudsval» → Sundsvall; «Toronto saludable 2000», «38 metas» no se usaron.
- «La conferencia de América Latina en Brasil (1992)»: la conferencia latinoamericana de 1992 suele ubicarse en Santafé de Bogotá; se menciona sin lugar.
- «La estrategia de APS planteada a principios de los 70»: la meta es de 1977 y la Declaración de 1978; se escribió «años 70» y se dejó nota.
- «APS renovada (OMS, 2005)»: se aclara que el documento de posición es de mediados de los 2000 y la publicación de 2007.
- «JUNASA: independiente del MSP»: la Ley 18.211 la crea como organismo desconcentrado dependiente del MSP. Se corrigió y se dejó nota en b6-7; no se hizo V/F sobre esto.
- «Alma Atma», «Vascarezza», «AOS» y otras erratas tipográficas corregidas.
- La cita de Sigerist se ajustó a lo que trae el material (sin «esparcimiento y descanso»).
- «Pereira Rossel» → Pereira Rossell (ejemplo de contrarreferencia, Plan Aduana; presentado como «ejemplo que suele darse»).

### Datos no confirmados

- Año del texto de Tomasina (b6-8): no figura. Año de Tomasina y León: no figura (b6-7 usa 2007 de la ley).
- Nombres de pila de varios autores no se incluyeron cuando no estaban seguros (Vignolo et al., Benia, Macri y Berhier, De Lellis y Berra, Tomasina).
- La reforma «de los gobiernos progresistas (2005-2019)»: se escribió «desde 2005».
- Hospital de Clínicas como ejemplo de segundo nivel (apuntes de clase): no se usó.
- Accesibilidad del primer nivel «1 hora de distancia» (apuntes de clase): no se usó.
- 95 % de problemas resueltos entre 1.º y 2.º nivel: cifra de Vignolo et al.; algunos estudiantes citan 80 % para el primer nivel (se aclara en nota).
- Períodos prepatogénico/patogénico de Leavell y Clark: esquema clásico usado sólo como marco del diagrama (nota en b6-4).

### Diagramas (15)

1. b6-1 · Arquitectura de la Declaración de Alma-Ata (arts. I–IX, contenido mínimo del art. VII).
2. b6-2 · Sistema total de salud de Saforcada (SOS, SPS, intersubjetivos).
3. b6-2 · Funciones y tipos de sistemas (tabla seguro social / servicio nacional / privado).
4. b6-3 · De la APS integral a la selectiva y la renovación (la selectiva se atenúa con `data-off`).
5. b6-4 · Pirámide de niveles de atención, 95 %, referencia/contrarreferencia, complejidad.
6. b6-4 · Niveles de prevención sobre la historia natural y matriz atención × prevención.
7. b6-5 · Carta de Ottawa: prerrequisitos, estrategias (anillo) y cinco áreas.
8. b6-5 · Cronología de la promoción (Sigerist → Yakarta).
9. b6-5 · Promoción vs prevención (tabla de Buss).
10. b6-6 · Valores, principios y elementos (rectángulos anidados).
11. b6-6 · Alma-Ata 1978 vs APS renovada 2007 (columna de 1978 se atenúa).
12. b6-7 · Estructura del SNIS (MSP, FONASA, JUNASA, cuota salud, prestadores, usuarios, red).
13. b6-7 · Ejes de cambio «de… a…» (columna de partida se atenúa).
14. b6-7 · Salud mental en el SNIS (1936 → 2011 → 2017, avances y críticas).
15. b6-8 · Riesgos del sector salud, CyMAT, burnout y gestión de la SST.

Total unidad 6: 15 diagramas (uno por scrolly). Verificado con check.py y capturas de figs_preview (doc/tools/out/fu56_*.png).

## Unidad 7 · Accesibilidad, usuarios y derechos en el SNIS

### Bloques
- `b7-1` Arias, Ramos y Suárez (2009) · La accesibilidad en tiempos de reforma. Incluye Stolkiner (accesibilidad como vínculo), Comes (2003: disponibilidad / acceso / accesibilidad) y la definición de sujeto de derecho de Suárez.
- `b7-2` Rudolf (2013) · La responsabilidad profesional en la protección de la salud como derecho.
- `b7-3` Ley 18.335 (2008) · Derechos y obligaciones de pacientes y usuarios. Incluye los datos de conocimiento de derechos en centros de Montevideo (2011, 2018).
- `b7-4` Saforcada (s/f) · Barrera psicosociocultural entre efectores y consultantes.
- `b7-5` Juárez (s/f) · De pacientes a consultantes.
- El encabezado `u7` resume el enfoque de derechos (Constitución de 1934, art. 44; Ley 18.211; elementos del derecho a la salud del Comité DESC, 2000).

### Correcciones al material de entrada
- «En el año 2008 se elimina la Ley 18.335»: errata; la ley se sanciona en 2008. Se escribió «sancionada».
- Título de Saforcada: «efectos médicos» → «efectores médicos». «Giro coperniano» → «copernicano». «Psicosociosultural» → «psicosociocultural».
- «Comité de Derechos Sociales y Culturales» → Comité de Derechos Económicos, Sociales y Culturales (ONU).
- Ley 18.335, art. 17: se omitió el paréntesis «(utilidad terapéutica)», probablemente errata por «futilidad terapéutica»; se parafraseó sin el término.
- Ley 18.335: el material titula «De los derechos de los pacientes» el capítulo con los arts. 22-24, que establecen obligaciones. Se presentan como obligaciones. El derecho a la historia clínica (revisarla, obtener copia, traslado entre instituciones) se menciona sin número de artículo (el material lo trae sin numerar).
- Juárez: el material ubica la «posición salubrista expansiva» «a partir del siglo XVII»; la fecha es dudosa y se omitió.

### Datos no confirmados
- Saforcada y Juárez sin año en el material: `data-year=""` y chip «s/f».
- Rudolf: año 2013 tomado del programa; Comisión Mixta MSP-Udelar fechada en 2010 según el material.
- Nombre de pila de Rudolf no consta en el material; se usa sólo el apellido.

### Diagramas
1. `b7-1`: servicios y población unidos por las seis dimensiones de la accesibilidad; abajo, disponibilidad → acceso → accesibilidad.
2. `b7-2`: modelo medicalizado y consenso diagnóstico (se atenúan desde el paso 4) frente a política progresista, derecho a la salud y perfil profesional; cierre «el cambio es cultural».
3. `b7-3`: definiciones de la ley, derechos (atención, dignidad, información) frente a obligaciones, y papel del MSP.
4. `b7-4`: condicionantes históricos y mercantiles → barrera en el espacio intersubjetivo entre componente formal e informal; efectos; en el paso 6 la barrera se atenúa y aparece el puente.
5. `b7-5`: planos de las concepciones médicas, «paciente», trato asimétrico y efectos frente a «consultante» y acciones del psicólogo sanitario.

## Unidad 8 · Evaluación de resultados de la atención

### Bloques y agrupamiento
- `b8-1` Donabedian, Palmer, Grönroos (vía Salinas y González, 2006), Llinás Delgado (2010) y OMS (2020) · Qué es la calidad de la atención. Se agruparon los textos que definen la calidad; `data-year` = 2006. Dos scrollies.
- `b8-2` Salinas y González (2006) y Domínguez et al. (2021) · Percepción del usuario y servicios psicológicos (satisfacción, expectativas, adaptación de modelos a la psicología, estudio de Monterrey).
- `b8-3` Ley 19.529 (2017) · Ley de Salud Mental.
- `b8-4` Plan Nacional de Salud Mental 2020-2027 (MSP, 2020).
- `b8-5` Piñol y Sanz (2004) · Calidad de vida en atención primaria (bloque propio; corto pero con material suficiente para 20 V/F).

### Correcciones al material de entrada
- El material atribuye «Servicios de salud de calidad» a la OPS; el programa lo cita como OMS (2020). Se usa OMS (2020) y se aclara en una nota.
- El material nombra a Llinás Delgado sólo como «Delgado»; se usa la cita del programa.
- Erratas menores: «CACLIDAD», «respecto a los DDHH» (respeto), «salid» (salud), «Notthingham» (Nottingham).
- Plan: «deberá desarrollarse como un plan vertical, como uno que alcance cada vez más imbricación en el SNIS» parece haber perdido un «no … sino»; se evitó afirmar que sea un plan vertical.

### Datos no confirmados
- Domínguez et al.: año 2021 tomado del programa (el material no lo trae).
- Cifras del Plan (20,3/100.000, 12.500 internaciones/año, 9,5 % del PBI en 2018, 18,5 % y 23,3 % de consumo de marihuana) transcritas del material sin verificación externa.
- Ley 19.529, art. 30: el material presenta riesgo inminente y capacidad de juicio afectada como condiciones conjuntas; se respetó.

### Diagramas
1. `b8-1` (a): tríada estructura → proceso → resultado; cinco elementos de Palmer; componentes técnico y humano; cuatro tipos de Grönroos.
2. `b8-1` (b): siete características de los servicios de calidad (OMS 2020), cobertura universal, acciones de mejora; cierre con Llinás Delgado.
3. `b8-2`: expectativas → satisfacción → uso, adherencia, resultados; determinantes por servicio en Monterrey; práctica privada vs ámbitos extendidos.
4. `b8-3`: antes (Ley 9.581, modelo asilar; se atenúa desde el paso 4) / después (Ley 19.529, sujeto de derecho, red comunitaria, hospitalización restringida, art. 38, Comisión de Contralor).
5. `b8-4`: línea de antecedentes 1936-2020, tres modelos que coexisten, diez nudos críticos, propósito y líneas de trabajo (destacada la de información y monitoreo).
6. `b8-5`: de las pruebas clínicas a la CVRS; usos, ventajas, instrumentos, COOP-WONCA, PECVEC y monitorización.

## Unidad 9 · Aspectos psicológicos del proceso salud-enfermedad-atención. Relación asistencial

Título tomado del programa (el encabezado del material de entrada decía «Intervenciones psicológicas en los distintos niveles de atención…», que no corresponde a esta unidad).

### Bloques

| id | autor | año | título |
|---|---|---|---|
| b9-1 | Tizón García | s/f | Componentes psicológicos de la práctica médica, cap. 1 |
| b9-2 | Nieto-Munuera y cols. | 2004 | Psicología para ciencias de la salud, cap. 5: La dimensión asistencial |
| b9-3 | Nieto-Munuera y cols. | 2004 | Psicología para ciencias de la salud, cap. 7: Comportamientos adaptativos y no adaptativos ante los estados de salud y enfermedad |
| b9-4 | Moreno-Altamirano | 2007 | Reflexiones sobre el trayecto salud-padecimiento-enfermedad-atención: una mirada socioantropológica |
| b9-5 | Rodríguez Silva | 2006 | La relación médico-paciente, cap. 1 |
| r9 | — | — | Repaso de la unidad |

Un bloque por texto, sin agrupaciones. El encabezado de unidad (`u09_00_head.html`) usa la introducción del material (proceso salud-enfermedad-atención, padecimiento, estado de enfermedad, «asistir», Morales Calatayud 1997).

Para Nieto-Munuera se usó, además de la unidad, el complemento de los caps. 5 y 7 (hospitalización, interconsulta y enlace, líneas de desarrollo de la conducta de enfermedad, IBQ).

### Correcciones al material de entrada

- «Morales Calayatud» → **Morales Calatayud**.
- «modelo biopsicosocial descrito por Engels» → **Engel (1977)**.
- «las formulaciones de Parson» → **Parsons**.
- «relación afectica» (Rodríguez Silva) → afectiva.
- «Impredicibilidad» → impredecibilidad.

### Datos no confirmados y decisiones

- **Tizón García:** la cita del programa no trae año. El material lo menciona como «Tizón García, 1998», pero hay referencias a una edición de 1988 del libro; se dejó `data-year=""` con chip **s/f** y un recuadro Nota que explica la duda.
- **Bloque 9.1:** el material de Tizón es breve y viene mezclado con otros autores (Cortés, Dapueto, Dapueto y Varela, Morales Calatayud, Martín Alfonso, Arganis Suárez). Las ideas se citan con su autor; la doble demanda se atribuye a Cortés (el material da «Cortés, 1997» y «Cortés, 2013» para dos citas distintas; en el bloque la doble demanda va sin año y la cita del cuerpo con 2013).
- **Parsons:** el material dice que su análisis de roles es de 1950 (The Social System es de 1951). En el texto no se puso año.
- **Hollender:** el capítulo atribuye la tríada actividad-pasividad / dirección-cooperación / participación mutua a Hollender; es la clasificación de Szasz y Hollender. Los cuatro modelos según valores (paternalista, informativo, interpretativo, deliberativo) se suelen atribuir a Emanuel y Emanuel; el material no los atribuye. Ambas cosas van en un recuadro Nota de 9.2, con redacción prudente.
- **Canguilhem:** Moreno-Altamirano le atribuye tres concepciones (ontológica, dinámica, social); Canguilhem suele asociarse a la oposición ontológica/dinámica. Se respetó la lectura del texto y se aclaró en una Nota.
- **OMS:** la cita usa la redacción canónica de 1946 (⚑); el material la parafrasea («ausencia de enfermedad o malestar»).
- **Moreno-Altamirano y Rodríguez Silva:** no se pusieron nombres de pila (no están en el material). Moreno-Altamirano se cita sin pronombres de género.
- **Rodríguez Silva:** el material cierra con un apartado «Parsons: perspectiva sociológica funcionalista» sin autoría clara; se usó en un recuadro de Recontextualización de 9.5.
- Los recuadros «Caso» de los cinco bloques son **casos ilustrativos** (así rotulados), no casos del material.
- No hay contenido uruguayo en el material: no se usó `call uy`.

### Diagramas (10)

- **9.1** Componentes psicológicos de la relación asistencial: paciente y médico en vínculo asimétrico, doble demanda, fantasías, pedidos y temores del paciente, esperanzas y temores del médico, problemas del vínculo, cuatro ejes de Dapueto y Varela (7 pasos).
- **9.2 a** Dos niveles de análisis: rol de enfermo (obligaciones y derechos) y rol de médico según Parsons; sistema social abierto con sus cuatro propiedades (6 pasos).
- **9.2 b** Modelos de relación: tríada de Hollender, cuatro modelos según valores, medicina contemporánea y paso de la ética de la beneficencia a la de la autonomía, sobre un eje paternalismo → autonomía (8 pasos).
- **9.2 c** Hospitalización: el hospital como institución, condiciones objetivas, indefensión (Seligman), respuesta adaptativa y no adaptativas, intervención psicosocial, interconsulta y enlace (7 pasos).
- **9.3 a** Conducta de enfermedad (Mechanic): mismos síntomas y conductas distintas, cadena percibir → responder, alta/baja inclinación, factores sociales y personales, proceso dinámico, disease e illness (6 pasos).
- **9.3 b** Tres conceptos (rol de enfermo, conducta de enfermedad, afrontamiento) y tres líneas de desarrollo: sociológica (Parsons, Suchman, Kleinman, creencias, apoyo social), medicina comportamental (Lazarus y Folkman, Bandura, Leventhal, Lipowski) y psicopatológica (Pilowsky, IBQ, Mayou, perfiles de Nieto) (7 pasos).
- **9.4 a** Línea histórica de las nociones de enfermedad coloreada por concepción (ontológica, dinámica, social): mágico-religiosa, Hipócrates, Medioevo, positivismo unicausal, multicausalidad, medicina social, Parsons, OMS y crítica de López-Moreno (7 pasos).
- **9.4 b** Trayecto salud → padecimiento → enfermedad → atención con illness, disease y sickness, dentro de un sistema cultural, y las disciplinas que requiere (6 pasos).
- **9.5 a** Tabla comparativa de los tres tipos de relación de Rodríguez Silva en cinco dimensiones (vínculo, roles, saber, enfermedad) y cuándo corresponde cada uno (5 pasos).
- **9.5 b** Bioética: enfermo-autonomía, médico-beneficencia, sociedad-justicia; extremos paternalismo y autonomismo; equilibrio; principios + respeto; método clínico en siete etapas; tecnología (6 pasos).

## Unidad 10 · Intervenciones psicológicas en los niveles de atención

### Bloques

| id | Autor | Año | Título |
|---|---|---|---|
| b10-1 | Martín Alfonso | 2003 | Aplicaciones de la psicología en el proceso salud-enfermedad |
| b10-2 | Fernandes Alves, Carmo Eulálio y Jiménez Brobeil | 2009 | La promoción de la salud y la prevención de enfermedades como actividades propias de la labor de los psicólogos |
| b10-3 | Buitrago Ramírez (coord.), Ciurana Misol, Chocrón Bentata | s/f | Prevención de los trastornos de la salud mental en atención primaria |
| b10-4 | Morales Calatayud | 2009 | La psicología en la atención primaria de la salud |
| b10-5 | Morales Calatayud | 2009 | La psicología en los hospitales y centros de rehabilitación |
| b10-6 | Giménez y Suárez · Protesoni | 2017 · s/f | Intervenciones psicológicas en el Hospital de Clínicas · Intervenciones con pacientes oncológicos en servicios de salud |
| b10-7 | Perea Negreira | s/f | Significaciones acerca del quehacer del psicólogo en el primer nivel de atención en salud |
| r10 | — | — | Repaso |

**Agrupación:** Protesoni (psicooncología) es demasiado breve para 20 V/F distintos; se agrupó con Giménez y Suárez (el texto más afín: hospital uruguayo, 2.º y 3.º nivel) en b10-6. `data-year` 2017 (primer chip); Protesoni aparece como chip «Protesoni (s/f)».

El concepto de «intervenir» (Montero, 2002; RAE) y los criterios para que una intervención sea psicológica (objetivos, marco, objeto; destinatarios usuario/equipo/institución) son aportes complementarios sin autor del programa: se ubicaron en las dos tarjetas del encabezado de unidad.

### Correcciones al material de entrada

- «Calayatud» → **Calatayud** (errata repetida).
- El material atribuye «Significaciones acerca del quehacer del psicólogo/a en el PNA» a **Protesoni**; según el programa es de **Perea Negreira**. Se siguió el programa.
- En Perea Negreira el material dice «problemáticas … de baja calidad»; el sentido es «baja complejidad». Corregido y señalado en una Trampa.
- Los arts. 36, 37 y 38 que el material inserta dentro de Fernandes Alves et al. son de la **Ley 18.211** (Uruguay), no de esos autores; se pusieron en un `call uy`. Lo mismo para la lista de «dificultades en el SNIS» (sin autor).
- La lista «Cambios propuestos en el modelo de atención» (monodisciplinar → interdisciplinario, etc.) aparece en la sección de Martín Alfonso sin atribución explícita: se presenta en una Nota sin atribuirla.
- La sección «Modalidad de intervención» (relación jerárquica, médicos ven a la psicología como rival, etc.) aparece entre Diekstra y los temas prioritarios de Morales sin autor claro: **no se usó**.
- Las cifras de mobbing («en nuestro país, 14 %») son de España (autores del PAPPS), no de Uruguay: aclarado en una Nota.

### Datos no confirmados

- Martín Alfonso: se la trata como autora (Libertad Martín Alfonso, Rev. Cubana de Salud Pública, 2003) por conocimiento general; el material dice «los autores».
- Expansión de PAPPS (Programa de Actividades Preventivas y de Promoción de la Salud, España): conocimiento general, no está en el material.
- Años s/f: Buitrago Ramírez et al., Protesoni, Perea Negreira.
- No se confirmó el nombre de pila de Perea Negreira ni de Giménez, Suárez y Protesoni (no se usan).
- La coincidencia de las cinco acciones de promoción de Martínez (1994) con la Carta de Ottawa (1986) es una Recontextualización propia.

### Diagramas (11 en 10 scrollies)

1. b10-1: tramos del proceso salud-enfermedad-atención (estilo de vida, síntomas, tratamiento, desenlaces) con las variables psicológicas de cada uno.
2. b10-2: matriz niveles de prevención (incidencia/prevalencia/secuelas) × niveles de atención (arts. 36-38), con el «no confundir».
3. b10-2: tareas del psicólogo en la intervención primaria, secundaria y terciaria + perfil profesional + adherencia.
4. b10-3: maltrato infantil: APS como ámbito idóneo, prevención primaria/secundaria/terciaria y circuito de derivación según riesgo.
5. b10-4: riesgo psicosocial en tres planos, factores (acontecimientos, estrés, tipo A, creencias, apoyo social), categorías de Diekstra y temas por etapa.
6. b10-5: de la psicología dependiente de la psiquiatría al servicio de psicología autónomo, servicios y cuatro objetivos.
7. b10-6: SNIS, Hospital de Clínicas y datos del estudio de Giménez y Suárez.
8. b10-6: trayecto de la paciente oncológica y momentos de intervención (Protesoni).
9. b10-7: triángulo de Saforcada y técnicas por nivel.
10. b10-7: desajustes (deben/pueden/se les pide), tres categorías de resultados y tensión modelo clínico / comunitario.

(El preview cuenta 11 «diagramas» porque incluye el gráfico año × orden.)