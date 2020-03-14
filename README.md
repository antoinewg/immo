# immo

[![Build Status](https://travis-ci.com/antoinewg/immo.svg?branch=master)](https://travis-ci.com/antoinewg/immo)
[![codecov](https://codecov.io/gh/antoinewg/immo/branch/master/graph/badge.svg)](https://codecov.io/gh/antoinewg/immo)

### Installation

**Steps**:

-   Create virtual environment: `python3 -m venv venv`
-   Activate it: `source ./venv/bin/activate`
-   Install dependencies: `pip install -r requirements.txt`

You're ready to go 🚀!

To update dependencies:

-   Install dependency: `pip install <library>`
-   Freeze requirements: `pip freeze > requirements.txt`
-   Commit "requirements.txt"

### Tests

Launch the test using: `python -m pytest`

_Options_:

-   `<path_to_file>::<test_name>`: only run a specific test,
-   `s`: debugger enabled: you can use `ipdb` 👍.
