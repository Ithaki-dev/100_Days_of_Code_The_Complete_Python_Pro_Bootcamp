import requests


def get_gender(user_name):
        # Use the Genderize API
    response = requests.get(f'https://api.genderize.io?name={user_name}')
    gender = response.json().get('gender')
    return gender

def get_age(user_name):
        # Use the Agify API
    response = requests.get(f'https://api.agify.io?name={user_name}')
    age = response.json().get('age')
    return age

if __name__ == "__main__":
    user_name = "John"
    user_age = get_age(user_name)
    user_gender = get_gender(user_name)
    print(f"Name: {user_name}, Age: {user_age}, Gender: {user_gender}")