import json
from gitWebScrapper import logger


def dump_json(obj, absolute_path: str):
    """
    Writes the JSON output to a file.

    :param obj: data to be written as a JSON file
    :param absolute_path: aboslute path to write file
    :return: output file absolute path
    """
    with open('{}'.format(absolute_path), 'w') as json_file:
        json.dump(obj, json_file)
        logger.info('Generated {}'.format(absolute_path))
    return absolute_path
