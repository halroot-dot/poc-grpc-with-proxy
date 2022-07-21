#!/bin/bash

set -ue -o pipefail

cd `dirname $0`
cd ssl

CLIENT_CN=cleint-example
SERVER_CN=server-example

# ------------- クライアント -------------
# クライアント用 CA作成
openssl req -new -x509 -nodes -days 365 -subj "/CN=cleint-example-ca" -keyout clientca.key -out clientca.crt

# クライアント秘密鍵作成
openssl genrsa -out client.key

# クライアント秘密鍵用 Certificate Signing Request（CSR） 作成
openssl req -new -key client.key -subj "/CN=localclient" -out client.csr

# クライアント証明書作成
openssl x509 -req -in client.csr -CA clientca.crt -CAkey clientca.key -CAcreateserial -days 365 -out client.crt

# ------------- サーバ -------------

# サーバ用 CA作成
openssl req -new -x509 -nodes -days 365 -subj "/CN=server-example-ca" -keyout serverca.key -out serverca.crt

# サーバ秘密鍵作成
openssl genrsa -out server.key

# サーバ秘密鍵用 Certificate Signing Request（CSR） 作成
openssl req -new -key server.key -subj "/CN=server-example" -out server.csr

# サーバ証明書作成
openssl x509 -req -in server.csr -CA serverca.crt -CAkey serverca.key -CAcreateserial -days 365 -out server.crt