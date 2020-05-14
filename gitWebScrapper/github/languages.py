import requests
from gitWebScrapper import logger
from gitWebScrapper.github import GITHUB_API_BASE_URL, ACCESS_TOKEN

LANGUAGES_API_URL = GITHUB_API_BASE_URL + '/repos/{}/{}/languages'
HEADER = {'Authorization': 'token {}'.format(ACCESS_TOKEN)}


def get_languages(user_id: str, repo: str):
    """
    Gets the languages used in desired repository.

    :param user_id: git user id
    :param repo: user's repository name
    :return: dict
    """
    return requests.get(url=LANGUAGES_API_URL.format(user_id, repo), headers=HEADER).json()
