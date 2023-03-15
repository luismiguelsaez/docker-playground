FROM alpine:3.17

RUN addgroup languagetool && adduser  -h /languagetool -s /dev/zero -H -u 1000 -G languagetool -D languagetool

RUN apk add curl openjdk8-jre

RUN mkdir /languagetool

WORKDIR /languagetool

RUN curl -sL https://languagetool.org/download/LanguageTool-stable.zip -o /tmp/LanguageTool-stable.zip && \
    unzip /tmp/LanguageTool-stable.zip -d /languagetool && \
    rm -rf LanguageTool-stable.zip && \
    mv LanguageTool-*/* . && \
    rm -rf LanguageTool-*

RUN chown -R languagetool.languagetool .
USER languagetool

ENTRYPOINT ["java","-cp","languagetool-server.jar","org.languagetool.server.HTTPServer"]
CMD ["--port","8010","--public","--allow-origin"]
