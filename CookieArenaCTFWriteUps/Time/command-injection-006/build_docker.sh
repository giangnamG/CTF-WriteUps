#!/bin/bash
docker rm -f command-injection-006
docker build -t command-injection-006 . && \
docker run --name=command-injection-006 --rm -p1337:1337 -it command-injection-006