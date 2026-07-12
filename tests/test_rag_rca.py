import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from tools.Kubernetes_tool import KubernetesTool
from agents.rca_agent import RCAAgent

k8s = KubernetesTool()
rca = RCAAgent()

events = k8s.get_events()

results = rca.analyze_events(events)

print("\nRAW RESULTS:\n")
print(results)