import requests


def get_questions():
    url = "https://opentdb.com/api.php?amount=10&type=boolean"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["results"]

question_data = get_questions()

