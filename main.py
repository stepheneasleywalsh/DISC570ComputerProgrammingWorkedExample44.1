import requests, json


def askQuestion(question):
    API_KEY = "HIDDEN"
    model = "models/gemini-2.5-flash"

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