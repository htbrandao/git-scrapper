# Git web scrapper

Tool for automating GitHub and GitLab public info extraction. You can run it directly or as a container.

This app, currently, gathers the following information about an user: User projects (repos), branches, languages and commits

# I - Standard:

1- pip3 install -r requirements.txt

2- Have a csv (no header) file with git lab/hub user names

3- Create a config.json file and pass it's adress to the function in main.py

4- Set an enviroment variable (`ACCESS_TOKEN_HUB` or `ACCESS_TOKEN_LAB`) with your access token

5- Run it

# II - Dockerized:


1- Fill in your git **hub/lab** token on Dockerfile


2- Create file system folders for: 
- App config: `/LOCAL_FS/CONFIG`
- Input data: `/LOCAL_FS/DATA`
- Output file: `/LOCAL_FS/DUMP`

3- Write down:
- JSON config file on `/LOCAL_FS/CONFIG`
- CSV file (no header) withe the users you want to parse data from on `/LOCAL_FS/DATA`

4- Build:
    
```bash
$ docker build . -t gitwebscrapper:0.1
```

5- Run:

```bash
$ docker container rm -f gitwebscrapper

$ docker run --name gitwebscrapper -v /LOCAL_FS/CONFIG:/config/ -v /LOCAL_FS/DATA:/data -v /LOCAL_FS/DUMP:/dump -d gitwebscrapper:0.1

$ docker logs gitwebscrapper
```

# config.json

    {
        "git": "lab",                           # either 'lab' or 'hub'
        "commits": true,                        # true/false to add user's commit history
        "users": "/data/users_lab.csv",         # csv (no header) list of users to parse data
        "output": "/dump/dump.json"             # output file. leave blank ("") for no output file
    }

Make sure that the `folders` on config.json match the ones you mount when you run the cointainer.
