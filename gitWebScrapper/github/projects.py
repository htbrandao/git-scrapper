import requests
from gitWebScrapper import logger
from gitWebScrapper.github import GITHUB_API_BASE_URL, ACCESS_TOKEN

PROJECTS_API_URL = GITHUB_API_BASE_URL + '/users/{}/repos'
HEADER = {'Authorization': 'token {}'.format(ACCESS_TOKEN)}


def get_user_projects(user_id: str):
    """
    Gets the projects from desired user.

    :param user_id: git user id
    :return: list(dict)
    """
    repos = requests.get(url=PROJECTS_API_URL.format(user_id), headers=HEADER).json()
    d = {'user_id': user_id, 'repos': []}
    for repo in repos:
        d['repos'].append(
            {
                'name': repo['name'],
                'id': repo['id'],
                'html_url': repo['html_url'],
                'clone_url': repo['clone_url'],
                'created_at': repo['created_at'],
                'updated_at': repo['updated_at'],
            }
        )
    return d
