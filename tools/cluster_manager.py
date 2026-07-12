from kubernetes import config


class ClusterManager:

    def get_contexts(self):

        contexts, active = config.list_kube_config_contexts()

        return {
            "active": active["name"],
            "contexts": [c["name"] for c in contexts]
        }

    def switch_context(self, context_name):

        config.load_kube_config(
            context=context_name
        )

        return f"Switched to {context_name}"