import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from ai_agent.cluster_analyzer import ClusterAnalyzer
from ai_agent.recommendation_engine import RecommendationEngine


analyzer = ClusterAnalyzer()

report = analyzer.analyze()

engine = RecommendationEngine()

recommendations = engine.generate(report)

print()
print("=" * 60)
print("AI RECOMMENDATIONS")
print("=" * 60)

for r in recommendations:

    print(f"- {r}")

print("=" * 60)