# Python3 Simple HTTP server
This project is an example how you can create a HTTP server in python3

# Manual test
For manual testing the preferred tool is 'curl', and the server has only one EP
to make calls, so the only command which can be useful with that is:

```
curl \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -X POST -d '{
  "sortKeys": ["fruits", "numbers"],
  "payload": {
    "fruits": ["watermelon", "apple", "pineapple"],
    "numbers": [1333, 4, 2431, 7],
    "colors": ["green", "blue", "yellow"]
  }
}' 127.0.0.1:8080/sort
```

# Run

## Build

Build can be made by 'pyinstaller'. Binary files will be in the dist directory

## Docker

To try out it in docker, run:

> docker run -d --rm --name python-http-server --network host -v "$PWD":/usr/src/app python:3 python /usr/src/app/server.py
