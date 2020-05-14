import requests
from gitWebScrapper import logger
from gitWebScrapper.github import GITHUB_API_BASE_URL, ACCESS_TOKEN

COMMIT_API_URL = GITHUB_API_BASE_URL + '/repos/{}/{}/git/commits/{}'
BRANCH_COMMITS_API_URL = GITHUB_API_BASE_URL + '/repos/{}/{}/commits?branch={}&per_page=100'
BRANCH_COMMITS_SEARCH_API_URL = GITHUB_API_BASE_URL + '/repos/{}/{}/commits?branch={}&sha={}&per_page=100'

HEADER = {'Authorization': 'token {}'.format(ACCESS_TOKEN)}


def parse_single_commit(commit: dict):
    return {
        'sha': commit['sha'],
        'html_url': commit['html_url'],
        'author': commit['commit']['author']['name'],
        'email': commit['commit']['author']['email'],
        'date': commit['commit']['author']['date'],
        'message': commit['commit']['message']
    }


def parse_multiple_commits(commits: list):
    return [parse_single_commit(commit) for commit in commits]


def get_single_commit(user_id: str, repo: str, commit_sha: str):
    commit = requests.get(url=COMMIT_API_URL.format(user_id, repo, commit_sha), headers=HEADER).json()
    return parse_single_commit(commit)


def get_all_commits(user_id: str, repo: str, branch='master'):
    """
    Gets the commits from desired user's repository.

    :param user_id: git user id
    :param repo: user's repository name
    :param branch: repo's branch name
    :return:
    """
    url = BRANCH_COMMITS_API_URL.format(user_id, repo, branch)
    commits = requests.get(url=url, headers=HEADER).json()
    if commits[0]['sha'] == commits[-1]['sha']:
        return parse_multiple_commits(commits)
    else:
        oldest_relative_sha = commits[-1]['sha']
        while True:
            url = BRANCH_COMMITS_SEARCH_API_URL.format(user_id, repo, branch, oldest_relative_sha)
            more_commits = requests.get(url=url, headers=HEADER).json()
            newest_relative_sha = more_commits[0]['sha']
            more_commits = more_commits[1:]
            if len(more_commits) == 0:
                break
            for one_commit in more_commits:
                commits.append(one_commit)
            oldest_relative_sha = more_commits[-1]['sha']
            if newest_relative_sha == oldest_relative_sha:
                break
    return parse_multiple_commits(commits)
