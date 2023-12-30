FROM alpine:3.14.2

ARG TARGET_ARCH=arm64
ARG TARGET_OS=linux

RUN apk add --no-cache curl bash

# Install argocd-vault-plugin
RUN curl -sL https://github.com/argoproj-labs/argocd-vault-plugin/releases/download/v1.17.0/argocd-vault-plugin_1.17.0_${TARGET_OS}_${TARGET_ARCH} -o /usr/local/bin/argocd-vault-plugin \
    && chmod +x /usr/local/bin/argocd-vault-plugin

# Install Kustomize
RUN curl -sL https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v5.2.1/kustomize_v5.2.1_${TARGET_OS}_${TARGET_ARCH}.tar.gz -o /tmp/kustomize.tar.gz \
    && tar -xzf /tmp/kustomize.tar.gz -C /usr/local/bin \
    && chmod +x /usr/local/bin/kustomize \
    && rm /tmp/kustomize.tar.gz

# Install Helm
RUN curl -sL https://get.helm.sh/helm-v3.13.3-${TARGET_OS}-${TARGET_ARCH}.tar.gz -o /tmp/helm.tar.gz \
    && tar -xzf /tmp/helm.tar.gz -C /usr/local/bin \
    && chmod +x /usr/local/bin/helm \
    && rm /tmp/helm.tar.gz

RUN addgroup -g 1000 argocd && adduser -u 1000 -G argocd -D -s /bin/sh -h /home/argocd argocd

USER argocd
WORKDIR /home/argocd
