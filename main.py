from gitWebScrapper import scrape

if __name__ == '__main__':
    """
    Example json config file:

        {
            "git": "lab",
            "commits": true,
            "users": "/data/users_lab.csv",
            "output": "/dump/dump.json"
        }

    """
    scrape(config='/config/config.json')
