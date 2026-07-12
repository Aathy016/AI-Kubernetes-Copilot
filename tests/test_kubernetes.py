from kubernetes import client, config

try:
    # Load Kubernetes config from ~/.kube/config
    config.load_kube_config()

    # Create API client
    v1 = client.CoreV1Api()

    print("\nConnected Successfully to Kubernetes Cluster\n")

    # Get all nodes
    nodes = v1.list_node()

    print("Available Nodes:")
    for node in nodes.items:
        print(f"- {node.metadata.name}")

except Exception as e:
    print(f"Connection Failed: {e}")