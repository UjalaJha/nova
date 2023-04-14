import json

import requests
from config import TOKEN

headers = {
    'Authorization': 'token '+TOKEN
}


def get_top_repositories(stars):
    api_url = f"https://api.github.com/search/repositories?q=stars:>{stars}&sort=stars&order=desc"
    response = requests.get(api_url, headers=headers)
    # print(response.status_code)
    repositories = json.loads(response.text)['items']
    # print(f"Top OS Repository : {len(repositories)}")
    return repositories

# stars = 100000
# get_top_repositories(stars)
