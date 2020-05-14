from gitWebScrapper import logger
from gitWebScrapper.github.projects import get_user_projects
from gitWebScrapper.github.languages import get_languages
from gitWebScrapper.github.branches import get_branches
from gitWebScrapper.github.commits import get_all_commits


def github_scrapper(user_id: str, get_commits=False):
    """
    Main function for GitHub submodule.

    This needs to be the only function called outside this submodule.

    :param user_id: git user id
    :param get_commits: boolean value for adding or not commits to output
    :return: list(dict)
    """
    logger.info('Scrapping \'{}\' @ GitHub, commits={}'.format(user_id, get_commits))
    projects = get_user_projects(user_id=user_id)
    for repo in projects['repos']:
        repo['languages'] = get_languages(user_id=user_id, repo=repo['name'])
        repo['branches'] = get_branches(user_id=user_id, repo=repo['name'])
        if get_commits:
            for branch in repo['branches']:
                branch['commits'] = get_all_commits(user_id=user_id, repo=repo['name'], branch=branch['name'])
    return projects
