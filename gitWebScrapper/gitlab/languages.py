import requests
from gitWebScrapper import logger
from gitWebScrapper.gitlab import GITLAB_API_BASE_URL, ACCESS_TOKEN

LANGUAGES_API_URL = GITLAB_API_BASE_URL + '/projects/{}/languages'

HEADER = {'Private-Token': '{}'.format(ACCESS_TOKEN)}


def get_languages(repo_id: str):
    """
    Gets the languages used in desired repository.

    :param repo_id: repo id
    :return: dict
    """
    return requests.get(url=LANGUAGES_API_URL.format(repo_id), headers=HEADER).json()
