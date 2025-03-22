import streamlit as st
import streamlit.components.v1 as components
import json

# Configuración inicial de la página
st.set_page_config(page_title="MC-14 y MPDI", layout="wide")

# Información del autor (Texto en blanco)
st.markdown("""
<div style='background-color: #2D2D2D; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
    <h2 style='color: white;'>👤 Autor</h2>
    <p style='color: white;'>© 2025 <strong>Ibar Federico Anderson, Ph.D., Master, Industrial Designer</strong></p>
    <div style='display: flex; justify-content: space-between; margin-top: 10px;'>
        <div>
            <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" style="height: 20px; vertical-align: middle;"> <a href="https://scholar.google.com/citations?user=mXD4RFUAAAAJ&hl=en" target="_blank" style='color: white;'>Google Scholar</a></p>
            <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" style="height: 20px; vertical-align: middle;"> <a href="https://orcid.org/0000-0002-9732-3660" target="_blank" style='color: white;'>ORCID</a></p>
        </div>
        <div>
            <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/ResearchGate_icon_SVG.svg" style="height: 20px; vertical-align: middle;"> <a href="https://www.researchgate.net/profile/Ibar-Anderson" target="_blank" style='color: white;'>Research Gate</a></p>
            <p style='color: white;'><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="height: 20px; vertical-align: middle;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="height: 20px; vertical-align: middle;"> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" style='color: white;'>CC BY 4.0 License</a></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Título de la aplicación con ISO 5807:1985 (Texto en negro)
st.markdown("""
<h1 style='text-align: center; color: black;'>Selecciona una metodología</h1>
<p style='text-align: center; color: black; font-size: 18px;'>Los diagramas de flujo computacionales (Flowcharts) están basados en la norma <strong>ISO 5807:1985</strong>, que define las convenciones gráficas para representar procesos lógicos y estructuras de datos.</p>
""", unsafe_allow_html=True)

# Botones personalizados para seleccionar metodología
col1, col2 = st.columns(2)

with col1:
    if st.button("MC-14: Método Científico", key="mc14_button", help="Selecciona esta opción para ver el flujo del Método Científico"):
        st.session_state["selected_option"] = "MC-14: Método Científico"

with col2:
    if st.button("MPDI: Diseño Industrial", key="mpdi_button", help="Selecciona esta opción para ver el flujo del Diseño Industrial"):
        st.session_state["selected_option"] = "MPDI: Diseño Industrial"

# Descripciones ampliadas para MC-14
mc14_descriptions = {
    "🔍 Observación Curiosa": """
        La observación curiosa es el punto de partida del método científico. Consiste en identificar fenómenos o patrones inusuales que despierten interés investigativo. Este paso implica estar atento a detalles que otros podrían pasar por alto.
    """,
    "❓ Planteamiento del Problema": """
        El planteamiento del problema consiste en formular una pregunta clara y específica que guíe la investigación. Debe ser lo suficientemente precisa para permitir una solución práctica y relevante.
    """,
    "📚 📖 Revisión de Literatura": """
        La revisión de literatura implica explorar estudios previos, teorías y datos existentes relacionados con el problema. Este paso ayuda a contextualizar el problema dentro del conocimiento actual y evitar duplicaciones innecesarias.
    """,
    "💡 Hipótesis": """
        La hipótesis es una afirmación predictiva que intenta explicar el fenómeno observado. Debe ser comprobable mediante experimentos y debe proporcionar una base sólida para la investigación.
    """,
    "🔨 🔩 Diseño Experimental": """
        El diseño experimental incluye la planificación de métodos, herramientas y procedimientos para recolectar datos de manera sistemática. Este paso asegura que los resultados sean válidos y reproducibles.
    """,
    "📋 Recolección de Datos": """
        La recolección de datos implica ejecutar los métodos planificados para obtener información relevante. Este proceso debe ser riguroso y seguir protocolos establecidos para garantizar la calidad de los datos.
    """,
    "📈 📊 Análisis de Datos": """
        El análisis de datos incluye la interpretación estadística o cualitativa de los datos recolectados. Este paso busca identificar patrones, tendencias o relaciones significativas que respalden o refuten la hipótesis.
    """,
    "✅ Conclusión": """
        La conclusión evalúa si los resultados obtenidos apoyan la hipótesis inicial. Este paso también puede generar nuevas preguntas o ajustes en el marco teórico.
    """,
    "📂 Redacción del Informe": """
        La redacción del informe documenta formalmente todo el proceso de investigación, incluyendo objetivos, métodos, resultados y conclusiones. Es esencial para la comunicación científica.
    """,
    "👨 👩 Revisión por Pares": """
        La revisión por pares es un proceso crítico en el que expertos externos evalúan el informe para garantizar su rigor y validez. Este paso mejora la calidad y credibilidad del trabajo.
    """,
    "📂 📥 Publicación": """
        La publicación difunde los resultados en revistas científicas o conferencias especializadas. Este paso permite que otros investigadores accedan y construyan sobre el trabajo realizado.
    """,
    "♻️ Retroalimentación": """
        La retroalimentación genera nuevas preguntas, aplicaciones o mejoras en el proceso investigativo. Este ciclo continuo fomenta el avance del conocimiento científico.
    """,
    "🏁 Fin": """
        Representa el final del ciclo investigativo. Aquí se cierran los procesos y se prepara para posibles nuevas investigaciones basadas en los resultados obtenidos.
    """,
    "📌 Revisión de Hipótesis": """
        En caso de que la hipótesis no sea comprobada, este paso permite reformularla o ajustarla según los datos recolectados, para intentar nuevamente su validación.
    """,
}

# Descripciones ampliadas para MPDI
mpdi_descriptions = {
    "🏠 Empatizar y Contextualizar": """
        La empatía implica comprender profundamente las necesidades, deseos y limitaciones de los usuarios finales. Este paso también incluye analizar el contexto social, cultural y ambiental donde se utilizará el producto.
    """,
    "❓ Definir el Problema": """
        Definir el problema consiste en identificar claramente qué necesidad o desafío se intenta resolver. Este paso debe ser específico y centrarse en los usuarios y sus interacciones con el entorno.
    """,
    "👨‍💻 💾 📲 🔗 Investigación Web y DeepSearch": """
        La investigación web incluye buscar tendencias actuales, materiales innovadores y casos similares. Esta etapa utiliza herramientas digitales avanzadas para recopilar información relevante.
    """,
    "💡 ✨ Ideación y Conceptualización": """
        La ideación es un proceso creativo que genera múltiples soluciones potenciales al problema. Se utilizan técnicas como brainstorming, mapas mentales y prototipado rápido para explorar ideas.
    """,
    "✏️ 📝 🎨 📐 Bocetos, Render 2D y Prototipos 3D": """
        Los bocetos y prototipos iniciales permiten visualizar y explorar formas, funciones y usabilidad. Este paso es clave para materializar ideas abstractas en conceptos tangibles.
    """,
    "⚖️ 🔧 Evaluación Técnica": """
        La evaluación técnica analiza la viabilidad del diseño desde perspectivas técnicas, económicas y de usabilidad. Este paso asegura que el producto sea funcional, seguro y rentable.
    """,
    "⚙️ Iteración y Refinamiento": """
        La iteración implica mejorar el diseño basado en pruebas y retroalimentación. Este proceso cíclico garantiza que el producto final sea óptimo y cumpla con las expectativas del usuario.
    """,
    "📑 Documentación Técnica": """
        La documentación técnica incluye especificaciones detalladas, planos y manuales de uso. Este paso es esencial para la producción y mantenimiento del producto.
    """,
    "👤 Validación con Usuarios": """
        La validación con usuarios prueba el producto en contextos reales para verificar su funcionalidad, estética, ergonomía y aceptación. Este paso asegura que el diseño satisfaga las necesidades del usuario.
    """,
    "🏭 🔩 Producción y Fabricación": """
        La producción y fabricación consiste en la implementación del diseño en un entorno industrial. Este paso incluye la selección de materiales, herramientas y procesos para crear el producto final.
    """,
    "🚀 Lanzamiento": """
        El lanzamiento implica la introducción del producto al mercado. Este paso incluye estrategias de marketing, distribución y soporte técnico para asegurar una adopción exitosa.
    """,
    "📢 👪 👤 Comunicación y Marketing para Usuarios": """
        La comunicación y marketing para usuarios se enfoca en promover el producto y generar interés entre los consumidores. Este paso incluye campañas publicitarias, redes sociales y eventos.
    """,
    "🎯 Fin": """
        Marca la conclusión del proceso de diseño industrial. Aquí se evalúa el éxito general del producto y se consideran futuras iteraciones o mejoras.
    """,
    "🔄 Revisión de Diseño": """
        Cuando un diseño no es aprobado en la fase de documentación, este paso permite regresar a la etapa de bocetos para hacer ajustes y mejoras sustanciales.
    """,
}

# Diagramas de flujo en Mermaid con flechas más largas y negras
mc14_diagram = """
%%{init: {'theme': 'base', 'themeVariables': { 'fontFamily': 'arial', 'fontSize': '20px' }}}%%
flowchart TD
    A([🔍 Observación Curiosa]) -->|" "| B[❓ Planteamiento del Problema]
    B -->|" "| C[/📚 📖 Revisión de Literatura/]
    C -->|" "| D{💡 Hipótesis}
    D -->|"Formulación"| E[🔨 🔩 Diseño Experimental]
    E -->|" "| F([📋 Recolección de Datos])
    F -->|" "| G[[📈 📊 Análisis de Datos]]
    G -->|" "| H{ ✅ Conclusión}
    H -->|"👍 Apoya Hipótesis"| I[/📂 Redacción del Informe/]
    H -->|"👎 ❌ No Apoya"| J[[📌 Revisión de Hipótesis]]
    J -->|" "| E
    I -->|" "| K((👨 👩 Revisión por Pares))
    K -->|" "| L[(📂 📥 Publicación)]
    L -->|" "| M([♻️ Retroalimentación])
    M -->|"Nuevas Preguntas"| A
    M -->|"🏁 Fin del Proceso"| N([🏁 Fin])

    classDef default fill:#3498db,stroke:#2980b9,color:white,stroke-width:2px
    classDef round fill:#e74c3c,stroke:#c0392b,color:white,cursor:pointer
    classDef diamond fill:#2ecc71,stroke:#27ae60,color:white,cursor:pointer
    classDef parallel fill:#9b59b6,stroke:#8e44ad,color:white,cursor:pointer
    classDef circle fill:#f1c40f,stroke:#f39c12,color:white,cursor:pointer
    classDef database fill:#1abc9c,stroke:#16a085,color:white,cursor:pointer

    linkStyle default stroke:#000000,stroke-width:3px

    class A,F,M,N round
    class D,H diamond
    class G,J parallel
    class K circle
    class L database
"""

mpdi_diagram = """
%%{init: {'theme': 'base', 'themeVariables': { 'fontFamily': 'arial', 'fontSize': '20px' }}}%%
flowchart TD
    A([🏠 Empatizar y Contextualizar]) -->|" "| B[/❓ Definir el Problema/]
    B -->|" "| C[/👨‍💻 💾 📲 🔗 Investigación Web y DeepSearch/]
    C -->|" "| D{💡 ✨ Ideación y Conceptualización}
    D -->|"Generación"| E[✏️ 📝 🎨 📐 Bocetos, Render 2D y Prototipos 3D]
    E -->|" "| F([⚖️ 🔧 Evaluación Técnica])
    F -->|" "| G[[⚙️ Iteración y Refinamiento]]
    G -->|" "| H{📑 Documentación Técnica}
    H -->|"📄 Documentación"| I[/👤 Validación con Usuarios/]
    H -->|"👎 No Aprobado ❌"| J[[🔄 Revisión de Diseño]]
    J -->|" "| E
    I -->|" "| K((🏭 🔩 Producción y Fabricación))
    K -->|" "| L[(🚀 Lanzamiento)]
    L -->|" "| M([📢 👪 👤 Comunicación y Marketing para Usuarios])
    M -->|"Nuevas Mejoras"| A
    M -->|"🎯 Fin del Proceso"| N([🎯 Fin])

    classDef default fill:#3498db,stroke:#2980b9,color:white,stroke-width:2px
    classDef round fill:#e74c3c,stroke:#c0392b,color:white,cursor:pointer
    classDef diamond fill:#2ecc71,stroke:#27ae60,color:white,cursor:pointer
    classDef parallel fill:#9b59b6,stroke:#8e44ad,color:white,cursor:pointer
    classDef circle fill:#f1c40f,stroke:#f39c12,color:white,cursor:pointer
    classDef database fill:#1abc9c,stroke:#16a085,color:white,cursor:pointer

    linkStyle default stroke:#000000,stroke-width:3px

    class A,F,M,N round
    class D,H diamond
    class G,J parallel
    class K circle
    class L database
"""

def render_mermaid(diagram, descriptions):
    # Preparar las descripciones para JavaScript
    descriptions_json = json.dumps({k: v.strip() for k, v in descriptions.items()})
    
    # HTML con espacio adicional y tooltips fijos
    html = f"""
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <div style="padding-bottom: 400px;">
        <div class="mermaid">
            {diagram}
        </div>
    </div>
    
    <div id="tooltip-box" style="display: none; position: fixed; bottom: 40px; left: 50%; transform: translateX(-50%); 
                                width: 90%; max-width: 1200px; background-color: #34495e; color: white; 
                                padding: 35px; border-radius: 15px; box-shadow: 0 0 30px rgba(0,0,0,0.6); z-index: 1000;">
        <h3 id="tooltip-title" style="margin-top: 0; border-bottom: 2px solid #fff; padding-bottom: 15px; font-size: 32px; font-weight: bold;"></h3>
        <p id="tooltip-text" style="margin: 20px 0 0 0; font-size: 24px; line-height: 1.7;"></p>
    </div>
    
    <div id="scroll-indicator" style="position: fixed; right: 20px; bottom: 80px; 
                                      background-color: rgba(52, 73, 94, 0.8); color: white; padding: 10px; 
                                      border-radius: 8px; animation: pulse 2s infinite;">
        ⬇️ Desliza para ver más contenido
    </div>
    
    <style>
        @keyframes pulse {{
            0% {{ opacity: 0.7; }}
            50% {{ opacity: 1; }}
            100% {{ opacity: 0.7; }}
        }}
        
        /* Personalización de la barra de desplazamiento */
        ::-webkit-scrollbar {{
            width: 12px;
            height: 12px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: #f1f1f1;
            border-radius: 10px;
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: #3498db;
            border-radius: 10px;
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
            background: #2980b9;
        }}
    </style>
    
    <script>
        // Inicializar Mermaid
        mermaid.initialize({{ startOnLoad: true }});
        
        // Esperar a que el DOM esté listo
        document.addEventListener('DOMContentLoaded', function() {{
            // Dar tiempo para que Mermaid renderice completamente
            setTimeout(function() {{
                // Referencias a elementos del DOM
                const tooltipBox = document.getElementById('tooltip-box');
                const tooltipTitle = document.getElementById('tooltip-title');
                const tooltipText = document.getElementById('tooltip-text');
                const scrollIndicator = document.getElementById('scroll-indicator');
                
                // Descripciones de los nodos
                const descriptions = {descriptions_json};
                
                // Función para manejar clics en nodos
                function handleNodeClick(event) {{
                    // Obtener el texto del nodo
                    const nodeText = event.currentTarget.textContent.trim();
                    
                    // Si hay una descripción para este nodo
                    if (descriptions[nodeText]) {{
                        // Mostrar tooltip con la descripción
                        tooltipTitle.textContent = nodeText;
                        tooltipText.textContent = descriptions[nodeText].trim();
                        tooltipBox.style.display = 'block';
                        
                        // Detener propagación para evitar cierre inmediato
                        event.stopPropagation();
                    }}
                }}
                
                // Agregar interactividad a todos los elementos del diagrama
                setTimeout(function() {{
                    // Obtener todos los nodos y elementos interactivos
                    const allNodes = document.querySelectorAll('.node, .cluster');
                    
                    // Hacer cada elemento interactivo
                    allNodes.forEach(function(node) {{
                        node.style.cursor = 'pointer';
                        node.addEventListener('click', handleNodeClick);
                    }});
                    
                    // Obtener específicamente elementos dentro del diagrama
                    document.querySelectorAll('g.node text, g.cluster text').forEach(function(textElement) {{
                        textElement.addEventListener('click', function(e) {{
                            const nodeText = e.target.textContent.trim();
                            if (descriptions[nodeText]) {{
                                tooltipTitle.textContent = nodeText;
                                tooltipText.textContent = descriptions[nodeText].trim();
                                tooltipBox.style.display = 'block';
                                e.stopPropagation();
                            }}
                        }});
                    }});
                }}, 1000);
                
                // Cerrar tooltip al hacer clic fuera de los nodos
                document.addEventListener('click', function(e) {{
                    if (!e.target.closest('.node') && !e.target.closest('.cluster')) {{
                        tooltipBox.style.display = 'none';
                    }}
                }});
                
                // Ocultar indicador de desplazamiento después de un tiempo
                setTimeout(function() {{
                    scrollIndicator.style.display = 'none';
                }}, 8000); // 8 segundos
            }}, 1500);
        }});
    </script>
    """
    
    # Renderizar el HTML
    components.html(html, height=800, scrolling=True)

# Instrucciones para el usuario
st.markdown("""
<div style="background-color: #f0f0f0; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
    <p style="margin: 0; text-align: center;"><strong>Instrucciones:</strong> Haz clic en cualquier nodo del diagrama para ver su descripción detallada.</p>
</div>
""", unsafe_allow_html=True)

# Por defecto, mostrar MC-14 si no hay selección
if "selected_option" not in st.session_state:
    st.session_state["selected_option"] = "MC-14: Método Científico"

# Mostrar el título del diagrama seleccionado
st.markdown(f"<h2 style='text-align: center; color: black;'>{st.session_state['selected_option']}</h2>", unsafe_allow_html=True)

# Renderizar el diagrama seleccionado
if st.session_state["selected_option"] == "MC-14: Método Científico":
    render_mermaid(mc14_diagram, mc14_descriptions)
else:
    render_mermaid(mpdi_diagram, mpdi_descriptions)

# Espacio extra al final para tooltips
st.markdown("<div style='height: 300px;'></div>", unsafe_allow_html=True)

# Nota de copyright
st.markdown("""
<div style='text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ccc;'>
    <p style='color: gray; font-size: 12px;'>© 2025 Ibar Federico Anderson. Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)