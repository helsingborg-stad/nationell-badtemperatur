#!/usr/bin/env bash
docker buildx build --platform linux/amd64 -t mrspex/badtemp:latest ../
docker push mrspex/badtemp:latest
ssh 151946-10742@gate.jelastic.elastx.net -p 3022 ./docker/update_badtemp.sh
