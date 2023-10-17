#!/bin/bash
cd ..
fileEnv="docker-compose.yaml"
echo "Deploying docker-compose.yaml"
docker-compose -f docker-compose.yaml -f $fileEnv up --build 