import faiss
import numpy as np

from retrieval.embedding import create_embedding
from utils.helper import load_knowledge
from nlp.preprocessing import extract_keywords

knowledge = load_knowledge()

embeddings = []

for item in knowledge:

    processed_question = extract_keywords(
        item["question"]
    )

    embeddings.append(
        create_embedding(processed_question)
    )
print()
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)


def search(query, top_k=3):

    processed_query = extract_keywords(query)

    query_embedding = create_embedding(processed_query)

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:

        results.append(knowledge[idx])

    return results