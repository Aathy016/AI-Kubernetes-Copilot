import requests


class GrafanaTool:

    def __init__(self):

        self.url = "http://localhost:3000"

        self.headers = {
            "Authorization": f"Bearer {os.getenv('GRAFANA_TOKEN')}"
        }

    def health(self):

        response = requests.get(
            f"{self.url}/api/health",
            timeout=60
        )

        return response.json()

    def get_dashboards(self):

        response = requests.get(
            f"{self.url}/api/search",
            headers=self.headers,
            timeout=60
        )

        return response.json()