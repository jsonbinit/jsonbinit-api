# JSON {🗑} IT API

[![codecov](https://codecov.io/gh/jsonbinit/jsonbinit-api/branch/master/graph/badge.svg)](https://codecov.io/gh/jsonbinit/jsonbinit-api)
[![Build Status](https://travis-ci.org/jsonbinit/jsonbinit-api.svg?branch=master)](https://travis-ci.org/jsonbinit/jsonbinit-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/jsonbinit/jsonbinit-api/blob/master/LICENSE)

## Run locally for development

```sh
pip install -r requirements.txt
cd app
python main.py
```

## Run with Docker Compose

```sh
docker-compose up
```

## Run tests

```sh
pip install -r requirements-dev.txt
pytest app/test.py --cov main -s --cov-report term-missing
```
