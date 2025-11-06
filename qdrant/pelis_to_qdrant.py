from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.models import VectorParams

# Inicializa el cliente de Qdrant
client = QdrantClient(url="http://10.13.0.6:6333", api_key="p4r4ng4r1cut1r1m1cu4r0")

# Carga un modelo de Sentence Transformers
model = SentenceTransformer("all-MiniLM-L6-v2")

# Nombre de la coleccion
collection_name = "peliculas"

# Tus datos de películas
peliculas = [
    {
        "título": "El Padrino",
        "género": "drama",
        "año": 1972,
        "director": "Francis Ford Coppola",
        "actores": ["Marlon Brando", "Al Pacino"],
        "sinopsis": "Un poderoso patriarca de la mafia italoamericana transfiere el control de su imperio criminal a su hijo reticente.",
        "idioma": "inglés",
        "país": "Estados Unidos",
        "calificación": "9.2"
    },
    {
        "título": "Toy Story",
        "género": "animación",
        "año": 1995,
        "director": "John Lasseter",
        "actores": ["Tom Hanks", "Tim Allen"],
        "sinopsis": "Un vaquero de juguete llamado Woody es celoso del nuevo juguete, Buzz Lightyear, hasta que ambos quedan atrapados en una gasolinera.",
        "idioma": "inglés",
        "país": "Estados Unidos",
        "calificación": "8.3"
    },
    {
        "título": "Jaws",
        "género": "aventura, thriller",
        "año": 1975,
        "director": "Steven Spielberg",
        "actores": ["Roy Scheider", "Robert Shaw"],
        "sinopsis": "Un gran tiburón blanco aterroriza a una comunidad costera durante la temporada turística.",
        "idioma": "inglés",
        "país": "Estados Unidos",
        "calificación": "8.0"
    },
    {
        "título": "Jurassic Park",
        "género": "acción, aventura, ciencia ficción",
        "año": 1993,
        "director": "Steven Spielberg",
        "actores": ["Sam Neill", "Laura Dern", "Jeff Goldblum"],
        "sinopsis": "Un parque temático con dinosaurios clonados sufre un colapso cuando los animales escapan de sus recintos.",
        "idioma": "inglés",
        "país": "Estados Unidos",
        "calificación": "8.1"
    },
    {
        "título": "Ex Machina",
        "género": "ciencia ficción, thriller",
        "año": 2014,
        "director": "Alex Garland",
        "actores": ["Alicia Vikander", "Domhnall Gleeson"],
        "sinopsis": "Un programador es invitado a evaluar la conciencia artificial de un robot femenino con inteligencia avanzada.",
        "idioma": "inglés",
        "país": "Reino Unido",
        "calificación": "7.7"
    }
]   

# Crear colección
client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=384, distance="Cosine")
)

# Genera embeddings y almacena en Qdrant
for i, peli in enumerate(peliculas):
    vector = model.encode(peli["sinopsis"]).tolist()  # Convierte texto a vector
    client.upsert(
        collection_name=collection_name,
        points=[
            {
                "id": i,
                "vector": vector,
                "payload": peli  # Incluye todos los datos originales
            }
        ]
    )   