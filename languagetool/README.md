
# Build

```bash
docker build --platform linux/arm64 -t languagetool:4.7 --build-arg LANGTOOL_VERS=4.7x .
```

# Performance testing

```bash
docker run -it -v $PWD/test:/test --rm --network host grafana/k6:0.45.0 run /test/performance.js
```
