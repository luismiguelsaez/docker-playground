
- Commit: https://github.com/lokalise/languagetool-int/blob/b4d608128e0a396d2ba407a3a1193b508fb16be7/infra/Dockerfile
- Dockerfile: https://github.com/Erikvl87/docker-languagetool/blob/v4.7/Dockerfile

# Build image

```bash

```bash
docker build -t languagetool:5.0-fastText \
  --build-arg LANGTOOL_ZIP_URL=https://languagetool.org/download/LanguageTool-5.0.zip -f Dockerfile.fasttext .
```

# Start container

```bash
docker run -v ${PWD}/projects/k8s/langtool/perf/server.properties:/srv/server.properties:ro -p 8010:8010 -d 053497547689.dkr.ecr.eu-central-1.amazonaws.com/languagetool/app:6.2-SNAPSHOT
```

# Launch load test

```bash
docker run -it -v ${PWD}/projects/k8s/langtool/perf:/test --rm --network host grafana/k6:0.45.0 run /test/performance_tuning.js
```
