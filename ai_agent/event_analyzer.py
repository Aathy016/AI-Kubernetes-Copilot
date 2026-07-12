from kubernetes import client, config


class EventAnalyzer:

    def __init__(self):

        config.load_kube_config()

        self.v1 = client.CoreV1Api()

    def analyze(self):

        events = self.v1.list_event_for_all_namespaces()

        findings = []

        for event in events.items:

            message = str(event.message)

            if "CrashLoopBackOff" in message:

                findings.append({
                    "severity": "HIGH",
                    "issue": "CrashLoopBackOff",
                    "resource": event.involved_object.name
                })

            elif "ImagePullBackOff" in message:

                findings.append({
                    "severity": "HIGH",
                    "issue": "ImagePullBackOff",
                    "resource": event.involved_object.name
                })

            elif "OOMKilled" in message:

                findings.append({
                    "severity": "CRITICAL",
                    "issue": "OOMKilled",
                    "resource": event.involved_object.name
                })

        return findings