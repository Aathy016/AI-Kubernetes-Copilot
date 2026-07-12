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

from ai_agent.llm_recommendation_engine import LLMRecommendationEngine


sample_report = {
    "cpu": 70,
    "memory": 65,
    "health_score": 80,
    "running": 10,
    "pending": 1,
    "failed": 0
}


engine = LLMRecommendationEngine()


response = engine.generate(
    sample_report
)


print("AI RESPONSE:")
print(response)