#!/bin/sh

SRC_DIR=src

. ./scripts/venv.sh
pip install -q -r requirements-lint.txt || exit 1

echo 'Running mypy...'
mypy "$SRC_DIR" || exit 1
