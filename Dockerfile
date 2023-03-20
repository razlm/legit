FROM python:3.9-slim
USER root
WORKDIR /app

RUN apt-get update && \
    apt-get install -y default-jdk

COPY requirements.txt .

RUN pip install keycloak
RUN pip install python-keycloak
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

CMD ["python", "app.py"]

