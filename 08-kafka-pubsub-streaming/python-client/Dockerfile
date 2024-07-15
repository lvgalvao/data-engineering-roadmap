FROM --platform=amd64 python:3.8-alpine
RUN pip install kafka-python Faker
ENV ACTION produce
ENV BOOTSTRAP_SERVERS "broker-1:29091,broker-2:29092,broker-3:29093"
ADD consume.py /src/consume.py
ADD produce.py /src/produce.py
ADD run.sh /src/run.sh
CMD ["sh", "/src/run.sh", "$ACTION"]
