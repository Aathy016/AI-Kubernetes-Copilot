class PromQLGenerator:

    def __init__(self):

        self.promql_map = {

            "cpu usage":
            '100 - (avg by(instance)(irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)',

            "memory usage":
            '(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100',

            "pod count":
            'count(kube_pod_info)',

            "running pods":
            'count(kube_pod_status_phase{phase="Running"})',

            "failed pods":
            'count(kube_pod_status_phase{phase="Failed"})'
        }

    def generate(self, query):

        query = query.lower()

        for key in self.promql_map:

            if key in query:

                return self.promql_map[key]

        return "No PromQL Found"