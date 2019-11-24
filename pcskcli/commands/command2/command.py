"""
CLI command for "command1" command
"""
import json
import logging

import click

LOG = logging.getLogger(__name__)

HELP_TEXT= """
Write something useful here

Examples
--------
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.
$ pcskcli command2

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.
$ pcskcli command2 --option1 --option2
"""

SHORT_HELP= "This is a short help for command2" 


@click.command(
    "command2",
    short_help=SHORT_HELP,
    help=HELP_TEXT,
)
@click.option(
    "--option1",
    "-o1",
    required=True,
    is_flag=True,
    is_eager=True,
    help="This option is required with an argument",
)
@click.option(
    "--option2",
    "-o2",
    required=False,
    is_flag=True,
    is_eager=True,
    help="This option is a flag and it is NOT requried",
)

def cli(option1, option2):
    """
    All logic must be implemented in the ``do_cli`` method. This helps with easy unit testing
    """
    do_cli(option1, option2)

def do_cli(option1, option2):
    """
    Implementation of the ``cli`` method, just separated out for unit testing purposes
    """
    
    print("command2: Add you logic here")