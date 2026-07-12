class IncidentDetector:

    def detect(self, report):

        incidents = []

        if report["cpu"] > 80:

            incidents.append({
                "severity": "HIGH",
                "issue": "High CPU Usage",
                "value": report["cpu"]
            })

        if report["memory"] > 80:

            incidents.append({
                "severity": "HIGH",
                "issue": "High Memory Usage",
                "value": report["memory"]
            })

        if report["pending"] > 0:

            incidents.append({
                "severity": "MEDIUM",
                "issue": "Pending Pods",
                "count": report["pending"]
            })

        if report["failed"] > 0:

            incidents.append({
                "severity": "CRITICAL",
                "issue": "Failed Pods",
                "count": report["failed"]
            })

        return incidents