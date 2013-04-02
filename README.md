# PopIt Django App

[![Build Status](https://travis-ci.org/mysociety/popit-django.png?branch=master)](https://travis-ci.org/mysociety/popit-django)

A Django app that makes it easy to locally store and use data from one or more
PopIt API instances.

This code will be started on in earnest once this [Mzalendo
ticket](https://github.com/mysociety/mzalendo/issues/615) has been closed as for
us it is the pre-cursor to this work.

## WARNING - Alpha code

This code is a work in progress - it is probably not useful to you yet.

This is alpha code and subject to frequent and backwards incompatible change.
Feel free to experiment but do not use in production until this message is
removed.

## Development

``` bash
git clone https://github.com/mysociety/popit-django.git
cd popit-django

virtualenv --no-site-packages .venv
. .venv/bin/activate

pip install -r requirements.txt --use-mirrors

./manage.py test popit
```

