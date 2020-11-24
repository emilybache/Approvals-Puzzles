#!/usr/bin/env python3

import json
import requests


def main():
    response = requests.get("https://petstore.swagger.io/v2/swagger.json")
    swagger = response.json()
    print(json.dumps(swagger))


if __name__ == "__main__":
    main()