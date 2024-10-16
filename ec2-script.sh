#!/usr/bin/env bash

cd /home/ec2-user/world-of-games
docker-compose -f docker-compose.yaml up --detach
cat scores.txt