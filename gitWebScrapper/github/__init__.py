from os import getenv
from gitWebScrapper import logger

GITHUB_API_BASE_URL = 'https://api.github.com'


def check_token():
    token = getenv('ACCESS_TOKEN_HUB')
    if token is None:
        logger.error('ACCESS_TOKEN_HUB not found')
    return token


ACCESS_TOKEN = check_token()
