import requests


url = "http://localhost:11434/api/generate"


payload = {
    "model": "qwen2.5:1.5b",
    "prompt": "Explain Kubernetes in simple terms",
    "stream": False,
    "options": {
        "num_ctx": 512,
        "num_predict": 200
    }
}


response = requests.post(
    url,
    json=payload,
    timeout=120
)


print("STATUS:")
print(response.status_code)


print("\nRAW RESPONSE:")
print(response.text)


try:
    data = response.json()

    if "response" in data:
        print("\nANSWER:")
        print(data["response"])

    else:
        print("\nERROR:")
        print(data)

except Exception as e:
    print(e)