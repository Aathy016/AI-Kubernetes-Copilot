import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.Kubernetes_tool import KubernetesTool
from agents.rca_agent import RCAAgent


k8s = KubernetesTool()
rca = RCAAgent()

events = k8s.get_events()

results = rca.analyze_events(events)

print("\n===== RCA REPORT =====\n")

for result in results:

    print(f"Error      : {result['error']}")
    print(f"Cause      : {result['cause']}")
    print(f"Solution   : {result['solution']}")
    print("-" * 50)