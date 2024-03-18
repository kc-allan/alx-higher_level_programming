#!/bin/bash
url=$1
res=$(curl -sI "$url")
cont_len=$(echo "$res" | grep "Content-Length") | tr -d '\r' | wc -c
echo "$cont_len"