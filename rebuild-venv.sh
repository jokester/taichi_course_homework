#!/usr/bin/env bash

cd $(dirname "$0")
set -uex

__OUR_PYTHON=python3
#__OUR_PYTHON=/opt/miniconda/bin/python3.9

if [[ ! -e venv ]]; then
  command $__OUR_PYTHON -m venv venv
  venv/bin/pip3 install wheel pipdeptree autopep8 # dev deps
  venv/bin/pip3 install "taichi"
  venv/bin/pip3 freeze > requirements.txt
else
  echo "'venv' directory already exists. remove it and run $0 again to rebuild all deps"
fi
