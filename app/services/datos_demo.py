"""Datos de ejemplo para el prototipo navegable (fase 2).
En la fase 3 estos datos saldrán de la base de datos."""


def unsplash(foto_id, ancho=600, alto=400):
    """Devuelve la URL de una foto de ejemplo de Unsplash."""
    return f"https://images.unsplash.com/{foto_id}?w={ancho}&h={alto}&fit=crop&auto=format"


PROYECTOS = [
    {"id": 1, "nombre": "SistemaSalud360", "anio": 2022, "tecnologias": ["React", "Node.js", "PostgreSQL", "Docker"],
     "imagen": "photo-1576091160399-112ba8d25d1d",
     "desc": "Sistema integral de gestión hospitalaria que optimiza el flujo de pacientes, inventario médico y agendamiento de citas. Implementado en 3 clínicas piloto con reducción del 40% en tiempos de espera.",
     "integrantes": ["Carlos Ruiz", "Andrea Mora", "Luis Pérez"], "asesor": "Dr. Ricardo Leal",
     "evidencias": ["Documento técnico", "Video demo", "Repositorio GitHub"]},
    {"id": 2, "nombre": "EcoTracker", "anio": 2025, "tecnologias": ["Flutter", "Firebase", "ML Kit", "Python"],
     "imagen": "photo-1441974231531-c6227db76b6e",
     "desc": "Aplicación móvil para el cálculo y seguimiento de huella de carbono personal. Usa modelos de ML para sugerir acciones de compensación y conecta con iniciativas ambientales locales.",
     "integrantes": ["Felipe Castro", "Natalia Suárez", "Diego Moreno"], "asesor": "Dra. Carmen Vidal",
     "evidencias": ["APK demo", "Informe de impacto", "Prototipo Figma"]},
    {"id": 3, "nombre": "CampusConnect", "anio": 2023, "tecnologias": ["Vue.js", "Django", "Redis", "AWS"],
     "imagen": "photo-1522202176988-66273c2fd55f",
     "desc": "Plataforma de comunidad universitaria que centraliza novedades, servicios académicos, oferta laboral y eventos del campus. Actualmente con más de 2.000 usuarios activos.",
     "integrantes": ["María Torres", "Juan Cárdenas", "Sara Molina"], "asesor": "Mg. Alberto Quintero",
     "evidencias": ["Plataforma en vivo", "Manual de usuario"]},
    {"id": 4, "nombre": "CyberShield IDS", "anio": 2024, "tecnologias": ["Python", "TensorFlow", "Scapy", "Elasticsearch"],
     "imagen": "photo-1563986768609-322da13575f3",
     "desc": "Sistema de detección de intrusiones basado en redes neuronales recurrentes. Detecta ataques DDoS, SQL Injection y anomalías de red con 97.3% de precisión en entornos de prueba.",
     "integrantes": ["Andrés Gómez", "Valentina Ríos"], "asesor": "Dr. Pablo Muñoz",
     "evidencias": ["Paper IEEE", "Dataset público", "Código fuente"]},
    {"id": 5, "nombre": "AgriSmart", "anio": 2023, "tecnologias": ["IoT", "LoRaWAN", "React Native", "MongoDB"],
     "imagen": "photo-1574943320219-553eb213f72d",
     "desc": "Sistema de agricultura de precisión con sensores IoT para monitoreo de humedad, temperatura y nutrientes del suelo. Piloto en 5 fincas de la región con incremento del 30% en rendimiento.",
     "integrantes": ["Roberto Silva", "Paola Jiménez", "Camilo Torres"], "asesor": "Dr. Ricardo Leal",
     "evidencias": ["Informe técnico", "Prototipo físico", "Dashboard en vivo"]},
    {"id": 6, "nombre": "LexIA", "anio": 2024, "tecnologias": ["NLP", "Python", "FastAPI", "React"],
     "imagen": "photo-1589578228447-e1a4e481c6c8",
     "desc": "Asistente de IA para análisis y comprensión de documentos jurídicos. Automatiza la extracción de cláusulas clave, riesgos y obligaciones en contratos en menos de 30 segundos.",
     "integrantes": ["Sofía Vargas", "Mateo Herrera"], "asesor": "Dra. Carmen Vidal",
     "evidencias": ["Demo interactiva", "Informe de validación"]},
]

HALL_FAMA = [
    {"id": 1, "nombre": "Dr. Ricardo Leal", "categoria": "Docente Destacado", "foto": "photo-1507003211169-0a1dd7228f2d",
     "bio": "Doctor en Ciencias de la Computación por la Universidad de los Andes. Líder del grupo DataSIS, con 15 publicaciones en revistas Q1. Reconocido como Mejor Docente 2022 y 2023.",
     "logros": ["Mejor Docente 2022 y 2023", "15 publicaciones Scopus", "Líder Semillero DataSIS", "Premio COLCIENCIAS 2022"]},
    {"id": 2, "nombre": "Dra. Carmen Vidal", "categoria": "Docente Destacado", "foto": "photo-1573496359142-b8d87734a5a2",
     "bio": "Doctora en Ingeniería de Sistemas por la Universidad Nacional. Especialista en IoT y sistemas embebidos. Directora del laboratorio de innovación tecnológica.",
     "logros": ["Patente SPI-2023-007", "Premio mujer en STEM 2024", "Directora Lab. Innovación", "Ponente en 8 conferencias internacionales"]},
    {"id": 3, "nombre": "Carlos Andrés Ruiz", "categoria": "Egresado Destacado", "foto": "photo-1500648767791-00dcc994a43e",
     "bio": "Egresado cohorte 2022. Cofundador de HealthTech SAS, startup valorada en $2M USD. Líder del proyecto SistemaSalud360 ganador del Premio Nacional de Innovación.",
     "logros": ["Premio Nacional de Innovación 2022", "Fundador de HealthTech SAS", "Seleccionado Endeavor 2024", "Forbes Under 30 Colombia 2025"]},
    {"id": 4, "nombre": "Sofía Vargas Mejía", "categoria": "Estudiante Destacada", "foto": "photo-1494790108377-be9c29b29330",
     "bio": "Estudiante de 9° semestre con promedio de 4.8/5.0. Su proyecto de grado sobre ML para predicción de deserción estudiantil obtuvo distinción Laureada.",
     "logros": ["Promedio 4.8/5.0", "Distinción Laureada de Grado", "Mejor Trabajo CLEI 2024", "Becaria Colciencias Joven"]},
    {"id": 5, "nombre": "Mg. Alberto Quintero", "categoria": "Docente Destacado", "foto": "photo-1472099645785-5658abf4ff4e",
     "bio": "Magíster en Ingeniería de Software por la Universidad Javeriana. Docente con 10 años de experiencia, coordinador del programa de proyección social.",
     "logros": ["10 años de docencia", "Coordinador Proyección Social", "Guía 4 proyectos premiados", "Certificación AWS Solutions Architect"]},
    {"id": 6, "nombre": "Felipe Castro Mora", "categoria": "Egresado Destacado", "foto": "photo-1519085360753-af0119f7cbe7",
     "bio": "Egresado 2024, actualmente Software Engineer en Globant. Lideró el proyecto EcoTracker que ganó 2do lugar en App Challenge Colombia 2025.",
     "logros": ["Software Engineer en Globant", "2do lugar App Challenge 2025", "Speaker PyCon Colombia 2025", "Contribuidor Open Source activo"]},
    {"id": 7, "nombre": "Valentina Ríos Castro", "categoria": "Estudiante Destacada", "foto": "photo-1438761681033-6461ffad8d80",
     "bio": "Estudiante de 8° semestre, investigadora del semillero CyberLab. Co-autora de paper en IEEE sobre detección de intrusiones con redes neuronales.",
     "logros": ["Co-autora IEEE 2024", "Investigadora CyberLab", "Monitora académica 3 semestres", "Beca de honor 2023-2024"]},
    {"id": 8, "nombre": "Dr. Pablo Muñoz", "categoria": "Docente Destacado", "foto": "photo-1560250097-0b93528c311a",
     "bio": "Doctor en Ciberseguridad por la Universidad Politécnica de Madrid. Consultor para el MINTIC y director del semillero CyberLab.",
     "logros": ["2 publicaciones ACM/Springer", "Consultor MINTIC", "Líder CyberLab", "Certificación CEH Master"]},
]


def buscar(lista, id_):
    """Devuelve el elemento de la lista cuyo 'id' coincide, o None."""
    return next((x for x in lista if x["id"] == id_), None)


LINEA_TIEMPO = [
    {"id": 1, "anio": 2019, "titulo": "Fundación del Programa", "fecha": "15 Feb 2019", "img": "photo-1562774053-701939374585",
     "desc": "Se crea oficialmente el Programa de Ingeniería de Sistemas con 40 estudiantes en la primera cohorte."},
    {"id": 2, "anio": 2020, "titulo": "Primer Laboratorio de Innovación", "fecha": "20 Mar 2020", "img": "photo-1518770660439-4636190af475",
     "desc": "Inauguración del Laboratorio de Innovación Tecnológica con equipos de última generación."},
    {"id": 3, "anio": 2021, "titulo": "Acreditación de Alta Calidad", "fecha": "08 Jun 2021", "img": "photo-1523050854058-8df90110c9f1",
     "desc": "El programa obtiene la acreditación de Alta Calidad por el Ministerio de Educación, reconociendo su excelencia académica."},
    {"id": 4, "anio": 2022, "titulo": "Premio Nacional de Innovación", "fecha": "22 Oct 2022", "img": "photo-1567427017947-545c5f8d16ad",
     "desc": "Estudiantes del programa ganan el Premio Nacional de Innovación con el proyecto SistemaSalud360."},
    {"id": 5, "anio": 2023, "titulo": "Semillero de Investigación IA", "fecha": "10 Mar 2023", "img": "photo-1507003211169-0a1dd7228f2d",
     "desc": "Creación del primer semillero de investigación en Inteligencia Artificial con 18 estudiantes activos."},
    {"id": 6, "anio": 2024, "titulo": "Publicación en Revista Scopus", "fecha": "05 Sep 2024", "img": "photo-1456513080510-7bf3a84b82f8",
     "desc": "El grupo de investigación DataSIS publica su primer artículo en una revista indexada en Scopus Q1."},
    {"id": 7, "anio": 2025, "titulo": "Convenio Internacional MIT", "fecha": "14 Jan 2025", "img": "photo-1524178232363-1fb2b075b655",
     "desc": "Firma de convenio con el MIT Media Lab para intercambio estudiantil y proyectos de investigación conjunta."},
]

GALERIA_HISTORIA = [
    "photo-1562774053-701939374585", "photo-1518770660439-4636190af475", "photo-1523050854058-8df90110c9f1",
    "photo-1540575467063-178a50c2df87", "photo-1475721027785-f74eccf877e2", "photo-1558618666-fcd25c85cd64",
    "photo-1529156069898-49953e39b3ac", "photo-1524178232363-1fb2b075b655",
]

GALERIA_EVENTO = ["photo-1540575467063-178a50c2df87", "photo-1475721027785-f74eccf877e2", "photo-1558618666-fcd25c85cd64"]

PREMIOS = [
    {"id": 1, "nombre": "Premio Nacional de Innovación Tecnológica", "anio": 2022, "lugar": "1er Lugar Nacional",
     "participantes": ["Carlos Ruiz", "Andrea Mora", "Luis Pérez"], "imagen": "photo-1567427017947-545c5f8d16ad", "categoria": "Innovación",
     "desc": "Reconocimiento otorgado por COLCIENCIAS al proyecto SistemaSalud360, solución de gestión hospitalaria integral."},
    {"id": 2, "nombre": "Hackathon Empresarial FinTech Colombia", "anio": 2023, "lugar": "1er Lugar Regional",
     "participantes": ["María Torres", "Juan Cárdenas"], "imagen": "photo-1551836022-4c4c79ecde51", "categoria": "Hackathon",
     "desc": "Primer lugar en el hackathon organizado por Bancolombia con la solución de pagos descentralizados."},
    {"id": 3, "nombre": "Mejor Proyecto de Grado", "anio": 2023, "lugar": "Distinción Laureada",
     "participantes": ["Sofía Vargas"], "imagen": "photo-1523240795612-9a054b0db644", "categoria": "Académico",
     "desc": "Tesis sobre modelos de machine learning aplicados a predicción de deserción estudiantil universitaria."},
    {"id": 4, "nombre": "IEEE Student Paper Contest", "anio": 2024, "lugar": "3er Lugar Internacional",
     "participantes": ["Andrés Gómez", "Valentina Ríos"], "imagen": "photo-1434030216411-0b793f4b4173", "categoria": "Investigación",
     "desc": "Reconocimiento de IEEE por el artículo sobre redes neuronales para detección de ciberataques en tiempo real."},
    {"id": 5, "nombre": "Premio a la Investigación Universitaria", "anio": 2024, "lugar": "Mejor Grupo Emergente",
     "participantes": ["Dr. Ricardo Leal", "Semillero DataSIS"], "imagen": "photo-1481627834876-b7833e8f5570", "categoria": "Investigación",
     "desc": "Reconocimiento institucional al Semillero DataSIS por sus contribuciones al análisis de datos educativos."},
    {"id": 6, "nombre": "App Challenge Colombia 2025", "anio": 2025, "lugar": "2do Lugar Nacional",
     "participantes": ["Felipe Castro", "Natalia Suárez", "Diego Moreno"], "imagen": "photo-1512941937669-90a1b58e7e9c", "categoria": "Desarrollo",
     "desc": "Segunda posición en el reto nacional de desarrollo de aplicaciones móviles con EcoTracker, app de huella de carbono."},
]

INVESTIGACION = [
    {"id": 1, "nombre": "DataSIS", "linea": "Ciencia de Datos e Inteligencia Artificial", "lider": "Dr. Ricardo Leal", "integrantes": 12,
     "publicaciones": ["Predicción de deserción universitaria con ML (Scopus Q1, 2024)", "Análisis de sentimientos en redes sociales académicas (IEEE, 2023)"],
     "patentes": ["Software de análisis predictivo educativo – SPI-2024-001"], "software": ["DataEdu v2.0 (registro DNDA)", "SentimentAcademic API"]},
    {"id": 2, "nombre": "CyberLab", "linea": "Ciberseguridad y Redes", "lider": "Dr. Pablo Muñoz", "integrantes": 8,
     "publicaciones": ["IDS basado en LSTM para detección de DDoS (ACM, 2024)", "Análisis de vulnerabilidades en infraestructuras críticas (Springer, 2023)"],
     "patentes": [], "software": ["CyberShield IDS v1.3", "VulnScanner CLI"]},
    {"id": 3, "nombre": "IoT-Sistemas", "linea": "Internet de las Cosas y Sistemas Embebidos", "lider": "Dra. Carmen Vidal", "integrantes": 10,
     "publicaciones": ["Arquitecturas LoRaWAN para agricultura de precisión (Elsevier, 2023)"],
     "patentes": ["Sistema de monitoreo agro-inteligente – SPI-2023-007"], "software": ["AgriSmart Platform", "SensorHub Firmware"]},
    {"id": 4, "nombre": "SoftEng", "linea": "Ingeniería de Software y Calidad", "lider": "Mg. Alberto Quintero", "integrantes": 6,
     "publicaciones": ["Métricas de calidad en proyectos ágiles universitarios (CLEI, 2024)"],
     "patentes": [], "software": ["QualityMeter Dashboard", "AgileTrack v1.0"]},
]

EVENTOS = [
    {"id": 1, "nombre": "VII Semana de la Ingeniería 2025", "fecha": "2025-10-15", "lugar": "Auditorio Principal – Bloque A", "tipo": "proximo",
     "desc": "Semana académica con conferencias, talleres y feria de proyectos. Contará con ponentes de Google, Microsoft y empresas nacionales."},
    {"id": 2, "nombre": "Hackathon INNOVATECH 2025", "fecha": "2025-11-08", "lugar": "Laboratorio de Innovación – Sala 301", "tipo": "proximo",
     "desc": "Maratón de programación de 36 horas continuas. Tema: soluciones tecnológicas para la salud. Premios en efectivo y mentoría empresarial."},
    {"id": 3, "nombre": "Conferencia: IA Generativa en la Industria", "fecha": "2025-09-05", "lugar": "Auditorio Virtual – Zoom", "tipo": "proximo",
     "desc": "Conferencia magistral con expertos de OpenAI y el MIT sobre el impacto de la IA generativa en los sectores productivos de Latinoamérica."},
    {"id": 4, "nombre": "VI Semana de la Ingeniería 2024", "fecha": "2024-10-18", "lugar": "Auditorio Principal – Bloque A", "tipo": "realizado",
     "desc": "Exitosa edición con más de 800 asistentes, 12 ponentes nacionales e internacionales y exposición de 30 proyectos estudiantiles."},
    {"id": 5, "nombre": "Taller: DevOps y Cloud Computing", "fecha": "2024-08-22", "lugar": "Sala de Cómputo 204", "tipo": "realizado",
     "desc": "Taller intensivo de 16 horas sobre prácticas DevOps, CI/CD con GitHub Actions y despliegue en AWS. Certificado por Amazon Web Services."},
    {"id": 6, "nombre": "Feria de Empleo TechCareers 2024", "fecha": "2024-05-10", "lugar": "Patio Central del Campus", "tipo": "realizado",
     "desc": "Feria de empleo con participación de 25 empresas del sector TI. Más de 150 estudiantes conectados con oportunidades laborales y de práctica."},
]
