import requests
from gitWebScrapper import logger
from gitWebScrapper.gitlab import GITLAB_API_BASE_URL, ACCESS_TOKEN

PROJECTS_API_URL = GITLAB_API_BASE_URL + '/users/{}/projects'

HEADER = {'Private-Token': '{}'.format(ACCESS_TOKEN)}


def get_user_projects(user_id: str):
    """
    Gets the projects from desired user.

    :param user_id: git user id
    :return: list(dict)
    """
    repos = requests.get(url=PROJECTS_API_URL.format(user_id), headers=HEADER).json()
    d = {'user_id': user_id, 'repos': []}
    for repo in repos:
        d['repos'].append({
            'id': repo['id'],
            'name': repo['name'],
            'web_url': repo['web_url'],
            'http_url_to_repo': repo['http_url_to_repo'],
            'created_at': repo['created_at'],
            'last_activity_at': repo['last_activity_at'],
        })
    return d
