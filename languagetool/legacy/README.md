
- Commit: https://github.com/lokalise/languagetool-int/blob/b4d608128e0a396d2ba407a3a1193b508fb16be7/infra/Dockerfile
- Dockerfile: https://github.com/Erikvl87/docker-languagetool/blob/v4.7/Dockerfile

# Build image

- Debian ( amd64 )
```bash
docker build -t languagetool:5.0-fastText \
  --platform amd64 \
  --build-arg LANGTOOL_ZIP_URL=https://languagetool.org/download/LanguageTool-5.0.zip \
  -f Dockerfile.fasttext .
```

- Alpine ( amd64 )
```bash
docker buildx build -t languagetool:5.0-alpine-fastText \
  --no-cache \
  --build-arg LANGTOOL_ZIP_URL=https://languagetool.org/download/LanguageTool-5.0.zip \
  --platform linux/amd64 \
  -f Dockerfile.alpine-fasttext .
```

# Start container

```bash
docker run -d -v ${PWD}/server.properties:/srv/server.properties:ro -p 8010:8010 -d languagetool:5.0-alpine-fastText
```

# Launch load test

```bash
docker run -it -v ${PWD}/../test:/test --rm --network host grafana/k6:0.45.0 run /test/performance.js
```
