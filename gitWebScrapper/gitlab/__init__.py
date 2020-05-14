from os import getenv
from gitWebScrapper import logger

GITLAB_API_BASE_URL = 'https://gitlab.com/api/v4'


def check_token():
    token = getenv('ACCESS_TOKEN_LAB')
    if token is None:
        logger.error('ACCESS_TOKEN_LAB not found')
    return token


ACCESS_TOKEN = check_token()