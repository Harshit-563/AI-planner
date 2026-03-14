import requests

def count_files(url):

    response = requests.get(url)
    items = response.json()

    total = 0

    for item in items:

        if item["type"] == "file":

            if item["name"].endswith((".cpp",".py",".java",".c")):
                total += 1

        elif item["type"] == "dir":

            total += count_files(item["url"])

    return total


def count_solved_problems():

    owner = "Harshit-563"
    repo = "DSA"

    url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    return count_files(url)