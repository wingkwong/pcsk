"""
Invokable Module for CLI

python -m pcskcli
"""

from pcskcli.cli.main import cli


if __name__ == "__main__":
    cli(prog_name="pcsk")