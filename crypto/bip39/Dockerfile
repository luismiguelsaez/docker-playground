FROM python:3.9-alpine

ARG VERSION="0.5.4"
ARG PORT="8000"

RUN mkdir /app
RUN wget https://github.com/iancoleman/bip39/archive/refs/tags/${VERSION}.tar.gz -Obip39.tar.gz && \
    tar -xzf bip39.tar.gz -C /app && \
    rm bip39.tar.gz

RUN adduser -h /app -s /bin/nologin -u 1000 -D app
RUN chown -R app.app /app

WORKDIR /app/bip39-${VERSION}/src

EXPOSE 8000

USER app

ENTRYPOINT ["python3","-m","http.server","--bind","0.0.0.0","8000"]
