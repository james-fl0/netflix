FROM python:3.8.0-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY netflix_clone .
COPY entrypoint.sh .

RUN ["chmod", "+x", "entrypoint.sh"]

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
