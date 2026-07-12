import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from ai_agent.cluster_analyzer import ClusterAnalyzer

analyzer = ClusterAnalyzer()

report = analyzer.analyze()

print()
print("=" * 60)
print("AI CLUSTER HEALTH REPORT")
print("=" * 60)

print(
    f"CPU Usage      : {report['cpu']:.2f}%"
)

print(
    f"Memory Usage   : {report['memory']:.2f}%"
)

print(
    f"Running Pods   : {report['running']}"
)

print(
    f"Pending Pods   : {report['pending']}"
)

print(
    f"Failed Pods    : {report['failed']}"
)

print(
    f"Health Score   : {report['health_score']}/100"
)

print("=" * 60)