FROM python:3.8-alpine

RUN apk update && apk upgrade

RUN apk add bash \
            vim \
            pkgconfig \
            git \
            gcc \
            libcurl \
            libc-dev \
    && rm -rf /var/cache/apk/*


WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", ":8001", "memorize.wsgi:application"]