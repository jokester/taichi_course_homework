#!/usr/bin/env bash

cd $(dirname "$0")
set -uex

if [[ ! -e venv ]]; then
  python3 -m venv venv
  exec venv/bin/pip3 install -r requirements.txt
else
  echo "'venv' directory already exists. remove it and run $0 again would install all packages again"
fi
