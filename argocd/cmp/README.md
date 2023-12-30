
## Build

```bash
docker buildx build --push -t luismiguelsaez/argocd-cmp-default:v0.0.3 --build-arg TARGET_OS=linux --build-arg TARGET_ARCH=arm64 .
```
