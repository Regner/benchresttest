# benchresttest
[![Build Status](https://travis-ci.org/Regner/benchresttest.svg?branch=master)](https://travis-ci.org/Regner/benchresttest)
[![Coverage Status](https://coveralls.io/repos/github/Regner/benchresttest/badge.svg?branch=master)](https://coveralls.io/github/Regner/benchresttest?branch=master)

Test for Bench.co.

## Example Usage
### Getting the total balance
```python
>>> from benchresttest import total_balance
>>> total_balance()
18377.16
```

### Getting transactions grouped by category
```python
>>> from benchresttest import fetch_transactions_categorized
>>> fetch_transactions_categorized()
...
```

### Fetch running tally
```python
>>> from benchresttest import fetch_running_tally
>>> fetch_running_tally()
...
```

## Running tests
The best way to run tests is simple running `tox` if you have it
installed. That will run py.test and flake8. The other option is to run
`py.test --cov=benchresttest tests.py`.

Note sample_data.py is excluded from flake8.
