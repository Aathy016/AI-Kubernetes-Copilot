import requests

r = requests.get(
    "http://localhost:3000/login",
    timeout=30
)

print(r.status_code)
print(r.url)
print(r.text[:200])