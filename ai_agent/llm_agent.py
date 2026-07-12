import requests


class LLMAgent:

    def __init__(self):

        self.url = "http://localhost:11434/api/generate"

    def ask(self, prompt):

        try:

            response = requests.post(
                self.url,
                json={
                    "model": "qwen2.5:1.5b",
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "num_ctx": 512,
                        "num_predict": 300,
                        "temperature": 0.2
                    }
                },
                timeout=300
            )

            response.raise_for_status()

            result = response.json()

            print("\n===== LLM RESPONSE =====")
            print(result)

            return result.get(
                "response",
                "No response from model."
            )

        except Exception as e:

            print("\n===== LLM ERROR =====")
            print(str(e))

            return f"LLM Error: {str(e)}"