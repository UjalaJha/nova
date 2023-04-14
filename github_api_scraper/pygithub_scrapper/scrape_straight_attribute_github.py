import csv
import github
import pandas as pd
# Replace YOUR_GITHUB_TOKEN with your personal access token
from github.GithubException import GithubException
from nova.github_api_scraper.config import TOKEN

g = github.Github(TOKEN)

# Define the columns of the CSV file
headers = ['Repository',
           'Repository_owner',
           'Repository_fullname',
           'Is_fork',
           'Parent',
           'Stars',
           'Watchers',
           'Forks',
           'Description',
           'Language',
           'Topic',
           'Open_issues',
           'Created',
           'Last_update']

# Define the search query to retrieve open source repositories
query = 'is:public stars:>1000'

# Create an empty list to store the data
data = []

# Search for repositories using the GitHub API and retrieve the desired data
for repo in g.search_repositories(query):
    # print(repo)
    try:
        row = [repo.name,
               repo.owner.login,
               repo.full_name,
               repo.fork,
               repo.parent.full_name if repo.parent is not None else "",
               repo.stargazers_count,
               repo.subscribers_count,
               repo.forks_count,
               repo.description,
               repo.language,
               repo.topics,
               repo.open_issues_count,
               repo.created_at,
               repo.updated_at]
        data.append(row)
    except GithubException as e:
        print(f"{repo.full_name} | {repo}")
        print(e)

# Save the data as a CSV file
with open('1k_stars_up_github_repos_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)


def good_first_issues():
    # Define the search query to retrieve open source repositories
    query = 'is:public good-first-issues:>20'

    # Create an empty list to store the data
    data = []

    # Search for repositories using the GitHub API and retrieve the desired data
    for repo in g.search_repositories(query):
        # print(repo)
        try:
            row = [repo.name,
                   repo.owner.login,
                   repo.full_name,
                   repo.fork,
                   repo.parent.full_name if repo.parent is not None else "",
                   repo.stargazers_count,
                   repo.subscribers_count,
                   repo.forks_count,
                   repo.description,
                   repo.language,
                   repo.topics,
                   repo.open_issues_count,
                   repo.created_at]
            data.append(row)
            data = pd.DataFrame(data, columns=headers)
            data.to_csv("good_first_issues_data.csv")
        except GithubException as e:
            print(f"{repo.full_name} | {repo}")
            print(e)


if __name__ == '__main__':
    good_first_issues()