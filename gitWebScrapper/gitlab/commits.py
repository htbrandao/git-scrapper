import requests
from gitWebScrapper import logger
from gitWebScrapper.gitlab import GITLAB_API_BASE_URL, ACCESS_TOKEN

COMMIT_API_URL = GITLAB_API_BASE_URL + '/projects/{}/repository/commits?ref_name={}'
BRANCH_COMMITS_SEARCH_API_URL = GITLAB_API_BASE_URL + '/projects/{}/repository/commits?ref_name={}&per_page=100&page={}'

HEADER = {'Private-Token': '{}'.format(ACCESS_TOKEN)}


def parse_single_commit(commit: dict):
    return {
        'sha': commit['id'],
        'html_url': commit['web_url'],
        'author': commit['author_name'],
        'email': commit['author_email'],
        'date': commit['created_at'],
        'message': commit['message']
    }


def parse_multiple_commits(commits: list):
    return [parse_single_commit(commit) for commit in commits]


def get_single_commit(repo_id: str, commit_sha: str):
    commit = requests.get(url=COMMIT_API_URL.format(repo_id, commit_sha), headers=HEADER).json()
    return parse_single_commit(commit)


def get_all_commits(repo_id: str, branch='master'):
    """
    Gets the commits from desired user's repository.

    :param repo_id: repo id
    :param branch: repo's branch name
    :return:
    """
    page = 1
    commits = []
    while True:
        more_commits = requests.get(url=BRANCH_COMMITS_SEARCH_API_URL.format(repo_id, branch, page), headers=HEADER).json()
        if len(more_commits) != 0:
            for one_commit in more_commits:
                commits.append(one_commit)
            page += 1
        else:
            break
    return parse_multiple_commits(commits)
