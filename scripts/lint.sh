#!/bin/sh

SRC_DIR=src
TEST_DIR=test

DIRS='src test'

. ./scripts/venv.sh
pip install -q -r requirements-lint.txt || exit 1

for dir in $DIRS; do
  echo '-------------'
  echo "Linting $dir"
  echo '-------------'

  echo 'Running mypy...'
  mypy "$dir" || exit 1

  echo 'Running pylint...'
  pylint "$dir" || exit 1

  echo 'Running black...'
  black --check "$dir" || exit 1
done
