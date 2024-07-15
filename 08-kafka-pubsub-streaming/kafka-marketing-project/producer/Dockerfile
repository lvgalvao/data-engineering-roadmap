FROM python:3.9-slim

WORKDIR /app

COPY producer.py .

RUN pip install faker confluent_kafka

CMD ["python", "producer.py"]
