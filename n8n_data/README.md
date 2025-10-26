## Inicio de n8n y licencia

### INICIO

El servidor ***N8N*** esta en la dirección ***http://localhost:5678***

Cuando se entra por primera vez, aperece un formulario donde se solicita una direccion de correo valida y algunos datos adicionales incluida una contraseña. En esa dirección de correo llegará la llave para la licencia de N8N.

### ACTIVACION DE LA LICENCIA

En el ambiente de trabajo de ***N8N***, abajo a la izquierda, donde aparece el ***nombre del usuario*** está el menu ***...***, tome la opción ***Settings*** y posteriormente presione el botón ***Enter activation key***, digite la licencia que llego a su correo y acepte para completar el proceso de configuración.

### SOBRE N8N

Crear ***Workflows*** es muy sencillo, existen muchos video tutoriales en la red que puedes consultar.

Algunas de mis plantillas -***Workflows***- son muy sencillas, las de nodo unico sirven para ilustrar como debe configurarse y usarse un nodo dentro de una red de contenedores.

Otros ***Workflow*** son mas elaboradas y representan soluciones a problemas reales.

Lo que más me entusiasma de ***N8N*** no son los ***agentes de IA***, es su facilidad de integración con WhatsApp, Telegram, PostgreSql y la Suite de Google (Gmail, Drive, Hojas de cálculo, Documentos, Calendario, Contactos ...)

Mis soluciones se basan en scripts de Python y no soy hábil para desarrollar interfaces -***FrontEnd***-, entonces ***N8N*** me facilita esa tarea.

Recibo mensajes o correos con datos adjuntos que desencadenan la ejecución de una solución y dan la respuesta, ***por supuesto en modo desatendido***.

Inclusive ***N8N*** me brinda la posibilidad de generar formularios ***dinámicos*** para el ingreso de datos. El nodo ***Form*** tiene la opción de definir sus elementos con código ***JSON***, esto abre la posibilidad de construir formularios basados en datos previos.

### DETERMINISMO E IA

El determinismo en computación se refiere a que, dadas unas mismas entradas y condiciones iniciales, un algoritmo o sistema siempre producirá la misma salida y seguirá la misma secuencia de estados durante su ejecución. Es decir, su comportamiento es completamente predecible.

Muchas soluciones de IA son no deterministas, esto significa que ante la misma entrada pueden producir respuestas ligeramente diferentes en distintas ejecuciones. Aunque su naturaleza es probabilistica algunas aplicaciones de IA pueden ser deterministas, especialmente cuando:

- Se usan algoritmos clásicos (reglas lógicas).
- Se combinan modelos de IA con sistemas deterministas (recuperación de datos exactos, generación de consultas SQL o llamado a servicios API REST).

***N8N*** es una herramienta determinista por naturaleza (mismas entradas -> mismas salidas), entonces en ***N8N*** debes delegar a los agentes de IA tareas que requieran razonamiento, comprensión del lenguaje o toma de decisiones. 

Las tareas más adecuadas para IA incluyen:

- Procesamiento de lenguaje natural
- Generación de contenido
- Clasificación de datos
- **Extracción** de datos en documentos no estructurados
- Descomposición de tareas complejas
- Busqueda y sintesis de información

Toma esto en cuenta durante el aprendizaje de esta magnifica herramienta.









