FROM python:3.9-alpine

ARG VERSION="0.5.4"

RUN mkdir /app
RUN wget https://github.com/iancoleman/bip39/archive/refs/tags/${VERSION}.tar.gz -Obip39.tar.gz && \
    tar -xzf bip39.tar.gz -C /app && \
    rm bip39.tar.gz

WORKDIR /app/${VERSION}

EXPOSE 8000

ENTRYPOINT ["python3","-m","http.server","8000","--bind","0.0.0.0"]
