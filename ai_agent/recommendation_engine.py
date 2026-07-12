class RecommendationEngine:

    def generate(self, report):

        recommendations = []

        if report["pending"] > 0:

            recommendations.append(
                "Investigate Pending Pods."
            )

        if report["failed"] > 0:

            recommendations.append(
                "Check Failed Pods immediately."
            )

        if report["cpu"] > 80:

            recommendations.append(
                "High CPU usage detected."
            )

        if report["memory"] > 80:

            recommendations.append(
                "High Memory usage detected."
            )

        if report["health_score"] >= 90:

            recommendations.append(
                "Cluster health is good."
            )

        return recommendations