#!/bin/sh

DIRS='src test'

. ./scripts/venv.sh

pip install -q -r requirements-lint.txt || exit 1

for dir in $DIRS; do
  black "$dir"
done
