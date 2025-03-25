# This is a app for use pixela API

import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "asd2dqwed23dsd23sd23",
    "username": "rquesada",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(pixela_endpoint, json=user_params)
print(response.text)