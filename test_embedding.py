from app.services.embedding_service import EmbeddingService

text = "Python is an interpreted programming language."

embedding = EmbeddingService.generate_embedding(text)

print("Embedding generated successfully!")
print("Embedding Dimension:", len(embedding))
print("First 10 values:")
print(embedding[:10])