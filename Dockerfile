FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3 python3-pip

RUN pip3 install Flask requests urllib3

ENV FLASK_APP hello.py

COPY . /app
WORKDIR /app

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
