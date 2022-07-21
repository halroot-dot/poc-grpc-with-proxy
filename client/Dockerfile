FROM python:3

WORKDIR /app

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install grpcio google-api-python-client

EXPOSE 50051

COPY ./ssl /app/../ssl
COPY ./client .
CMD [ "python3", "-u", "greeter_client.py" ]