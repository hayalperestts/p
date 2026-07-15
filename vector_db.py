import chromadb
from sentence_transformers import SentenceTransformer

# Model yükle
print("Model yükleniyor...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# ChromaDB başlat
client = chromadb.Client()
koleksiyon = client.create_collection("belgeler")

# Belgeler ekle
belgeler = [
    "Python programlama dili veri bilimi için kullanılır.",
    "Machine learning yapay zekanın bir dalıdır.",
    "FastAPI Python ile API geliştirmek için kullanılır.",
    "SQL veritabanı sorgulamak için kullanılır.",
    "Neural network insan beyninden ilham alır.",
    "Pandas veri analizi için güçlü bir kütüphanedir.",
]

print("Belgeler ekleniyor...")
koleksiyon.add(
    documents=belgeler,
    ids=[f"belge_{i}" for i in range(len(belgeler))]
)

# Arama yap
sorgu = "yapay zeka öğrenme"
print(f"\nSorgu: '{sorgu}'")

sonuclar = koleksiyon.query(
    query_texts=[sorgu],
    n_results=3
)

print("\n--- En Yakın Belgeler ---")
for i, belge in enumerate(sonuclar['documents'][0]):
    print(f"{i+1}. {belge}")