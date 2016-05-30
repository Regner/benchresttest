# benchresttest
[![Build Status](https://travis-ci.org/Regner/benchresttest.svg?branch=master)](https://travis-ci.org/Regner/benchresttest)
[![Coverage Status](https://coveralls.io/repos/github/Regner/benchresttest/badge.svg?branch=master)](https://coveralls.io/github/Regner/benchresttest?branch=master)

Test for Bench.co.

## Install
The package has not been made available on PyPi because... well not
really any reason to do that. There is however a setup.py so you can
still pip install it. Assuming you have python 3.5, pip, and virtaulenv:

### Windows
```
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install --editable .
```

### Linux/Mac
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install --editable .
```

## Example Usage From CLI
```
$ benchresttest --help
Usage: benchresttest-script.py [OPTIONS] COMMAND [ARGS]...

Options:
  --page  Page the output.
  --help  Show this message and exit.

Commands:
  balance        Prints out current balance.
  running_tally  Prints out a running tally.
  transactions   Prints out transactions.

$ benchresttest balance
18377.16

$ benchresttest running_tally
2013-12-12 -227.35
2013-12-13 -1456.93
2013-12-15 -1462.32
2013-12-16 -6037.85
2013-12-17 4648.43
2013-12-18 2807.14
2013-12-19 22560.45
2013-12-20 18505.85
2013-12-21 18487.87
2013-12-22 18377.16

$ benchresttest --page transactions

============================================================
Category:
Total: 35907.85

Transactions:
2013-12-13 Payment - Thank You / Paiement - Merci 5000.0
2013-12-17 Payment - Thank You / Paiement - Merci 10000.0
2013-12-17 Payment Received - Thank You 907.85
2013-12-19 Payment - Thank You / Paiement - Merci 20000.0
============================================================

============================================================
Category: Phone & Internet Expense
Total: -110.71
-- More  --
```

Passing the `--page` argument will cause the results being output to the
console to be paginated.

## Example Usage From Python
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
