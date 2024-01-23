FROM apache/airflow:2.8.0-python3.8

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
        git \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow

COPY requirements.txt requirements.txt
RUN pip install --user -r requirements.txt
