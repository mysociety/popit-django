# Notes

## Releasing to PyPI

More notes on publishing can be found at
http://guide.python-distribute.org/creation.html

  * uncomment the various Django versions in `.travis.yml`, commit and push to
    test that the code works with older Djangos. Comment out the lines again
    afterwards.

  * Convert the `README.md` to `README.rst` either by running the command below
    or in smallish chunks using the [online
    tool](http://johnmacfarlane.net/pandoc/try/).

``` bash
pandoc --from=markdown --to=rst --output=README.rst README.md
```

  * Update the version number in `setup.py` and add date to relevant line in
    `CHANGES.md`. Commit using a simple 'v1.2.3' message and then tag it the
    same. Ideally it is this commit that will be packaged and published.

  * Run test suite: `./runtests.py` or `./setup.py test`

  * Quick sanity check: `./setup.py check`

  * Check that nothing has changed: `git status`

  * Create the source distribution and run tests in it:

```bash
# create a source distribution
./setup.py sdist

# go to it and run the tests
cd dist
tar zxf popit-django-*.tgz
cd popit-django-*

# start api server and run tests
./start_local_popit_api.bash && ./setup.py test

```

  * Finally upload the new version using `./setup.py sdist upload`