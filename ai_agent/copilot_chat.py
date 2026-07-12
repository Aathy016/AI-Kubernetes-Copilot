from ai_agent.llm_agent import LLMAgent
from rag.rag_engine import RAGEngine


class CopilotChat:

    def __init__(self):

        self.llm = LLMAgent()

        try:
            self.rag = RAGEngine()
        except Exception:
            self.rag = None

    def ask(self, question, report=None):

        context = ""

        try:

            if self.rag:

                docs = self.rag.search(question)

                if docs:

                    context = "\n".join(
                        [str(doc)[:500] for doc in docs[:3]]
                    )

        except Exception as e:

            print("RAG ERROR:")
            print(str(e))

            context = "No matching Kubernetes knowledge found."

        prompt = f"""
You are a Senior Kubernetes SRE.

Cluster Report:
CPU: {report.get('cpu', 0)}
Memory: {report.get('memory', 0)}
Running Pods: {report.get('running', 0)}
Pending Pods: {report.get('pending', 0)}
Failed Pods: {report.get('failed', 0)}
Health Score: {report.get('health_score', 0)}

Knowledge Base:
{context}

Question:
{question}

Provide:

1. Root Cause
2. Impact
3. Resolution
4. Best Practice

Keep answer under 250 words.
"""

        print("\n===== COPILOT PROMPT LENGTH =====")
        print(len(prompt))

        response = self.llm.ask(prompt)

        print("\n===== COPILOT RESPONSE =====")
        print(response)

        return response