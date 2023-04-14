import requests
from  nova.github_api_scraper.config import TOKEN

headers = {
    'Authorization': 'token '+TOKEN
}


def get_user_data_watch():
    api_url = f"https://api.github.com/users/khushijashnani/subscriptions"

    response = requests.get(api_url, headers=headers)
    data = response.json()
    print("output")
    print(data)

def get_user_data_forks():
    api_url = f"https://api.github.com/users/khushijashnani/repos?type=forks"

    response = requests.get(api_url, headers=headers)
    data = response.json()
    print("output")
    print(data)

def get_user_data_starred():
    api_url = f"https://api.github.com/users/khushijashnani/starred"

    response = requests.get(api_url, headers=headers)
    data = response.json()
    print("output")
    print(data)

get_user_data_starred()
get_user_data_forks()
get_user_data_watch()