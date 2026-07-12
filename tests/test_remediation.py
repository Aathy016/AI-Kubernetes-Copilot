import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_agent.remediation_engine import RemediationEngine

engine = RemediationEngine()

incident = {
    "issue": "CrashLoopBackOff",
    "pod": "nginx-app"
}

print(
    engine.generate_fix(
        incident
    )
)