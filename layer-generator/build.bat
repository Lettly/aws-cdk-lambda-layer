@echo off

cd "layer-generator"

echo ">> Building AWS Lambda layer inside a docker image..."
SET TAG=aws-lambda-layer

docker build -t "%TAG%" "."
echo ">> Extracting layer.zip from the build container..."
for /f %%i in ('docker run -d %TAG% false') do set CONTAINER=%%i

docker cp "%CONTAINER%:\layer.zip" "..\.layer-build.zip"

echo ">> Stopping container..."

docker rm -f "%CONTAINER%"

echo ">> %CD%layer-build.zip is ready"

pause