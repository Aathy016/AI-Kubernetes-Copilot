import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(
    name="k8s_incidents"
)


def search_incident(query):

    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    return results["documents"][0]