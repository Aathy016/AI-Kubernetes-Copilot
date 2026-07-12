import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from tools.Kubernetes_tool import KubernetesTool
from tools.prometheus_tool import PrometheusTool


class ClusterAnalyzer:

    def __init__(self):

        self.k8s = KubernetesTool()
        self.prom = PrometheusTool()

    def calculate_health_score(
        self,
        cpu,
        memory,
        running,
        pending,
        failed
    ):

        score = 100

        if cpu > 80:
            score -= 20

        if memory > 80:
            score -= 20

        if pending > 0:
            score -= 10

        if failed > 0:
            score -= 20

        if score < 0:
            score = 0

        return score

    def analyze(self):

        report = {}

        # =========================
        # CPU Metrics
        # =========================

        cpu_result = self.prom.get_node_cpu()

        print("\nCPU RAW:")
        print(cpu_result)

        try:

            cpu = float(
                cpu_result["data"]["result"][0]["value"][1]
            )

        except Exception as e:

            print("\nCPU ERROR:")
            print(e)

            cpu = 0

        # =========================
        # Memory Metrics
        # =========================

        memory_result = self.prom.get_node_memory()

        print("\nMEMORY RAW:")
        print(memory_result)

        try:

            memory = float(
                memory_result["data"]["result"][0]["value"][1]
            )

        except Exception as e:

            print("\nMEMORY ERROR:")
            print(e)

            memory = 0

        # =========================
        # Pod Metrics
        # =========================

        pods = self.k8s.get_pods()

        running = 0
        pending = 0
        failed = 0

        for pod in pods:

            status = pod["status"]

            if status == "Running":
                running += 1

            elif status == "Pending":
                pending += 1

            elif status == "Failed":
                failed += 1

        # =========================
        # Health Score
        # =========================

        score = self.calculate_health_score(
            cpu,
            memory,
            running,
            pending,
            failed
        )

        report["cpu"] = cpu
        report["memory"] = memory
        report["running"] = running
        report["pending"] = pending
        report["failed"] = failed
        report["health_score"] = score

        return report