FROM alpine:3.9

ENV DST_HOST="127.0.0.1"
ENV DST_PORT="443"
ENV SRC_PORT="80"

RUN apk add socat

EXPOSE ${SRC_PORT}

ENTRYPOINT ["sh","-c","socat TCP-LISTEN:${SRC_PORT},fork,reuseaddr OPENSSL:${DST_HOST}:${DST_PORT},verify=0"]
