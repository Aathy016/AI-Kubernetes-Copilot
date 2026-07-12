from ai_agent.llm_agent import LLMAgent
from tools.Kubernetes_tool import KubernetesTool


class RCAEngine:

    def __init__(self):
        self.k8s = KubernetesTool()
        self.llm = LLMAgent()

    def analyze(self, report=None):

        try:
            events = str(self.k8s.get_events())[:2000]

        except Exception as e:
            events = f"Unable to fetch events: {str(e)}"

        try:
            pods = self.k8s.get_pods()

        except Exception as e:
            pods = []
            events += f"\nUnable to fetch pods: {str(e)}"

        logs = []

        try:

            for pod in pods:

                namespace = pod.get("namespace", "")
                pod_name = pod.get("name", "")

                if namespace == "ai-copilot":

                    try:

                        pod_logs = self.k8s.get_pod_logs(
                            pod_name,
                            namespace
                        )

                        logs.append(
                            f"Pod: {pod_name}\n{str(pod_logs)[:1000]}"
                        )

                    except Exception as log_error:

                        logs.append(
                            f"Failed to get logs for {pod_name}: {str(log_error)}"
                        )

        except Exception as e:

            logs.append(
                f"Error processing pod logs: {str(e)}"
            )

        prompt = f"""
You are a Kubernetes Site Reliability Engineer (SRE).

Cluster Summary:
CPU Usage: {report.get('cpu', 0)}%
Memory Usage: {report.get('memory', 0)}%
Running Pods: {report.get('running', 0)}
Pending Pods: {report.get('pending', 0)}
Failed Pods: {report.get('failed', 0)}
Health Score: {report.get('health_score', 0)}

Recent Kubernetes Events:
{events}

Recent Pod Logs:
{logs[:3]}

Analyze the cluster and provide:

1. Executive Summary
2. Root Cause
3. Impact
4. Resolution Steps
5. Prevention Recommendations
6. Risk Level (Low / Medium / High)

Keep the response under 300 words.
"""

        print("\n===== RCA PROMPT LENGTH =====")
        print(len(prompt))

        try:

            response = self.llm.ask(prompt)

            print("\n===== RCA RESPONSE =====")
            print(response)

            if not response:
                return "No RCA response generated."

            return response

        except Exception as e:

            print("\n===== RCA ERROR =====")
            print(str(e))

            return f"RCA generation failed: {str(e)}"