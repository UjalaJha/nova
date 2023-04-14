import json
from collections import OrderedDict
import requests
import pandas as pd
from nova.github_api_scraper.config import TOKEN


class Base:

    def __init__(self, url, params, clname):
        self.headers = {
            'Authorization': 'token ' + TOKEN
        }
        self.url = url
        self.params = params
        self.clname = clname


    def makeRequest(self):
        # Make the API request and retrieve the JSON response
        response = requests.get(self.url, params=self.params, headers=self.headers)
        response_json = response.json()

        return response_json


# Define the API endpoint classes and search parameters
class AllRepositories(Base):

    def __init__(self, page):
        url = 'https://api.github.com/search/repositories'
        params = {
            'q': 'license:MIT stars:>10000',
            'sort': 'stars',
            'order': 'desc',
            'per_page': 100,
            'page': page
        }
        super(AllRepositories, self).__init__(url, params, self.__class__.__name__)

# Define the API endpoint classes and search parameters
class GetLanguage(Base):

    def __init__(self, repo):
        url = 'https://api.github.com/repos/{}/languages'.format(repo)
        params = {}
        super(GetLanguage, self).__init__(url, params, self.__class__.__name__)


if __name__ == '__main__':

    all_repos = []
    page = 1
    while True:
        print("Start fetching page = ", page)
        response = AllRepositories(page=page).makeRequest()

        if "items" in response:
            # transformation
            repos = response["items"]
            for repo in repos:
                languages = OrderedDict(GetLanguage(repo=repo["full_name"]).makeRequest())
                repo["lang_name"] = list(languages.keys())
                repo["lang_perc"] = list(languages.values())
                repo["license_name"] = repo["license"]["spdx_id"]

            # to get the current response length
            page_results = len(response["items"])
            print("Finished fetching page = ", page, " with ", page_results, " rows.")

            all_repos.extend(repos)
            print("Current dataset includes", len(all_repos), " rows.")

            if page_results == 100:
                page += 1
            else:
                break
        else:
            print(response)
            break

    df = pd.DataFrame(all_repos)
    df.to_csv("repos.csv")
