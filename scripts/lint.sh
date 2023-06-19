#!/usr/bin/env bash

set -x

mypy app
black app
isort --profile black app
flake8 app
pylint app
