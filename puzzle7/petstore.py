#!/usr/bin/env python

import requests, json, sys

r = requests.get('https://petstore.swagger.io/v2/swagger.json')
if "json" in r.headers["Content-Type"]:
    j = json.loads(r.text)
    print(j, file=sys.stderr)
    version = j["swagger"]
    print(f'"{version}"')
    if version == '2.0':
        print("Swagger version is fine")
        exit(0)

print("Swagger version is incorrect")
exit(-1)
