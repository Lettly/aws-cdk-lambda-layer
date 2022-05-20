#!/bin/bash

cd layer-generator

echo ">> Building AWS Lambda layer inside a docker image..."

TAG='aws-lambda-layer'

docker build -t ${TAG} .

echo ">> Extracting layer.zip from the build container..."
CONTAINER=$(docker run -d ${TAG} false)
docker cp ${CONTAINER}:/layer.zip ../.layer-build.zip


echo ">> Stopping container..."
docker rm -f ${CONTAINER}
echo ">> .layer-build.zip is ready"
