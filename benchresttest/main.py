

from itertools import groupby
from collections import defaultdict
from .utils import (crawl_transaction_api, process_transaction_results, group_transactions_by_day,
                    calculate_running_tally)


def total_balance() -> float:
    """Returns the total balance from the transactions API."""
    transactions = fetch_transactions()

    total = sum([t['Amount'] for t in transactions])

    return total


def fetch_transactions() -> dict:
    """Returns a list of all processed transactions."""
    transactions = crawl_transaction_api()
    transactions = process_transaction_results(transactions)

    return transactions


def fetch_transactions_categorized() -> dict:
    """Returns all transactions grouped by ledger value and a sum of those transactions per ledger group."""
    transactions = fetch_transactions()
    sorted_transactions = defaultdict(lambda: {'transactions': [], 'sum': 0})

    for key, group in groupby(transactions, lambda x: x['Ledger']):
        for thing in group:
            sorted_transactions[key]['transactions'].append(thing)
            sorted_transactions[key]['sum'] += thing['Amount']

    return sorted_transactions


def fetch_running_tally() -> list:
    """Returns a list of dictionaries each containing a date, the sum for that day, and the running tally."""
    transactions = fetch_transactions()
    grouped_transactions = group_transactions_by_day(transactions)
    sorted_transactions = sorted(grouped_transactions, key=lambda k: k['Date'])
    tallied_transactions = calculate_running_tally(sorted_transactions)

    return tallied_transactions
