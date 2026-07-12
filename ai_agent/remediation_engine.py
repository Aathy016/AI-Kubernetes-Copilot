from ai_agent.llm_agent import LLMAgent


class RemediationEngine:

    def __init__(self):

        self.llm = LLMAgent()

    def generate_fix(self, incident):

        prompt = f"""
You are a Kubernetes SRE.

Incident:

{incident}

Generate:

1. Root Cause
2. kubectl commands
3. Fix Procedure
4. Verification Steps
"""

        return self.llm.ask(prompt)