import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ai_agent.event_analyzer import EventAnalyzer

analyzer = EventAnalyzer()

results = analyzer.analyze()

print(results)