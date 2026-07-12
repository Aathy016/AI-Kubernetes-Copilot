import json


class RCAAgent:

    def __init__(self):

        with open(
            "knowledge_base/k8s_incidents.json",
            "r"
        ) as file:

            self.incidents = json.load(file)

    def analyze_events(self, events):

        findings = []

        for event in events:

            message = event["message"]

            for incident in self.incidents:

                if incident["error"] in message:

                    findings.append({
                        "error": incident["error"],
                        "cause": incident["cause"],
                        "solution": incident["solution"]
                    })

        return findings