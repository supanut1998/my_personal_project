FROM apache/airflow:2.1.4
USER airflow
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --user -r /tmp/requirements.txt