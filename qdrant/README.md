## BASES DE DATOS VECTORIALES E IA

El auge de la inteligencia artificial (IA) y el aprendizaje automático ha transformado la naturaleza de los datos. Ya no se trata solo de información estructurada como nombres, fechas o números, sino de datos no estructurados complejos como texto, imágenes, audio y comportamientos de usuarios. Este cambio ha expuesto las limitaciones de las bases de datos tradicionales, creando la necesidad de nuevas soluciones. Es aquí donde surgen las bases de datos vectoriales, diseñadas específicamente para manejar este nuevo tipo de datos en forma de vectores de alta dimensión.

La incrustación (embedding) es el proceso que transforma los datos no estructurados en vectores numéricos de tamaño fijo, capturando la semántica y las relaciones inherentes a los datos. Esto se consigue mediante grandes redes neuronales que aprenden a representar los datos en un espacio vectorial continuo, donde los elementos similares se colocan más cerca unos de otros.

Este enfoque permite realizar búsquedas basadas en la relevancia semántica o contextual, proporcionando resultados más significativos en comparación con las búsquedas de coincidencia exacta de las bases de datos convencionales.

### CONTEXTO Y DIMENSIONES

En el contexto de bases de datos vectoriales, las dimensiones se refieren al ***número de características numéricas que describen un dato en forma de vector***. Cada dimensión representa una propiedad o rasgo capturado por un modelo de IA. El número de dimensiones en un modelo de IA depende del modelo específico, pero generalmente oscila entre cientos y miles de dimensiones. 

Es importante señalar que cada dimensión no representa un dato específico del mundo real (como "género", "color" o "tamaño"). En su lugar, las dimensiones son abstracciones matemáticas aprendidas automáticamente por el modelo de IA durante el entrenamiento.

Aunque algunas dimensiones pueden terminar capturando ciertos patrones, no tienen una interpretación clara o directa. El significado emerge de la combinación de todas las dimensiones, no de una sola. Las dimensiones son componentes numéricos que juntos representan el significado, pero por sí solas no se pueden asociar directamente con conceptos humanos concretos.

Entonces: ***¿ Como es que las palabras cine y pelicula tendran valores mas cercanos a palabras como diversion y arte ?***

Sucede que las palabras ***"cine"*** y ***"película"*** tienen vectores cercanos a ***"diversión"*** y ***"arte"*** porque, durante su entrenamiento con grandes cantidades de texto, los modelos de IA observan que estas palabras aparecen frecuentemente en contextos similares.

Durante el entrenamiento del modelo de IA frases como ***"el cine es una forma de arte"*** o ***"una película divertida para ver en familia"*** son comunes. Entonces el modelo aprende que ***"cine"*** y ***"película"*** están asociadas con emociones, creatividad, entretenimiento y expresión cultural.

Esto hace que sus embeddings (vectores) se ubiquen cerca en el espacio multidimensional, no porque una dimensión específica signifique ***"arte"*** o ***"diversión"***, sino porque la combinación global de sus dimensiones refleja ese contexto compartido.

### EMBEDDING

Como se ha descrito embedding es una representación numérica de un dato en forma de vector, que captura su significado y contexto. En consecuencia, los embeddings ***no se pueden crear manualmente de forma efectiva***; requieren necesariamente un modelo de IA para generarse. 

Los modelos de IA analizan grandes volúmenes de texto y aprenden automáticamente a representar palabras, frases o documentos como vectores numéricos que capturan su significado y contexto. Aunque se pueden definir embeddings simples por reglas en casos muy básicos (como asignar valores arbitrarios a categorías), estos no capturan relaciones semánticas complejas y no son útiles en aplicaciones reales de IA.

### EJEMPLO QDRANT-PYTHON

El codigo Python de los archivos ***pelis_to_qdrant.py*** y ***consulta_pelis_qdrant.py*** son un ejemplo de como es que se almacenan y consultan los datos en una base de datos vectorial (Qdrant) con la ayuda de un modelo de IA (all-MiniLM-L6-v2).

El modelo ***"all-MiniLM-L6-v2"*** es un modelo ligero y eficiente de la biblioteca Sentence Transformers, diseñado para generar embeddings de frases y párrafos cortos. Mapea el texto a un espacio vectorial denso de 384 dimensiones, ideal para tareas como búsqueda semántica, agrupamiento y detección de similitud. 

***Requisitos:***

1. Se recomienda usar Python ***3.11*** o 3.12 por su equilibrio entre estabilidad, rendimiento y compatibilidad con las siguientes bibliotecas.
2. Biblioteca ***qdrant-client***: es el cliente oficial de Python para interactuar con Qdrant, una base de datos vectorial de alto rendimiento. Permite crear colecciones, insertar vectores, realizar búsquedas por similitud, aplicar filtros con metadatos y gestionar índices. Es ideal para integrar búsquedas semánticas en aplicaciones de IA, especialmente cuando se combina con modelos de Sentence Transformers para generar embeddings.
3. Biblioteca ***sentence-transformers***: permite generar embeddings semánticos de alta calidad para frases, párrafos o textos, usando modelos preentrenados como BERT o RoBERTa. Su utilidad principal es convertir texto en vectores que capturan su significado, lo que facilita tareas como búsqueda semántica, clustering, detección de paráfrasis o evaluación de similitud entre textos. Es sencilla de usar, eficiente y está optimizada para integrarse fácilmente con otras herramientas de IA.

***Instalacion:***

Descargue la imagen de python:

```
docker pull python:3.11-slim
```

Desde este directorio, genere la imagen con las bibliotecas definidas en el archivo ***requirements.txt***:

```
docker build -t python311_flask -f dockerfile .
```

Desde el directorio principal arranque el contenedor ***test_dbv***, definido en el ***docker-compose.yml***:

```
docker-compose up -d test_dbv
```

***Ejecución del ejemplo:***

Investigue el estado del contenedor y su Container_ID:

```
docker ps
```

Ejecute el codigo Python para almacenar datos asociados a peliculas en la base de datos vectorial Qdrant:

```
docker exec -it Container_ID bash -c "python pelis_to_qdrant.py"
```

Ejecute la consulta ***"pelicula sobre inteligencia artificial y robots"***:

```
docker exec -it Container_ID bash -c "python consulta_pelis_qdrant.py"
```

Espere el resultado:

```
Resultado: Ex Machina (puntaje: 0.751728)
Resultado: Jurassic Park (puntaje: 0.2623849)
Resultado: El Padrino (puntaje: 0.24137318)
```

El puntaje indica el grado de similitud entre el vector de consulta y los vectores almacenados. Puntaje alto (cercano a 1): el resultado es muy similar al texto buscado. Puntaje bajo (cercano a 0 o negativo): poca o ninguna similitud. 

El puntaje se calcula usando la métrica de similitud configurada (como coseno), donde valores más altos significan mayor cercanía semántica. Los resultados se ordenan de mayor a menor puntaje.



