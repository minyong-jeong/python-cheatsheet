import requests

REPO = "https://api.github.com/repos/minyong-jeong/python-cheatsheet/contents"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}


def get_python_list():
    python_list = {}
    response = requests.get(REPO, headers=HEADERS)
    contents = response.json()
    for content in contents:
        name = content["name"]
        url = content["html_url"]
        if name.endswith(".py"):
            python_list[name] = url
    return python_list


def write_list_to_jsfile(python_list):
    with open("data.js", "w") as f:
        f.write("const PYTHON_LIST = " + str(python_list))


if __name__ == "__main__":
    python_list = get_python_list()
    write_list_to_jsfile(python_list)
