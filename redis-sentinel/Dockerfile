FROM golang:1.17.3-alpine

RUN go install github.com/RedisLabs/sentinel_tunnel@latest

COPY conf/sentinel-tunnel/tunnel.conf /etc/tunnel.conf

ENTRYPOINT ["sentinel_tunnel","/etc/tunnel.conf","/dev/stdout"]
