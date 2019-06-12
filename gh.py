from github import Github
from env import token

# First create a Github instance:
github = Github(token)


def analyze_repos(user):
    print('Finding repository please wait a moment...')
    # Get repo
    repo = github.get_repo(
        'leslie-alldridge/yaml_config')
    # grab the yaml file
    contents = repo.get_contents("team.yml", ref="test")
    yaml_repo = contents

    # See if email address exists, and if so, remove it
    if user in str(yaml_repo.decoded_content):
        # decode byte string
        user_array = tidy_content(yaml_repo.decoded_content.decode("utf-8"))
        # remove user from list
        new_array = remove_user(user_array, user)
        # convert list back to string
        final_msg = list_to_string(new_array)
        # update github with the new changes
        repo.update_file(yaml_repo.path, "Removed user",
                         final_msg, contents.sha, branch="test")
    print('Done')


def tidy_content(content_as_string):
    tidy = content_as_string.splitlines()
    output = []
    for key_value in tidy:
        key, value = key_value.split(': ', 1)
        if not output or key in output[-1]:
            output.append({})
        output[-1][key] = value
    return output


def remove_user(users, email):
    for user in users:
        if user['email'] == email:
            users.remove(user)
    return users


def list_to_string(arr):
    string_final = ''
    for item in arr:
        string_final += ('name: ' + item['name'] + '\n' + 'email: ' +
                         item['email'] + '\n' + 'role: ' + item['role'] + '\n')
        if len(item) > 3:
            string_final += ('description: ' + item['description'] + '\n')
    return string_final


user = 'leslie.alldridge2@gmail.com'
analyze_repos(user)
