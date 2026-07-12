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

from kubernetes import client
from tools.Kubernetes_tool import KubernetesTool


# ==================================
# CONNECT TO KUBERNETES
# ==================================

k8s = KubernetesTool()

cfg = client.Configuration.get_default_copy()

print("\n" + "=" * 50)
print("KUBERNETES API SERVER")
print("=" * 50)
print(cfg.host)

# ==================================
# NODES
# ==================================

print("\n" + "=" * 50)
print("NODES")
print("=" * 50)

for node in k8s.get_nodes():
    print(node)

# ==================================
# NAMESPACES
# ==================================

print("\n" + "=" * 50)
print("NAMESPACES")
print("=" * 50)

for ns in k8s.get_namespaces():
    print(ns)

# ==================================
# PODS
# ==================================

print("\n" + "=" * 50)
print("PODS")
print("=" * 50)

for pod in k8s.get_pods():
    print(pod)

# ==================================
# SERVICES
# ==================================

print("\n" + "=" * 50)
print("SERVICES")
print("=" * 50)

for svc in k8s.get_services():
    print(svc)

# ==================================
# DEPLOYMENTS
# ==================================

print("\n" + "=" * 50)
print("DEPLOYMENTS")
print("=" * 50)

for deploy in k8s.get_deployments():
    print(deploy)

# ==================================
# EVENTS
# ==================================

print("\n" + "=" * 50)
print("EVENTS")
print("=" * 50)

events = k8s.get_events()

for event in events:
    print(event)

# ==================================
# POD LOGS
# ==================================

print("\n" + "=" * 50)
print("POD LOGS")
print("=" * 50)

pods = k8s.get_pods()

for pod in pods:

    if pod["namespace"] == "ai-copilot":

        print(
            f"\nLogs for Pod: {pod['name']}"
        )

        print("-" * 50)

        logs = k8s.get_pod_logs(
            pod["name"],
            pod["namespace"]
        )

        print(logs)

# ==================================
# SUMMARY
# ==================================

print("\n" + "=" * 50)
print("CLUSTER SUMMARY")
print("=" * 50)

print(
    f"Total Nodes       : {len(k8s.get_nodes())}"
)

print(
    f"Total Namespaces  : {len(k8s.get_namespaces())}"
)

print(
    f"Total Pods        : {len(k8s.get_pods())}"
)

print(
    f"Total Services    : {len(k8s.get_services())}"
)

print(
    f"Total Deployments : {len(k8s.get_deployments())}"
)