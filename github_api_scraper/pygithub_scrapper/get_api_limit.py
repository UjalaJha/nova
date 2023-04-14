from github import Github
from nova.github_api_scraper.config import TOKEN


# Create a GitHub API client using your access token
g = Github(TOKEN)

# Get the authenticated user
rate_limit = g.get_rate_limit()

# Get the rate limit information for the authenticated user

# Print the current rate limit status
print("Rate limit remaining:", rate_limit.core.remaining)
print("Rate limit reset time:", rate_limit.core.reset)