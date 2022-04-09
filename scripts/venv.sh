#!/bin/sh

VENV_DIR=.venv

if [ ! -d "$VENV_DIR" ]; then
  echo 'venv does not exist; creating...'
  python3 -m venv "$VENV_DIR" || exit 1
fi

source "$VENV_DIR/bin/activate" || exit 1
pip install -q --upgrade pip
