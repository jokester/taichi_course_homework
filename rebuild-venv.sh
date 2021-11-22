#!/usr/bin/env bash

cd $(dirname "$0")
set -uex

if [[ ! -e venv ]]; then
  python3 -m venv venv
  venv/bin/pip3 install wheel pipdeptree autopep8 # dev deps
  venv/bin/pip3 install "taichi<0.9"
  venv/bin/pip3 freeze > requirements.txt
else
  echo "'venv' directory already exists. remove it and run $0 again to rebuild all deps"
fi
