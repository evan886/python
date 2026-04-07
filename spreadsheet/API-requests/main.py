import requests
# https://archives.docs.gitlab.com/16.11/ee/api/rest/index.html
response=requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} \n Project Url: {project['web_url']}\n")
# print(response.json())
# print(type(response.json()))
# print(response.text)
# print(type(response.text))