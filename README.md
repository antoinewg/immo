# immo 🏠

[![Build Status](https://travis-ci.com/antoinewg/immo.svg?branch=master)](https://travis-ci.com/antoinewg/immo)
[![codecov](https://codecov.io/gh/antoinewg/immo/branch/master/graph/badge.svg)](https://codecov.io/gh/antoinewg/immo)

## Installation

**Steps**:

-   Create virtual environment: `python3 -m venv venv`
-   Activate it: `source ./venv/bin/activate`
-   Install dependencies: `make install`
-   Launch `python manage.py genfixtures` to generate data.

You're ready to go 🚀!

Run `make serve` and visit [localhost](http://127.0.0.1:8001) to start.

## Development

#### Dependencies

To update dependencies:

-   Install dependency: `pip install <library>`
-   Freeze requirements: `make freeze`
-   Commit "requirements.txt"

#### Tests

Launch the test using: `python -m pytest`

_Options_:

-   `<path_to_file>::<test_name>`: only run a specific test,
-   `s`: debugger enabled: you can use `ipdb` 👍.

## Next steps

-   [ ] Setup Django and postgresql
-   [ ] Configure a cron to refresh data every hour `0 * * * *`
-   [ ] Frontend to visualize data
-   [ ] Monitoring of cron + alert if nice appart available
-   [ ] Deploy back & front
-   [ ] Recommendation system using Bayesian optimisation.
