

import re
import click
import requests

from itertools import groupby

BASE_TRANSACTIONS_URL = 'http://resttest.bench.co/transactions/{}.json'


def crawl_transaction_api(page: int = 1, current_count: int = 0) -> list:
    """Crawls the transactions API and returns the processed response.

    Note: API does not have links to the next page or a guarantee of quantity
          per page so we attempt to figure out page numbers automatically.
    """
    transactions_url = BASE_TRANSACTIONS_URL.format(page)
    response = requests.get(transactions_url)
    response.raise_for_status()

    results = response.json()
    transactions = results['transactions']

    current_count += len(transactions)

    if current_count < results['totalCount']:
        transactions += crawl_transaction_api(page + 1, current_count)

    return transactions


def process_transaction_results(transactions: list) -> list:
    """Runs the different processors for the transaction API results."""
    transactions = convert_transaction_amounts_to_float(transactions)
    transactions = dedupe_transactions(transactions)
    transactions = prettify_company_names(transactions)
    transactions = sort_transactions(transactions)

    return transactions


def convert_transaction_amounts_to_float(transactions: list) -> list:
    """Converts the Amount string in transactions to a float."""
    for t in transactions:
        t['Amount'] = float(t['Amount'])

    return transactions


def dedupe_transactions(transactions: list) -> list:
    """Merges duplicate transactions."""
    deduped_transactions = []

    for key, group in groupby(transactions, lambda x: "{}{}{}".format(x['Date'], x['Ledger'], x['Company'])):
        group = list(group)

        if len(group) == 1:
            deduped_transactions.append(group[0])

        else:
            combined_transaction = {
                'Date': group[0]['Date'],
                'Ledger': group[0]['Ledger'],
                'Company': group[0]['Company'],
                'Amount': 0,
            }

            for thing in group:
                combined_transaction['Amount'] += thing['Amount']

            deduped_transactions.append(combined_transaction)

    return deduped_transactions


def prettify_company_names(transactions: list) -> list:
    """Attempts to clean up company names and make them prettier."""
    for t in transactions:
        t['Company'] = remove_card_numbers(t['Company'])
        t['Company'] = remove_receipt_number(t['Company'])
        t['Company'] = t['Company'].title()

    return transactions


def remove_receipt_number(some_string: str) -> str:
    """Removes a receipt number from a given string.

    Note: Admittedly working with a small sample size to create this regex so
          this needs more work with a larger sample.
    """
    matches = re.match('(.*) (#\S*) (.*)', some_string)

    if matches is not None:
        some_string = '{} {}'.format(matches.group(1), matches.group(3))

    return some_string


def remove_card_numbers(some_string: str) -> str:
    """Removes card numbers from a given string.

    Note: As with remove_receipt_number working with a small sample size when
          creating this. Should be tested on larger sample before release.
    """
    matches = re.match('(.*) (x{3,9})', some_string)

    if matches is not None:
        some_string = matches.group(1)

    return some_string


def sort_transactions(transactions: list) -> list:
    """Sorts a list of transactions by their Date value."""
    return sorted(transactions, key=lambda k: k['Date'])


def group_transactions_by_day(transactions: dict) -> list:
    """Takes a list of transactions then groups and sums them per date."""
    grouped_transactions = []

    for key, group in groupby(transactions, lambda x: x['Date']):
        transaction_date = {
            'Date': key,
            'date_sum': 0.0,
        }

        for thing in group:
            transaction_date['date_sum'] += thing['Amount']

        transaction_date['date_sum'] = transaction_date['date_sum']
        grouped_transactions.append(transaction_date)

    return grouped_transactions


def calculate_running_tally(transactions: list) -> list:
    """Takes a sorted and grouped list of transactions and adds a running tally.

    Note: This does assume the transactions have the 'date_sum' key added by by
          the group_transactions_by_day function.
    """
    for idx, val in enumerate(transactions):
        val['running_tally'] = val['date_sum']

        if idx > 0:
            val['running_tally'] += transactions[idx - 1]['running_tally']

        val['date_sum'] = round(val['date_sum'], 2)
        val['running_tally'] = round(val['running_tally'], 2)

    return transactions


def value_color_picker(value: float) -> str:
    """Takes a given value and decides what color it should be for click."""
    if value < 0:
        color = 'red'
    else:
        color = 'green'

    return color


def cli_format_transaction_line(day: str, value: float, company: str = None) -> str:
    """Formats an individual transaction line to be output to the console by click."""
    date = click.style(day, fg='blue')
    color = value_color_picker(value)
    tally = click.style(str(value), fg=color)

    if company is not None:
        response = '{} {} {}'.format(date, company, tally)

    else:
        response = '{} {}'.format(date, tally)

    return response


def cli_format_transaction_group(category: str, total: float, trans: list):
    """Formats a grouping of transactions to be output to the console by click."""
    response = '============================================================\n'
    response += 'Category: {}\n'.format(click.style(category, fg='cyan'))
    response += 'Total: {}\n'.format(click.style(str(round(total, 2)), fg=value_color_picker(total)))
    response += '\n'
    response += 'Transactions:\n'
    response += '\n'.join([cli_format_transaction_line(x['Date'], x['Amount'], x['Company']) for x in trans])
    response += '\n============================================================\n'

    return response


def cli_echo(ctx: click.core.Context, output: str):
    """Prints the output to console for click based on parameters in the context object."""
    if ctx.obj['page']:
        click.echo_via_pager(output)

    else:
        click.echo(output)
