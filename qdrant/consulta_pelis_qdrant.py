from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# Inicializa el cliente de Qdrant
client = QdrantClient(url="http://10.13.0.6:6333", api_key="p4r4ng4r1cut1r1m1cu4r0")

# Carga un modelo de Sentence Transformers
model = SentenceTransformer("all-MiniLM-L6-v2")

# Nombre de la coleccion
collection_name = "peliculas"


# Genera el vector de la consulta
query_vector = model.encode("pelicula sobre inteligencia artificial y robots").tolist()

# Realiza la búsqueda
results = client.query_points(
    collection_name="peliculas",
    query=query_vector,  # Vector de consulta
    limit=3,
    with_payload=True
)

# Muestra resultados
for result in results.points:
    print(f"Resultado: {result.payload['título']} (puntaje: {result.score})")   