#!/bin/sh

TEST_DIR=tests

. ./scripts/venv.sh
pip install -q -r requirements-test.txt || exit 1

pytest "$TEST_DIR" "$@"
