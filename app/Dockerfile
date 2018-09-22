FROM debian:stretch

ARG UID=1000
ARG GID=1000

RUN groupadd --gid $GID -r pocik && useradd --uid $UID --create-home --system -g pocik pocik \
    && mkdir -p /var/collected_static \
    && chown -R pocik:pocik /var/collected_static \
    && mkdir -p /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python3-pip \
       python3-venv \
       uwsgi \
       uwsgi-plugin-python3 \
       build-essential \
       python3-dev \
       curl \
       binutils \
       libproj-dev \
       gdal-bin \
    && apt-get clean

RUN su pocik -c "python3 -m venv /home/pocik/env"
COPY requirements /app/requirements
RUN su pocik -c ". /home/pocik/env/bin/activate && \
    pip3 install --no-cache-dir -r /app/requirements/development.pip && \
    rm -rf /home/pocik/.cache"

RUN apt-get purge -y python-dev && apt-get autoremove -y

COPY gis_app /app

# Can't use this earlier because python venv would not work after mapping the source code volume.
WORKDIR /app

# Always make the project virtualenv active
ENV VIRTUAL_ENV=/home/pocik/env \
    PATH=/home/pocik/env/bin:$PATH

EXPOSE 8000

# RUN /app/manage.py collectstatic --noinput
USER pocik


ENTRYPOINT ["/app/manage.py"]
CMD ["runserver_plus", "0.0.0.0:8000"]
