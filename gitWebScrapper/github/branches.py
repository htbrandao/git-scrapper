import requests
from gitWebScrapper import logger
from gitWebScrapper.github import GITHUB_API_BASE_URL, ACCESS_TOKEN

BRANCHES_API_URL = GITHUB_API_BASE_URL + '/repos/{}/{}/branches'
HEADER = {'Authorization': 'token {}'.format(ACCESS_TOKEN)}


def parse_branch(branch: dict):
    return {'name': branch['name'], 'sha': branch['commit']['sha']}


def get_branches(user_id: str, repo: str):
    """
    Gets the branches from desired repository.

    :param user_id: git user id
    :param repo: user's repository name
    :return: list(dict)
    """
    branches = requests.get(url=BRANCHES_API_URL.format(user_id, repo), headers=HEADER).json()
    return [parse_branch(branch) for branch in branches]
