import csv

import requests
from github.GithubException import GithubException

from nova.github_api_scraper.config import TOKEN

headers = {
    'Authorization': 'token ' + TOKEN
}
stars = 300000

# Create an empty list to store the data
data = []

# Define the columns of the CSV file
repo_headers = ['Repository', 'Repository_fullname', 'Language',
           'Topic', 'Description',
           'Watchers', 'Stars', 'Forks', 'open_issues_count'
           'Created', 'Last_update', 'License']


def get_repositories():
    api_url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'stars:>300000',
        'sort': 'stars',
        'order': 'desc',
    }
    response = requests.get(api_url, params=params, headers=headers)
    # print(response.status_code)
    response_json = response.json()
    print(response_json)
    repositories = response_json['items']
    # repositories = json.loads(response.text)['items']
    # print(f"Top OS Repository : {len(repositories)}")
    return repositories


# Search for repositories using the GitHub API and retrieve the desired data
for repository in get_repositories():
    # print(repo)
    try:
        row = [repository['name'], repository['full_name'], repository['language'],
               repository['topics'], repository['description'],
               repository['stargazers_count'], repository['stargazers_count'], repository['forks_count'],
               repository['open_issues_count'],
               repository['created_at'], repository['updated_at'], repository['license']['spdx_id']]
        data.append(row)
    except GithubException as e:
        print(f"{repository['full_name']} | {repository}")
        print(e)

# Save the data as a CSV file
with open('github_feature_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(repo_headers)
    writer.writerows(data)
