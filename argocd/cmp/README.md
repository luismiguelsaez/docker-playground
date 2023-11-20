
## Build

```bash
docker buildx build --push -t luismiguelsaez/argocd-cmp-default:latest --build-arg TARGET_OS=linux --build-arg TARGET_ARCH=arm64 .
```
