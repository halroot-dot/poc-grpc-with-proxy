# poc-grpc-with-proxy

grpc に proxy を利用した構成の実現方法調査

## Usage 1

server

```console
cd example/server
python greeter_server.py
```

client

```console
cd example/client
python greeter_client.py
```

## Usage 2

server

```console
cd example
docker compose up
```

client

```console
cd example/client
python greeter_client.py
```
