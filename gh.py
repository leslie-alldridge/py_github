from github import Github
from env import token

# First create a Github instance:
github = Github(token)

# Globals
python_repos = []

# Get all repos and analyze their tags
# add repos tagged with python to an array and print it


def analyze_repos():
    repositories = github.search_repositories(
        query='language:python user:leslie-alldridge')
    for repo in repositories:
        print(repo)
        topics = repo.get_topics()
        if topics != []:
            if "python" in topics:
                python_repos.append(repo.full_name)
    print("You have " + str(len(python_repos)) + " repo(s) using Python")


analyze_repos()
