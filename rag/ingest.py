import os
import chromadb

# Create folder if it doesn't exist
os.makedirs("chroma_db", exist_ok=True)

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="k8s_incidents"
)

with open(
    "knowledge_base/incidents.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()

documents = [
    doc.strip()
    for doc in content.split(
        "----------------------------------------------------"
    )
    if doc.strip()
]

for index, doc in enumerate(documents):

    collection.add(
        documents=[doc],
        ids=[f"incident_{index}"]
    )

print("Knowledge Base Ingested Successfully")