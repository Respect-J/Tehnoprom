#!/bin/bash

# Crash on errors.
set -e

DIR_VENV=$(dirname "$0")/venv
if [ -d "$DIR_VENV" ]; then
    echo "deleting existing venv ..."
    rm -fr $DIR_VENV
else
    echo "venv does not exist"
fi

echo "creating new venv ..."
python3.11 -mvenv venv

echo "activating venv ..."
source ${DIR_VENV}/bin/activate

echo "installing packages ..."
venv/bin/pip3 install pip==22.0.4
venv/bin/pip3 install wheel
if [[ $OSTYPE == 'darwin'* ]]; then
    if ! [ -x "$(command -v brew)" ]; then
        echo "You need to install brew first: https://brew.sh"
        exit
    fi
    if ! [ -x "$(command -v openssl)" ]; then
        brew install openssl
    fi
    if ! [ -x "$(command -v poetry | grep -q "1.2.1")" ]; then
        export POETRY_VERSION="1.2.1"
        curl -sSL https://install.python-poetry.org | python3 -
    fi
    export LDFLAGS="-L/usr/local/opt/openssl/lib"
    export CPPFLAGS="-I/usr/local/opt/openssl/include"
    export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"
fi

# update paths so e.g. pytest is the venv version
hash -r

poetry config virtualenvs.path venv --local
poetry config virtualenvs.create false --local
poetry install --no-root -v

# Install types for mypy. We have to pin them due to an issue with types-requests==3.31.0.7 forcing us to pull in urllib3==2.
venv/bin/python3.11 -m pip install "types-requests<2.31.0.7" types-python-dateutil types-pytz types-redis types-retry types-simplejson
# Don't use mypy --install-types anymore because it
# venv/bin/python3.11 -m mypy --install-types --non-interactive

# Install pre commit hooks
echo "installing pre commit hook"
pre-commit install