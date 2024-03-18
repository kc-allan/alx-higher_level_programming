#!/bin/bash
#A script that prints the content length of a http reponse
echo $(curl -sI "https://$1") | $(echo "$res" | grep "Content-Length") | tr -d '\r' | wc -c