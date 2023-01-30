FROM python:3.7-slim-buster as builder
RUN python3 -m venv /opt/venv 
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel
COPY requirements.txt .

RUN pip3 install -r requirements_api.txt \
    pip3 install pip-autoremove && \
    pip3 uninstall pip-autoremove -y

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

RUN mkdir /api
WORKDIR /api
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . .