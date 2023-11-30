FROM alpine:3.14.2

RUN apk add --no-cache bash

COPY entrypoint.sh /entrypoint.sh
COPY console.sh /console
RUN chmod +x /entrypoint.sh /console

ENTRYPOINT [ "/entrypoint.sh" ]
