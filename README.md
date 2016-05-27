# benchresttest
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
defaultdict(<function fetch_transactions_categorized.<locals>.<lambda> at 0x007146A8>, {'': {'transactions': [{'Amount': 5000.0, 'Date': '2013-12-13', 'Ledger': '', 'Company': 'Payment - Thank You / Paiement - Merci'}, {'Amount
': 10000.0, 'Date': '2013-12-17', 'Ledger': '', 'Company': 'Payment - Thank You / Paiement - Merci'}, {'Amount': 907.85, 'Date': '2013-12-17', 'Ledger': '', 'Company': 'Payment Received - Thank You'}, {'Amount': 20000.0, 'Date'
: '2013-12-19', 'Ledger': '', 'Company': 'Payment - Thank You / Paiement - Merci'}], 'sum': 35907.85}, 'Postage & Shipping Expense': {'transactions': [{'Amount': -30.69, 'Date': '2013-12-12', 'Ledger': 'Postage & Shipping Expen
se', 'Company': 'Dhl Yvr Gw Richmond Bc'}], 'sum': -30.69}, 'Auto Expense': {'transactions': [{'Amount': -72.75, 'Date': '2013-12-13', 'Ledger': 'Auto Expense', 'Company': 'Smart City Foods'}, {'Amount': 6.23, 'Date': '2013-12-
17', 'Ledger': 'Auto Expense', 'Company': 'Smart City Foods'}], 'sum': -66.52}, 'Web Hosting & Services Expense': {'transactions': [{'Amount': -63.01, 'Date': '2013-12-12', 'Ledger': 'Web Hosting & Services Expense', 'Company':
 'Growingcity.Com'}, {'Amount': -50.95, 'Date': '2013-12-18', 'Ledger': 'Web Hosting & Services Expense', 'Company': 'Linkedin Linkedin.Com'}, {'Amount': -10.99, 'Date': '2013-12-19', 'Ledger': 'Web Hosting & Services Expense',
 'Company': 'Dropbox'}], 'sum': -124.95}, 'Phone & Internet Expense': {'transactions': [{'Amount': -110.71, 'Date': '2013-12-22', 'Ledger': 'Phone & Internet Expense', 'Company': 'Shaw Cablesystems Calgary Ab'}], 'sum': -110.71
}, 'Insurance Expense': {'transactions': [{'Amount': -117.81, 'Date': '2013-12-13', 'Ledger': 'Insurance Expense', 'Company': 'London Drugs 78 Postal Vancouver Bc'}, {'Amount': -4.87, 'Date': '2013-12-17', 'Ledger': 'Insurance
Expense', 'Company': 'London Drugs 78 Postal Vancouver Bc'}, {'Amount': -22.94, 'Date': '2013-12-18', 'Ledger': 'Insurance Expense', 'Company': 'London Drugs Vancouver Bc'}], 'sum': -145.62}, 'Travel Expense, Nonlocal': {'trans
actions': [{'Amount': -9.55, 'Date': '2013-12-18', 'Ledger': 'Travel Expense, Nonlocal', 'Company': 'Vancouver Taxi Vancouver Bc'}, {'Amount': -21.8, 'Date': '2013-12-18', 'Ledger': 'Travel Expense, Nonlocal', 'Company': 'Yello
w Cab Co Ltd Vancouver Bc'}, {'Amount': -200.0, 'Date': '2013-12-19', 'Ledger': 'Travel Expense, Nonlocal', 'Company': 'Yellow Cab Company Ltd Vancouver'}, {'Amount': -7.6, 'Date': '2013-12-20', 'Ledger': 'Travel Expense, Nonlo
cal', 'Company': 'Vancouver Taxi Vancouver Bc'}, {'Amount': -8.1, 'Date': '2013-12-21', 'Ledger': 'Travel Expense, Nonlocal', 'Company': 'Black Top Cabs Vancouver Bc'}], 'sum': -247.04999999999998}, 'Education': {'transactions'
: [{'Amount': -4463.2, 'Date': '2013-12-16', 'Ledger': 'Education', 'Company': 'Clown College I Vancouver Bc'}], 'sum': -4463.2}, 'Equipment Expense': {'transactions': [{'Amount': -520.85, 'Date': '2013-12-13', 'Ledger': 'Equip
ment Expense', 'Company': 'Echosign'}, {'Amount': -5518.17, 'Date': '2013-12-13', 'Ledger': 'Equipment Expense', 'Company': 'Apple Store Vancouver Bc'}, {'Amount': -1874.75, 'Date': '2013-12-20', 'Ledger': 'Equipment Expense',
'Company': 'Ninja Star World Vancouver Bc'}, {'Amount': -1874.75, 'Date': '2013-12-20', 'Ledger': 'Equipment Expense', 'Company': 'Ninja Star World Vancouver Bc'}], 'sum': -9788.52}, 'Office Expense': {'transactions': [{'Amount
': -42.53, 'Date': '2013-12-12', 'Ledger': 'Office Expense', 'Company': 'Fedex'}, {'Amount': -16.35, 'Date': '2013-12-17', 'Ledger': 'Office Expense', 'Company': 'Dynamex Express'}, {'Amount': -642.79, 'Date': '2013-12-18', 'Le
dger': 'Office Expense', 'Company': 'Costco Wholesale Co Vancouver'}], 'sum': -701.67}, 'Business Meals & Entertainment Expense': {'transactions': [{'Amount': -91.12, 'Date': '2013-12-12', 'Ledger': 'Business Meals & Entertainm
ent Expense', 'Company': 'Nesters Market Vancouver Bc'}, {'Amount': -5.39, 'Date': '2013-12-15', 'Ledger': 'Business Meals & Entertainment Expense', 'Company': 'Urban Fare Vancouver Bc'}, {'Amount': -112.33, 'Date': '2013-12-16
', 'Ledger': 'Business Meals & Entertainment Expense', 'Company': 'Bows And Arrows Coffee Rovictoria Bc'}, {'Amount': -206.58, 'Date': '2013-12-17', 'Ledger': 'Business Meals & Entertainment Expense', 'Company': 'Justin Stitche
s Inc Vancouver Bc'}, {'Amount': -8.94, 'Date': '2013-12-18', 'Ledger': 'Business Meals & Entertainment Expense', 'Company': 'Nesters Market Vancouver Bc'}, {'Amount': -1084.32, 'Date': '2013-12-18', 'Ledger': 'Business Meals &
 Entertainment Expense', 'Company': 'Bc Liquor Vancouver Bc'}, {'Amount': -35.7, 'Date': '2013-12-19', 'Ledger': 'Business Meals & Entertainment Expense', 'Company': 'Nesters Market Vancouver Bc'}, {'Amount': -297.5, 'Date': '2
013-12-20', 'Ledger': 'Business Meals & Entertainment Expense', 'Company': 'Commodore Lanes & Bill Vancouver Bc'}, {'Amount': -9.88, 'Date': '2013-12-21', 'Ledger': 'Business Meals & Entertainment Expense', 'Company': 'Guilt &
Co. Vancouver Bc'}], 'sum': -1851.76}})
```

### Fetch running tally
```python
>>> from benchresttest import fetch_running_tally
>>> fetch_running_tally()
[{'Date': '2013-12-12', 'running_tally': -227.35, 'date_sum': -227.35}, {'Date': '2013-12-13', 'running_tally': -1456.93, 'date_sum': -1229.58}, {'Date': '2013-12-15', 'running_tally': -1462.32, 'date_sum': -5.39}, {'Date': '20
13-12-16', 'running_tally': -6037.85, 'date_sum': -4575.53}, {'Date': '2013-12-17', 'running_tally': 4648.43, 'date_sum': 10686.28}, {'Date': '2013-12-18', 'running_tally': 2807.14, 'date_sum': -1841.29}, {'Date': '2013-12-19',
 'running_tally': 22560.45, 'date_sum': 19753.31}, {'Date': '2013-12-20', 'running_tally': 18505.85, 'date_sum': -4054.6}, {'Date': '2013-12-21', 'running_tally': 18487.87, 'date_sum': -17.98}, {'Date': '2013-12-22', 'running_t
ally': 18377.16, 'date_sum': -110.71}]
```

## Running tests
The best way to run tests is simple running `tox` if you have it
installed. That will run py.test and flake8. The other option is to run
`py.test --cov=benchresttest tests.py`.

Note sample_data.py is excluded from flake8.
