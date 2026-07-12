import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_agent.promql_generator import PromQLGenerator

agent = PromQLGenerator()

print(
    agent.generate(
        "show cpu usage"
    )
)

print(
    agent.generate(
        "show memory usage"
    )
)

print(
    agent.generate(
        "show failed pods"
    )
)