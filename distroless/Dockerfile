FROM alpine:3.12 AS builder

RUN apk update && apk add vault

FROM scratch

COPY --from=builder /lib/ld-musl-aarch64.so.1 /lib/
COPY --from=builder /usr/sbin/vault /usr/sbin/
COPY --from=builder /bin/sh /bin/

ENTRYPOINT [ "/bin/sh" ]
