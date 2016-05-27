

import pytest
import responses
import sample_data

from benchresttest import total_balance, fetch_transactions, fetch_transactions_categorized, fetch_running_tally


@pytest.fixture()
def mock_responses():
    responses.add(
        responses.GET,
        'http://resttest.bench.co/transactions/1.json',
        body=sample_data.MOCK_TRANSACTION_BODY_1,
        status=200,
    )

    responses.add(
        responses.GET,
        'http://resttest.bench.co/transactions/2.json',
        body=sample_data.MOCK_TRANSACTION_BODY_2,
        status=200,
    )

    responses.add(
        responses.GET,
        'http://resttest.bench.co/transactions/3.json',
        body=sample_data.MOCK_TRANSACTION_BODY_3,
        status=200,
    )

    responses.add(
        responses.GET,
        'http://resttest.bench.co/transactions/4.json',
        body=sample_data.MOCK_TRANSACTION_BODY_4,
        status=200,
    )


@responses.activate
def test_total_balance(mock_responses):
    """Test that total_balance correctly sums the amounts.

    resttest objective: has a function that will calculate the total balance
    """
    assert total_balance() == 18377.16


@responses.activate
def test_fetch_transactions(mock_responses):
    """Tests fetch_transactions returns the correct data.

    resttest objective: As a user, I do not want to have any duplicated transactions in the list. Use the data provided
                        to detect and identify duplicate transactions.

                        As a user, I need vendor names to be easily readable. Make the vendor names more readable,
                        remove garbage from names.
    """
    assert fetch_transactions() == sample_data.SAMPLE_TRANSACTIONS_LIST


@responses.activate
def test_fetch_transactions_by_category(mock_responses):
    """Test fetch_transactions_by_category returns the correct data.

    resttest objective: As a user, I need to get a list expense categories. For each category I need a list of
                        transactions, and the total expenses for that category.
    """
    assert fetch_transactions_categorized() == sample_data.SAMPLE_TRANSACTIONS_BY_CATEGORY


@responses.activate
def test_fetch_running_tally(mock_responses):
    """Rest fetch_running_tally returns the correct data.

    resttest objective: As a user, I need to calculate daily calculated balances. A running total for each day. For
                        example, if I have 3 transactions for the 5th 6th 7th, each for $5, then the daily balance on
                        the 6th would be $10.
    """
    assert fetch_running_tally() == sample_data.SAMPLE_RUNNING_TALLY
