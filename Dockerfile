FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install

WORKDIR /code
COPY backend/requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ADD backend/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
