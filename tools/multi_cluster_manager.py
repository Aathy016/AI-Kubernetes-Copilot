from tools.cluster_manager import ClusterManager


class MultiClusterManager:

    def __init__(self):

        self.manager = ClusterManager()

    def analyze_all(self):

        contexts = self.manager.get_contexts()

        reports = []

        for context in contexts["contexts"]:

            self.manager.switch_context(
                context
            )

            reports.append({
                "cluster": context
            })

        return reports