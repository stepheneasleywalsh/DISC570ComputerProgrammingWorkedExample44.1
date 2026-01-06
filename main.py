import requests, json, os


def askQuestion(question):
    model = "models/gemini-2.5-flash"
    API_KEY = os.environ["G_API_KEY"]
    url = f"https://generativelanguage.googleapis.com/v1beta/{model}:generateContent?key={API_KEY}"

    data = {
        "contents": [
            {"parts": [{"text": f"{question} (please use only plain text, no ** etc)"}]}
        ]
    }

    response = requests.post(url, json=data)
    return (response.json()["candidates"][0]["content"]["parts"][0]["text"])

while True:
    print(askQuestion(input("> ")))