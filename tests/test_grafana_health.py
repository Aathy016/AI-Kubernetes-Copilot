# tests/test_grafana_health.py

import requests

response = requests.get(
    "http://localhost:3000/api/health",
    timeout=30
)

print(response.status_code)
print(response.text)