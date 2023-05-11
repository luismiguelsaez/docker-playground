
- Commit: https://github.com/lokalise/languagetool-int/blob/b4d608128e0a396d2ba407a3a1193b508fb16be7/infra/Dockerfile
- Dockerfile: https://github.com/Erikvl87/docker-languagetool/blob/v4.7/Dockerfile

## Build

```bash
docker build --platform amd64 -t 053497547689.dkr.ecr.eu-central-1.amazonaws.com/languagetool-int/app:4.7-amd64 .
docker build --platform arm64 -t 053497547689.dkr.ecr.eu-central-1.amazonaws.com/languagetool-int/app:4.7-arm64 .
```

## Push

```bash
docker push 053497547689.dkr.ecr.eu-central-1.amazonaws.com/languagetool-int/app:4.7-amd64
docker push 053497547689.dkr.ecr.eu-central-1.amazonaws.com/languagetool-int/app:4.7-arm64
```

## Run

```bash
docker run -p 8010:8010 -d -e IS_NEWRELIC_ENABLED=true -e NEWRELIC_LICENSE_KEY=test 053497547689.dkr.ecr.eu-central-1.amazonaws.com/languagetool-int/app:4.7-arm64

curl 'localhost:8010/v2/check?text=voila&language=fr'
```

## Deploy

- https://prod-ci.lokalise.work/job/langtool/job/promote/
  - `4.7-arm64`


# Issue libgomp?

```bash
docker build --platform amd64 -t 053497547689.dkr.ecr.eu-central-1.amazonaws.com/languagetool/app:4.7 .
```

```bash
docker run -d -p 8010:8010 053497547689.dkr.ecr.eu-central-1.amazonaws.com/languagetool/app:4.7
```
