import chromadb


class RAGEngine:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_collection(
            "k8s_incidents"
        )

    def search(
        self,
        query,
        n_results=3
    ):

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )

        print("\n===== RAG RESULTS =====")
        print(results)

        return results["documents"][0]