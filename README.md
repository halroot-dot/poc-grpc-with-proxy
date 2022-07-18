# poc-grpc-with-proxy

grpc に TLS proxy を利用した構成の実現方法調査

### 構成

```mermaid
graph LR
  client["client"]
  envoy1["envoy1"]
  envoy2["envoy2"]
  server["server"]

  subgraph PC
    client --no TLS:8080--> envoy1 --TLS:50051--> envoy2 --no TLS:50052-->server
  end
```

#### Usage

get envoy binary

```console
docker cp `docker create envoyproxy/envoy-dev:latest`:/usr/local/bin/envoy .
```

1. Start gRPC Server

```console
python server/greeter_server.py
```

2. Start Envoy Server Proxy

```console
./envoy -c proxy/envoy_server.yaml --base-id 0 -l debug
```

3. Start Envoy Client Proxy

```console
./envoy  -c proxy/envoy_client.yaml --base-id 1 -l debug
```

4. Start gRPC Client

```console
python client/greeter_client.py
```

## WIP

### 8080/tcp を nginx が listen しているか確認する方法

```console
$ ss -tanl | grep 8080
LISTEN 0 128 *:8080 *:*

$ ss -tanlp | grep 8080
LISTEN 0 128 *:8080 *:* users:*1
```

### パケットキャプチャ

```console
$ tcpdump -i any tcp port 8080 or tcp port 50051 -w /tmp/grpc.pcap
```
