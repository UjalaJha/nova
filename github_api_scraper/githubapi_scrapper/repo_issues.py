import json
import requests
from nova.github_api_scraper.config import TOKEN

headers = {
    'Authorization': 'token '+TOKEN
}


def get_issues(repo):
    api_url = f"https://api.github.com/repos/{repo}/issues"
    response = requests.get(api_url, headers=headers)
    # print(response.status_code)
    issues = json.loads(response.text)
    # print(f"Top OS Repository : {len(issues)}")
    # for issue in issues:
    #     print({issue['url']}, {issue['title']})\
    return issues


# repo = "twitter/the_algorithm"
# get_issues(repo)
