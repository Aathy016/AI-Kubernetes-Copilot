import requests


class PrometheusTool:

    def __init__(self):

        self.prometheus_url = "http://localhost:9090"

    def query(self, promql):

        try:

            response = requests.get(
                f"{self.prometheus_url}/api/v1/query",
                params={"query": promql},
                timeout=30
            )

            return response.json()

        except Exception as e:

            return {"error": str(e)}

    def get_up_targets(self):

        return self.query("up")

    def get_node_cpu(self):

        return self.query(
            '100 - (avg by(instance)(irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)'
        )

    def get_node_memory(self):

        return self.query(
            '(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100'
        )