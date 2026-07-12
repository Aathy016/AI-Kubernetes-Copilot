import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from storage.incident_storage import (
    IncidentStorage
)

storage = IncidentStorage()

report = {
    "cpu": 50,
    "memory": 60,
    "running": 10,
    "pending": 1,
    "failed": 0,
    "health_score": 90
}

storage.save_incident(
    report,
    "ImagePullBackOff RCA"
)

print(
    storage.get_all_incidents()
)