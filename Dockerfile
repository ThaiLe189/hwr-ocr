FROM python:3.7
LABEL maintainer "ThaiLe"

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
#RUN python3 -m venv /opt/venv 
RUN apt-get -y install python3-pip

RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel

RUN apt-get -y update\
    && apt-get -y install git\
    && apt-get install ffmpeg libsm6 libxext6  -y\
    && find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' + \
    && runDeps="$( \
    scanelf --needed --nobanner --recursive /usr/local \
    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
    | sort -u \
    | xargs -r apk info --installed \
    | sort -u \
    )"

RUN mkdir -p /api
WORKDIR /api
COPY . /api
RUN pip install -r requirements.txt

CMD ["bash", "docker-entrypoint.sh"]