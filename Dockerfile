ARG ALPINE_VERSION=latest
FROM alpine:${ALPINE_VERSION}

WORKDIR /app
COPY . /app

RUN set -euxo pipefail ;\
    sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/alpine.global.ssl.fastly.net/g' /etc/apk/repositories ;\
    apk add --no-cache --update python3 ca-certificates openssh-client ;\
    apk add --no-cache --update --virtual .build-deps python3-dev build-base libffi-dev openssl-dev ;\
    pip3 install --default-timeout=100 --no-cache --upgrade pip setuptools ;\
    pip3 install --default-timeout=100 --no-cache -r requirements.txt ;\
    apk del --no-cache --purge .build-deps ;\
    rm -rf /var/cache/apk/* ;\
    rm -rf /root/.cache ;\
    ln -s /usr/bin/python3 /usr/bin/python ;

CMD ["gunicorn", "-w", "3", "main:app", "-b", "0.0.0.0:8080"]