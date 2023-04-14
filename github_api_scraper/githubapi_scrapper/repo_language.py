import requests
from nova.github_api_scraper.config import TOKEN

headers = {
    'Authorization': 'token '+TOKEN
}


def get_language_percentages(repo):
    api_url = f"https://api.github.com/repos/{repo}/languages"
    response = requests.get(api_url, headers=headers)
    # print(response.status_code)
    data = response.json()
    total_bytes = sum(data.values())

    percentages = {}
    for language, bytes in data.items():
        percentage = bytes / total_bytes * 100
        percentages[language] = percentage

    return percentages


# repo = "twitter/the_algorithm"
# percentages = get_language_percentages(repo)
#
# for language, percentage in percentages.items():
#     print(f"{language}: {percentage:.2f}%")
