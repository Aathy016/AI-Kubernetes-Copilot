import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_agent.llm_agent import LLMAgent

agent = LLMAgent()

response = agent.ask(
    "Explain Kubernetes in 2 lines"
)

print(response)