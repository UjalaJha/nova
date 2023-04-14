import csv
import github
from github.GithubException import UnknownObjectException
# Replace YOUR_GITHUB_TOKEN with your personal access token
from github.GithubException import GithubException

g = github.Github("token")

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
