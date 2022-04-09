#!/bin/sh

SRC_DIR=src

source .venv/bin/activate
pip install -q -r requirements-lint.txt
mypy "$SRC_DIR"
