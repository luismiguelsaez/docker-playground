FROM openjdk:11 as base


FROM base as build

ARG LANGTOOL_ZIP_URL=https://lokalise-live-lok-app-main-assets.s3.eu-central-1.amazonaws.com/languagetool-lokalise-3.zip
ARG NEWRELIC_ZIP_URL=https://download.newrelic.com/newrelic/java-agent/newrelic-agent/current/newrelic-java.zip

WORKDIR /srv

# Download and install dependencies
RUN apt-get update && \
    curl -o languagetool-lokalise.zip "$LANGTOOL_ZIP_URL" && \
    unzip -q languagetool-lokalise.zip && \
    rm languagetool-lokalise.zip && \
    curl -O "$NEWRELIC_ZIP_URL" && \
    unzip -q newrelic-java.zip && \
    rm newrelic-java.zip && \
    mkdir -p /srv/newrelic/logs


FROM base as app

RUN groupadd languagetool && useradd -d /srv/languagetool-lokalise -g languagetool -s /dev/null languagetool

# Copy from build phase
COPY --from=build /srv /srv

# Set workdir and copy external files
WORKDIR /srv/languagetool-lokalise

# Fix libgomp1 error
RUN apt-get -y update && apt-get install -y libgomp1

COPY server.properties .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh
RUN chown -R languagetool.languagetool .

USER languagetool

ENTRYPOINT [ "./entrypoint.sh" ]