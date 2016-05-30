

import click

from .utils import value_color_picker, cli_format_transaction_line, cli_format_transaction_group, cli_echo
from .main import fetch_total_balance, fetch_running_tally, fetch_transactions_categorized


@click.group()
@click.option('--page', is_flag=True, help='Page the output.')
@click.pass_context
def cli(ctx, page):
    ctx.obj = {
        'page': page,
    }


@cli.command()
@click.pass_context
def balance(ctx):
    """Prints out current balance."""
    total = fetch_total_balance()
    color = value_color_picker(total)
    output = click.style(str(total), fg=color)

    cli_echo(ctx, output)


@cli.command()
@click.pass_context
def running_tally(ctx):
    """Prints out a running tally."""
    rt = fetch_running_tally()
    output = '\n'.join([cli_format_transaction_line(day['Date'], day['running_tally']) for day in rt])

    cli_echo(ctx, output)


@cli.command()
@click.pass_context
def transactions(ctx):
    """Prints out transactions."""
    categorized = fetch_transactions_categorized()
    formatted_trans = [cli_format_transaction_group(k, v['sum'], v['transactions']) for k, v in categorized.items()]

    cli_echo(ctx, ''.join(formatted_trans))
