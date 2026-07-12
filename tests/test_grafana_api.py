import requests

response = requests.get(
    "http://localhost:3000/api/search",
    timeout=10
)

print(response.status_code)
print(response.text[:500])