FROM python:3.9-alpine

LABEL Description="CI/CD AWS builder with awscli and aws-sam-cli"

RUN apk add make gcc musl-dev openssl-dev

ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

RUN adduser -h /home/app -D -u 1000 app
USER app
WORKDIR /home/app
