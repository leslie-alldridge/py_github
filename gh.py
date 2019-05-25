from github import Github
from env import token

# First create a Github instance:
github = Github(token)

# Globals
name = []
react_repos = []

# Get all repos and analyze their tags


def analyze_repos():
    for repo in github.get_user().get_repos():
        # add repo names to an array
        if "kakapo-2018" not in repo.full_name:
            name.append(repo.full_name)
        print(name)

        for item in name:
            repo = github.get_repo(item)
            topics = repo.get_topics()
            if "react" in topics:
                react_repos.append(item)


print(react_repos)
print("You have " + str(len(react_repos)) + " repos using React")

analyze_repos()
