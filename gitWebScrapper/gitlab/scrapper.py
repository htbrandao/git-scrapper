from gitWebScrapper import logger
from gitWebScrapper.gitlab.projects import get_user_projects
from gitWebScrapper.gitlab.languages import get_languages
from gitWebScrapper.gitlab.branches import get_branches
from gitWebScrapper.gitlab.commits import get_all_commits


def gitlab_scrapper(user_id: str, get_commits=False):
    """
    Main function for GitLab submodule.

    This needs to be the only function called outside this submodule.

    :param user_id: git user id
    :param get_commits: boolean value for adding or not commits to output
    :return: list(dict)
    """
    logger.info('Scrapping \'{}\' @ GitLab, commits={}'.format(user_id, get_commits))
    projects = get_user_projects(user_id=user_id)
    for repo in projects['repos']:
        repo['languages'] = get_languages(repo_id=repo['id'])
        repo['branches'] = get_branches(repo_id=repo['id'])
        if get_commits:
            for branch in repo['branches']:
                branch['commits'] = get_all_commits(repo_id=repo['id'], branch=branch['name'])
    return projects
