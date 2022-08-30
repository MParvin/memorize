FROM python:3.8-alpine

RUN apk update && apk upgrade

RUN apk add bash \
            vim \
            pkgconfig \
            git \
            gcc \
            libcurl \
            libc-dev \
            postgresql-dev \
            musl-dev \
            python3-dev \
            jpeg-dev \
            zlib-dev \
    && rm -rf "/var/cache/apk/*"


WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/bash", "/code/entrypoint.sh" ]