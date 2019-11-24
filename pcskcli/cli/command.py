"""
Base classes that implement the CLI framework
"""

import logging
import importlib
from collections import OrderedDict

import click

logger = logging.getLogger(__name__)

_COMMAND_PACKAGE = [
    "pcskcli.commands.command1",
    "pcskcli.commands.command2",
]

class BaseCommand(click.MultiCommand):
    def __init__(self, *args, cmd_packages=None, **kwargs):
        """
        Initializes the class, optionally with a list of available commands
        :param cmd_packages: List of Python packages names of CLI commands
        :param args: Other Arguments passed to super class
        :param kwargs: Other Arguments passed to super class
        """
        super(BaseCommand, self).__init__(*args, **kwargs)

        if not cmd_packages:
            cmd_packages = _COMMAND_PACKAGE

        self._commands = {}
        self._commands = BaseCommand._set_commands(cmd_packages)

    @staticmethod
    def _set_commands(package_names):
        """
        Extract the command name from package name. Last part of the module path is the command
        ie. if path is foo.bar.baz, then "baz" is the command name.
        :param package_names: List of package names
        :return: Dictionary with command name as key and the package name as value.
        """
        commands = OrderedDict()

        for pkg_name in package_names:
            cmd_name = pkg_name.split(".")[-1]
            commands[cmd_name] = pkg_name

        return commands

    def list_commands(self, ctx):
        """
        Overrides a method from Click that returns a list of commands available in the CLI.
        :param ctx: Click context
        :return: List of commands available in the CLI
        """
        return list(self._commands.keys())

    def get_command(self, ctx, cmd_name):
        """
        Overrides method from ``click.MultiCommand`` that returns Click CLI object for given command name, if found.
        :param ctx: Click context
        :param cmd_name: Top-level command name
        :return: Click object representing the command
        """
        if cmd_name not in self._commands:
            logger.error("Command %s not available", cmd_name)
            return None

        pkg_name = self._commands[cmd_name]

        try:
            mod = importlib.import_module(pkg_name)
        except ImportError:
            logger.exception("Command '%s' is not configured correctly. Unable to import '%s'", cmd_name, pkg_name)
            return None

        if not hasattr(mod, "cli"):
            logger.error("Command %s is not configured correctly. It must expose an function called 'cli'", cmd_name)
            return None

        return mod.cli