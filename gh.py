from github import Github
from env import token

# First create a Github instance:
github = Github(token)


def analyze_repos(user):
    print('Finding repository please wait a moment...')
    # Get repo
    repo = github.get_repo(
        'leslie-alldridge/yaml_config')
    # grab the yaml folder
    yaml_folder = repo.get_contents("teams")
    # run over each file
    for file in yaml_folder:
        file = repo.get_contents(file.path)
        # See if email address exists, and if so, remove it
        if user in str(file.decoded_content):
            # decode byte string
            user_array = tidy_content(file.decoded_content.decode("utf-8"))
            # remove user from list
            new_array = remove_user(user_array, user)
            # convert list back to string
            final_msg = list_to_string(new_array)
            # update github with the new changes
            print(final_msg)
            repo.update_file(file.path, "Removed user",
                             final_msg, yaml_folder.sha, branch="test")
            repo.create_pull(
                base='master', head='leslie-alldridge:test', title='test', body='test')
    print('Done')


# from yaml organised string to list of dictionaries


def tidy_content(content_as_string):
    tidy = content_as_string.splitlines()
    output = []
    for key_value in tidy:
        if 'email' in key_value:
            key, value = key_value.split(': ', 1)
            if not output or key in output[-1]:
                output.append({})
            output[-1][key] = value
        if 'role' in key_value:
            key, value = key_value.split(': ', 1)
            if not output or key in output[-1]:
                output.append({})
            output[-1][key] = value
        if 'name' in key_value:
            key, value = key_value.split(': ', 1)
            if not output or key in output[-1]:
                output.append({})
            output[-1][key] = value
        if 'role' in key_value:
            key, value = key_value.split(': ', 1)
            if not output or key in output[-1]:
                output.append({})
            output[-1][key] = value
        if 'job_title' in key_value:
            key, value = key_value.split(': ', 1)
            if not output or key in output[-1]:
                output.append({})
            output[-1][key] = value
    return output

# remove user from yaml file


def remove_user(users, email):
    for user in users:
        if len(user) > 2:
            if user['  email'] == email:
                users.remove(user)
    return users

# list of dictionaries back to a yaml organized string


def list_to_string(arr):
    string_final = ''
    print('arr')
    print(arr)
    for item in arr:
        if len(item) > 2:
            string_final += ('- name: ' + item['- name'] + '\n' + '  email: ' +
                             item['  email'] + '\n' + '  role: ' + item['  role'] + '\n')
            if len(item) > 3:
                string_final += ('  job_title: ' +
                                 item['  job_title'] + '\n')
    return string_final


user = 'leslie1@xero.com'
analyze_repos(user)
