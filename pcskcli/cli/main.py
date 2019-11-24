"""
Entry point for the CLI
"""

import logging
import json
import click

from pcskcli import __version__
from pcskcli.lib.utils.logging import CliLogger
from .command import BaseCommand


LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


@click.command(cls=BaseCommand)
@click.version_option(version=__version__)
def cli():
    logger = logging.getLogger("pcskcli")
    formatter = logging.Formatter("%(message)s")

    CliLogger.configure_logger(logger, formatter, logging.INFO)