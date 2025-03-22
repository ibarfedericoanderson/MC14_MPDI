Ingresar al Streamlit Cloud en: https://mc14mpdi-iyltddrgc2nbeiftn44xv5.streamlit.app/ 

A continuación una descripción:

El script MC14_MPDI.py es una aplicación web interactiva desarrollada con Streamlit que permite visualizar y comparar dos metodologías estructuradas: el MC-14 (Método Científico de 14 etapas) y el MPDI (Metodología de Proyectos de Diseño Industrial), basándose en la norma ISO 5807:1985 para diagramas de flujo computacionales. Su objetivo principal es facilitar la comprensión de ambos procesos mediante representaciones gráficas interactivas, integrando descripciones detalladas de cada etapa y herramientas de visualización dinámica.

Funcionalidades clave:
Interfaz de usuario intuitiva:

Configuración inicial con título, autoría y enlaces académicos (Google Scholar, ORCID, ResearchGate) en un formato visualmente atractivo.

Selección de metodología mediante botones personalizados ("MC-14" o "MPDI").

Diagramas de flujo interactivos:

Utiliza Mermaid.js para renderizar diagramas que siguen la norma ISO 5807:1985, con nodos, conectores y símbolos estandarizados.

Elementos visuales diferenciados por colores y formas (rombos para decisiones, círculos para procesos, etc.).

Interactividad mediante tooltips: al hacer clic en cualquier nodo, se despliega una ventana emergente con una descripción técnica ampliada de la etapa seleccionada, extraída de los diccionarios mc14_descriptions y mpdi_descriptions.

Metodologías representadas:

MC-14: Abarca desde la observación inicial hasta la publicación y retroalimentación científica, incluyendo fases como revisión de literatura, diseño experimental y validación por pares.

MPDI: Enfocado en diseño industrial, con etapas como empatía con usuarios, prototipado 3D, evaluación técnica y lanzamiento al mercado.

Ambos diagramas permiten ciclos iterativos (ej: revisión de hipótesis o diseño).

Personalización visual:

Estilos CSS integrados para tooltips, barras de desplazamiento y animaciones (ej: indicador de desplazamiento pulsante).

Diseño responsivo con ventanas emergentes posicionadas dinámicamente y contenido adaptable a pantallas grandes.

Integración de contenidos académicos:

Vincula las etapas del Design Thinking con el método científico, tal como se discute en el documento .docx.

Incluye referencias a casos prácticos (ej: desarrollo de extractores de aire eficientes) mencionados en la investigación adjunta.

Tecnologías utilizadas:
Streamlit: Para el framework web y la gestión de estados de sesión.

Mermaid.js: Para la generación de diagramas de flujo ISO 5807.

HTML/CSS/JavaScript: Para personalizar tooltips, animaciones y estilos.

JSON: Para estructurar las descripciones de etapas y su vinculación con los nodos.

Propósito académico:
El script sirve como herramienta pedagógica para:

Visualizar procesos complejos de investigación (MC-14) y diseño industrial (MPDI) de manera accesible.

Promover la transparencia metodológica, alineándose con estándares internacionales.

Facilitar la comparación crítica entre enfoques científicos y prácticos, tal como se analiza en el documento adjunto sobre Design Thinking e I+D+i.

Limitaciones y mejoras potenciales:
Dependencia de Mermaid.js: Requiere conexión a internet para cargar la librería externa.

Responsividad: Los tooltips podrían optimizarse para dispositivos móviles.

Extensibilidad: Podría integrar exportación de diagramas en PDF/PNG o conexión a bases de datos para cargar casos de estudio dinámicos.

En síntesis, el script combina rigor académico, normativas técnicas y diseño centrado en el usuario para democratizar el acceso a metodologías estructuradas, reflejando la intersección entre ciencia, diseño e innovación propuesta en la investigación adjunta.

