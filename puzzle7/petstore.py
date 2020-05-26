#!/usr/bin/env python3

import json
from urllib.request import urlopen


def main():
    try:
        url = "http://petstore.swagger.io/v2/swagger.json"
        response = urlopen(url)
        swagger = response.read().decode("utf-8")
        print(json.dumps(swagger))
    except Exception as e:
        import traceback, sys
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()