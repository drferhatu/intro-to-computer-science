# From the field: ask a web API for data. GitHub answers in JSON, which Python turns into dicts and lists.
# pip install requests   (already there in Colab and in the codespace)

import requests

user = input("GitHub username: ")
response = requests.get(f"https://api.github.com/users/{user}/repos?per_page=100")

if response.status_code != 200:
    print("No such user (or too many requests).")
else:
    repos = response.json()                       # a list of dicts, one per repository
    print(f"{len(repos)} public repositories")
    for repo in sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:5]:
        print(f"  {repo['name']:35} ★ {repo['stargazers_count']}")
