PopIt Django App
================

|Build Status|

A Django app that makes it easy to locally store and use data from one
or more PopIt API instances.

What is PopIt and PopIt-API?
----------------------------

PopIt is a project from `mySociety <http://www.mysociety.org/>`__ that
aims to make it really simple to store and share data on people such as
politicians, organisations such as parliaments and political parties,
and the posts and memberships that link the people to the organisations.

The PopIt-API is a self standing server that provides a HTTP REST API to
read and write this data. It is a `separate
codebase <https://github.com/mysociety/popit-api>`__ to this one.

This Django app lets you fetch data from several PopIt-APIs and store it
locally in your Django project so that you can use all the power of the
Django ORM to query the data. There are also management commands that
make it easy to fetch the latest updates from the PopIt-API.

It will also let you store your own data in the same models so that you
can add to the data from the PopIt-APIs. In time it should be possible
to push this local data out to a PopIt-API so that it is easy for others
to reuse.

WARNING - Alpha code
--------------------

This is alpha code and subject to frequent and backwards incompatible
change. Feel free to experiment but do not use in production until this
message is removed.

This code is a work in progress - it is probably not useful to you yet.
Please see the ``IDEAS.md`` file for possible future additions and the
`current
issues <https://github.com/mysociety/popit-django/issues?state=open>`__
for more immediately planned work.

Installing and configuring
--------------------------

Please install ``popit-django`` from PyPI. You should also add it to
your project's ``requirements.txt``.

.. code:: bash

    pip install popit-django --use-mirrors

In your ``settings.py`` add ``south`` and ``popit`` to your
``INSTALLED_APPS`` (``popit`` uses South to manage database migrations
so make sure it comes first).

.. code:: python

    INSTALLED_APPS = [
        # ...
        'south',
        'popit',
        # ....
    ]

Setup the database:

.. code:: bash

    python manage.py syncdb
    python manage.py migrate

Now create a ``popit.models.ApiInstance`` entry and fetch all the
documents from that API instance:

.. code:: bash

    python manage.py popit_retrieve_all

Database notes
--------------

For some of the referential integrity we use a ``UNIQUE INDEX`` to
prevent duplicates on values that are ``NOT NULL``. This is known to
work with Postgres and SQLite, but other databases may have issues. See
the ``PopItURLField`` class in ``popit/fields.py`` for more details.

Development
-----------

If you want to contribute to the development of ``popit-django`` that
would be great, we aim to be responsive to pull requests. These
instructions should get you a dev environment set up.

To run the tests you'll need a local PopIt-API instance that can be
deleted. This will be installed for you by the
``start_local_popit_api.bash`` script, but it requires the following:

-  `MongoDB <http://www.mongodb.org/>`__ for the PopIt-API instance.
   Should
    allow anonymous access and db creation (the default).
-  `Node.js <http://nodejs.org/>`__ installed.

.. code:: bash

    # get the code (you might want to clone your fork instead)
    git clone https://github.com/mysociety/popit-django.git
    cd popit-django

    # Set up virtual environment
    virtualenv --no-site-packages .venv
    . .venv/bin/activate

    # Install the python dependencies
    pip install -r requirements.txt --use-mirrors

    # Install (if needed) and start the popit-api server
    ./start_local_popit_api.bash

    # Run the tests
    ./manage.py test popit

.. |Build Status| image:: https://travis-ci.org/mysociety/popit-django.png?branch=master
   :target: https://travis-ci.org/mysociety/popit-django
