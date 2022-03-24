FROM golang:1.17.3-alpine

RUN apk add -u jq bash

RUN go install github.com/RedisLabs/sentinel_tunnel@latest

COPY conf/sentinel-tunnel/tunnel.conf /etc/tunnel-template.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
