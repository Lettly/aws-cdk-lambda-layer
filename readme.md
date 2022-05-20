# aws-cdk-lambda-layer
Generate a lambda layer for serverless framework 

## Source
The original file come form [AWS CLI](https://github.com/aws/aws-cdk/tree/master/packages/%40aws-cdk/lambda-layer-awscli)

The CLI will be installed under `/opt/awscli/aws`.

## Build 
To build the layer, run: 
    `node layer-generator/build.js` for the home directory.

## To install the dependencies
To install the dependencies, run: 
    `npm install` for the home directory.

## To build and deploy
To deploy the layer, run: 
    `npm deploy` for the home directory.