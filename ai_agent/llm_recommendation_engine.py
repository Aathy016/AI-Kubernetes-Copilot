import requests


class LLMRecommendationEngine:

    def __init__(self):

        self.url = "http://localhost:11434/api/generate"

    def generate(self, report):

        prompt = f"""
Analyze this Kubernetes cluster report:

{report}

Provide:
1. Cluster Health Summary
2. Risks
3. Recommendations
"""

        try:

            response = requests.post(
                self.url,
                json={
                    "model": "qwen2.5:1.5b",
                    "prompt": prompt,
                    "stream": False
                },
                timeout=300
            )

            result = response.json()

            print(result)

            return result.get(
                "response",
                "No AI response generated."
            )

        except Exception as e:

            return f"LLM Error: {e}"