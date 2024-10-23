'''
Implement the command-line interface
Steps:
    1. Initialize table by decorating under click.group()
    2. Wrap database command in a user-friendly way by click.command()
'''

import click
from dbtool.database import (
    create_table,
    add_record,
    view_records,
    update_record,
    delete_record,
)

@click.group()
def cli():
    """A simple command-line tool to interact with a database -- initialize."""
    create_table()

@cli.command()
@click.option('--name', prompt='Name', help='The name of the record.')
@click.option('--value', prompt='Value', help='The value of the record.')
def add(name, value):
    """Add a new record to the database."""
    add_record(name, value)
    click.echo('Record added successfully.')

@cli.command()
def view():
    """View all records in the database."""
    records = view_records()
    if records:
        for record in records:
            click.echo(f'ID: {record[0]}, Name: {record[1]}, Value: {record[2]}')
    else:
        click.echo('No records found.')

@cli.command()
@click.option('--id', prompt='Record ID', help='The ID of the record to update.', type=int)
@click.option('--name', prompt='New Name', help='The new name of the record.')
@click.option('--value', prompt='New Value', help='The new value of the record.')
def update(id, name, value):
    """Update an existing record."""
    update_record(id, name, value)
    click.echo('Record updated successfully.')

@cli.command()
@click.option('--id', prompt='Record ID', help='The ID of the record to delete.', type=int)
def delete(id):
    """Delete a record from the database."""
    delete_record(id)
    click.echo('Record deleted successfully.')

if __name__ == '__main__':
    cli()
