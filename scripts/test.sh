#!/bin/sh

TEST_DIR=test

. ./scripts/venv.sh
pip install -q -r requirements-test.txt || exit 1

pytest "$TEST_DIR" "$@" || exit 1
