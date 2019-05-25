from github import Github
from env import token

# First create a Github instance:
github = Github(token)

# Globals
python_repos = []

# Get all repos and analyze their tags
# add repos tagged with python to an array and print it


def analyze_repos():
    print('Checking repositories, please wait a moment...')
    repositories = github.search_repositories(
        query='language:python user:leslie-alldridge')
    for repo in repositories:
        topics = repo.get_topics()
        if topics != []:
            if "python" in topics:
                # here we would have all of our team tagged repos but just using 'python' for now
                python_repos.append(repo.full_name)
                # check if it has a PR?
                pulls = repo.get_pulls(
                    state='open')
                for pr in pulls:
                    # Print out message and PR url
                    print("Your repository " + repo.full_name +
                          ' has an open PR here: ' + pr.html_url)

    print('Done')


analyze_repos()
