#!/usr/bin/bash

VERSION=`curl 'https://petstore.swagger.io/v2/swagger.json' | jq '.swagger'`
echo $VERSION
if [ "$VERSION" = '"2.0"' ]; then
  echo "Swagger version is fine"
  exit 0
fi
echo "Swagger version is incorrect"
exit -1
