"""
Class containing error conditions that are exposed to the user.
"""

import click


class ConfigException(click.ClickException):
    """
    Exception class when configuration file fails checks.
    """