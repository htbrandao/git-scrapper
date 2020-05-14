import requests
from gitWebScrapper import logger
from gitWebScrapper.gitlab import GITLAB_API_BASE_URL, ACCESS_TOKEN

BRANCHES_API_URL = GITLAB_API_BASE_URL + '/projects/{}/repository/branches'

HEADER = {'Private-Token': '{}'.format(ACCESS_TOKEN)}


def parse_branch(branch: dict):
    return {'name': branch['name'], 'sha': branch['commit']['id']}


def get_branches(repo_id: str):
    """
    Gets the branches from desired repository.

    :param repo_id: repo id
    :return: list(dict)
    """
    branches = requests.get(url=BRANCHES_API_URL.format(repo_id), headers=HEADER).json()
    return [parse_branch(branch) for branch in branches]
