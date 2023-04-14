import csv
import github
from config import TOKEN
from github.GithubException import UnknownObjectException
from github.GithubException import GithubException

g = github.Github(TOKEN)

# Define the columns of the CSV file
headers = ['Repository', 'Repository_owner', 'Repository_fullname', 'Is_fork', 'Parent', 'Stars', 'Watchers', 'Forks',
           'Description', 'Language', 'Languages', 'Topic', 'Contributors', 'Open_issues', 'Open_pull_requests',
           'License', 'Created', 'Last_update']

# Define the search query to retrieve open source repositories
query = 'is:public stars:>10000 '

# Create an empty list to store the data
data = []

# Search for repositories using the GitHub API and retrieve the desired data
for repo in g.search_repositories(query):
    # print(repo)
    try:
        row = [repo.name, repo.owner.login, repo.full_name, repo.fork,
               repo.parent.full_name if repo.parent is not None else "", repo.stargazers_count, repo.subscribers_count,
               repo.forks_count, repo.description, repo.language, list(repo.get_languages().keys()), repo.topics,
               len(list(repo.get_contributors())), repo.open_issues_count, repo.get_pulls(state='open').totalCount,
               repo.get_license().name, repo.created_at, repo.updated_at]
        data.append(row)
    except GithubException as e:
        if e.status == 404:
            row = [repo.name, repo.owner.login, repo.full_name, repo.fork,
                   repo.parent.full_name if repo.parent is not None else "", repo.stargazers_count,
                   repo.subscribers_count,
                   repo.forks_count, repo.description, repo.language, list(repo.get_languages().keys()), repo.topics,
                   len(list(repo.get_contributors())), repo.open_issues_count, repo.get_pulls(state='open').totalCount,
                   "", repo.created_at, repo.updated_at]
            data.append(row)
        else:
            print(f"{repo.full_name} | {repo}")
            print(e)

# Save the data as a CSV file
with open('10k_stars_up_github_repos_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)
