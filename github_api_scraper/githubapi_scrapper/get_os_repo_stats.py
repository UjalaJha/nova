from repo_language import get_language_percentages
from repo_issues import get_issues
from open_source_repo import get_top_repositories

stars = 300000

for repository in get_top_repositories(stars):
    # print(repository)
    percentages = get_language_percentages(repository['full_name'])
    issues = get_issues(repository['full_name'])
    print("--------------------------------")
    print(f"REPO : {repository['full_name']}")
    print(f"LANGUAGES USED : {len(issues)}")
    for language, percentage in percentages.items():
        print(f"{language}: {percentage:.2f}%")
    print(f"ISSUES TOTAL : {len(issues)}")
    for issue in issues:
        print({issue['url']}, {issue['title']})