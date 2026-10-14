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
