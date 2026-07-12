from kubernetes import client, config


class KubernetesTool:

    def __init__(self):

        try:

            # Always reload kubeconfig
            config.load_kube_config()

            cfg = client.Configuration.get_default_copy()

            print("\n===================================")
            print("KUBERNETES CONNECTION")
            print("API SERVER:", cfg.host)
            print("===================================\n")

            self.v1 = client.CoreV1Api()
            self.apps_v1 = client.AppsV1Api()

            # Validate connection immediately
            self.v1.list_namespace(limit=1)

        except Exception as e:

            print(
                f"\nKubernetes Connection Error: {e}\n"
            )

            raise

    # --------------------------------------------------
    # Nodes
    # --------------------------------------------------
    def get_nodes(self):

        nodes = self.v1.list_node()

        result = []

        for node in nodes.items:

            status = "Unknown"

            for condition in node.status.conditions:

                if (
                    condition.type == "Ready"
                    and condition.status == "True"
                ):
                    status = "Ready"

            result.append(
                {
                    "name": node.metadata.name,
                    "status": status
                }
            )

        return result

    # --------------------------------------------------
    # Namespaces
    # --------------------------------------------------
    def get_namespaces(self):

        namespaces = self.v1.list_namespace()

        return [
            ns.metadata.name
            for ns in namespaces.items
        ]

    # --------------------------------------------------
    # Pods
    # --------------------------------------------------
    def get_pods(self):

        pods = self.v1.list_pod_for_all_namespaces()

        result = []

        for pod in pods.items:

            result.append(
                {
                    "name": pod.metadata.name,
                    "namespace": pod.metadata.namespace,
                    "status": pod.status.phase
                }
            )

        return result

    # --------------------------------------------------
    # Services
    # --------------------------------------------------
    def get_services(self):

        services = self.v1.list_service_for_all_namespaces()

        result = []

        for svc in services.items:

            result.append(
                {
                    "name": svc.metadata.name,
                    "namespace": svc.metadata.namespace,
                    "type": svc.spec.type
                }
            )

        return result

    # --------------------------------------------------
    # Deployments
    # --------------------------------------------------
    def get_deployments(self):

        deployments = (
            self.apps_v1
            .list_deployment_for_all_namespaces()
        )

        result = []

        for deploy in deployments.items:

            result.append(
                {
                    "name": deploy.metadata.name,
                    "namespace": deploy.metadata.namespace,
                    "replicas": deploy.spec.replicas
                }
            )

        return result

    # --------------------------------------------------
    # Events
    # --------------------------------------------------
    def get_events(
        self,
        namespace="ai-copilot"
    ):

        events = (
            self.v1
            .list_namespaced_event(namespace)
        )

        result = []

        for event in events.items:

            result.append(
                {
                    "reason": event.reason,
                    "type": event.type,
                    "message": event.message
                }
            )

        return result

    # --------------------------------------------------
    # Pod Logs
    # --------------------------------------------------
    def get_pod_logs(
        self,
        pod_name,
        namespace="ai-copilot"
    ):

        try:

            logs = (
                self.v1.read_namespaced_pod_log(
                    name=pod_name,
                    namespace=namespace
                )
            )

            return logs

        except Exception as e:

            return str(e)