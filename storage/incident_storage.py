import chromadb
from datetime import datetime


class IncidentStorage:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        try:

            self.collection = (
                self.client.get_collection(
                    "incident_history"
                )
            )

        except:

            self.collection = (
                self.client.create_collection(
                    "incident_history"
                )
            )

    def save_incident(
        self,
        report,
        rca
    ):

        incident_id = (
            datetime.now()
            .strftime("%Y%m%d%H%M%S")
        )

        document = f"""
CPU: {report['cpu']}
Memory: {report['memory']}
Running: {report['running']}
Pending: {report['pending']}
Failed: {report['failed']}
Health Score: {report['health_score']}

RCA:
{rca}
"""

        self.collection.add(
            ids=[incident_id],
            documents=[document]
        )

        return incident_id

    def get_all_incidents(self):

        return self.collection.get()