import faiss
import numpy as np

from retrieval.vector_store import (
    load_knowledge,
    build_embeddings
)



def build_index():

    vectors = build_embeddings()

    vectors = np.array(
        vectors,
        dtype="float32"
    )

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    return index