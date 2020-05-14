import csv
import json
import logging
from datetime import datetime

def create_logger(name: str):
    """
    Sets up a logger.

    :param name: name of the logger
    :return: logger on /tmp/LOGGERNAME.log
    """
    log_format = '%(name)s | %(levelname)s | %(asctime)s | %(funcName)s | %(message)s'
    logging.basicConfig(filename='/tmp/{}.log'.format(name), filemode='a', format=log_format)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def load_config(file_path: str):
    """
    Reads a JSON config file.

    :param file_path: str
    :return: dict
    """
    logger.info('Loading {}'.format(file_path))
    with open(file_path) as config_file:
        config = json.load(config_file)
    return config


def load_users(file: str):
    """
    Reads CSV file with a git user id on each line.

    :param file: csv file location
    :return: list
    """
    logger.info('Generating users list from {}'.format(file))
    with open(file=file, mode='r') as f:
        users_list = []
        for user in list(csv.reader(f)):
            users_list.append(user[0])
    logger.info('Found {} user(s)'.format(len(users_list)))
    return users_list


def dump_json_handler(output_abs_path: str, data):
    """
    Handler for writing scrapper output to file

    :param output_abs_path: output file absolute path
    :param data: list(dict)
    :return: None
    """
    if (isinstance(output_abs_path, str) and len(output_abs_path) > 0) and (len(data) > 0):
        from gitWebScrapper.output import dump_json
        dump_json(obj=data, absolute_path=output_abs_path)


def scrape_github_handler(users: list, commits=False):
    """
    Handler for scraping GitHub users.

    :param users: list of users
    :param commits: boolean value for adding or not commits to output
    :return: None
    """
    from gitWebScrapper.github.scrapper import github_scrapper
    return [github_scrapper(user_id=user, get_commits=commits) for user in users]


def scrape_gitlab_handler(users: list, commits=False):
    """
    Handler for scraping GitLab users.

    :param users: list of users
    :param commits: boolean value for adding or not commits to output
    :return: None
    """
    from gitWebScrapper.gitlab.scrapper import gitlab_scrapper
    return [gitlab_scrapper(user_id=user, get_commits=commits) for user in users]


def scrape(config: str):
    """
    Entrypoint for gitWebScrapper module.

    This needs to be the only function called outside this module.

    :param config: path to config file
    :return: None
    """
    t0 = datetime.now()
    cfg = load_config(config)
    git = cfg['git']
    users_list = load_users(file=cfg['users'])
    commits = cfg['commits']
    output_abs_path = cfg['output']
    if git == 'hub':
        logger.info('Started scrape_github_handler')
        data = scrape_github_handler(users=users_list, commits=commits)
        dump_json_handler(output_abs_path=output_abs_path, data=data)
    elif git == 'lab':
        logger.info('Started scrape_gitlab_handler')
        data = scrape_gitlab_handler(users=users_list, commits=commits)
        dump_json_handler(output_abs_path=output_abs_path, data=data)
    elif git == 'intranet':
        logger.warning('Handler not implemented yet!')
    else:
        logger.error('Unknown Git Repository: {}'.format(git))
    logger.info('Done. Runtime: {}'.format(datetime.now() - t0))

logger = create_logger('{}'.format(__name__))
