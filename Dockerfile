FROM python:3

RUN mkdir /app

COPY . /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

RUN rm -rf /root/.cache/pip/*
RUN rm -rf /usr/local/src/*
RUN rm -rf /var/cache/*
RUN rm -rf /root/.cache/*

RUN mkdir /config
RUN mkdir /data
RUN mkdir /dump
RUN chmod -R 777 /config
RUN chmod -R 777 /data
RUN chmod -R 777 /dump

VOLUME [ "/config", "/data", "/dump" ]

WORKDIR /app

ENV ACCESS_TOKEN_HUB 'FILL_THIS_IN'
ENV ACCESS_TOKEN_LAB 'FILL_THIS_IN'

CMD ["python3", "main.py"]

# docker build . -t gitwebscrapper:0.1
# docker container rm -f gitwebscrapper; docker run --name gitwebscrapper -v /tmp/gitWebScrapper/config:/config/ -v /tmp/gitWebScrapper/dados:/data -v /tmp/gitWebScrapper/dump:/dump -d gitwebscrapper:0.1 && docker ps
