import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_agent.copilot_chat import CopilotChat

chat = CopilotChat()

answer = chat.ask(
    "Explain ImagePullBackOff"
)

print()
print("=" * 50)
print(answer)