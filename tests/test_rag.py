import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag.rag_engine import RAGEngine

rag = RAGEngine()

results = rag.search(
    "ImagePullBackOff"
)

print("\n===== RAG RESULTS =====\n")

for doc in results:
    print(doc)
    print("-" * 50)