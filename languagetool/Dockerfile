FROM alpine:3.17

ARG LANGTOOL_VERS="stable"

RUN addgroup languagetool && adduser  -h /languagetool -s /dev/zero -H -u 1000 -G languagetool -D languagetool

RUN apk add curl openjdk11-jre-headless bash

# Install NewRelic
ARG NEWRELIC_ZIP_URL=https://download.newrelic.com/newrelic/java-agent/newrelic-agent/current/newrelic-java.zip

WORKDIR /srv
RUN curl -O "$NEWRELIC_ZIP_URL"; \
    unzip -q newrelic-java.zip; \
    rm newrelic-java.zip; \
    mkdir -p /srv/newrelic/logs

# Install Languagetool
RUN mkdir /languagetool

WORKDIR /languagetool

RUN curl -sL https://languagetool.org/download/LanguageTool-${LANGTOOL_VERS}.zip -o /tmp/LanguageTool-${LANGTOOL_VERS}.zip && \
    unzip /tmp/LanguageTool-${LANGTOOL_VERS}.zip -d /languagetool && \
    rm -rf LanguageTool-${LANGTOOL_VERS}.zip && \
    mv LanguageTool-*/* . && \
    rm -rf LanguageTool-*

COPY entrypoint.sh .
COPY server.properties .
RUN chmod +x entrypoint.sh

RUN chown -R languagetool.languagetool .
RUN chown -R languagetool.languagetool /srv
USER languagetool

ENTRYPOINT ["./entrypoint.sh","$@"]
#ENTRYPOINT ["java","-cp","languagetool-server.jar","org.languagetool.server.HTTPServer","--public","--port","8010"]
#CMD ["--port","8010","--public","--allow-origin"]
