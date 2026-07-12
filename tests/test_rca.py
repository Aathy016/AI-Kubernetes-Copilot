import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_agent.rca_engine import RCAEngine

engine = RCAEngine()

result = engine.analyze()

print(result)