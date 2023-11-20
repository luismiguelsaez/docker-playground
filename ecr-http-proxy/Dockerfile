FROM openresty/openresty:1.19.9.1-12-alpine

RUN apk add aws-cli

RUN addgroup app && adduser -h /usr/local/openresty -S -G app app

RUN mkdir /usr/local/openresty/.aws && chown -R app:app /usr/local/openresty
