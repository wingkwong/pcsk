# PCSK - Python CLI Starter Kit

PCSK is a CLI starter kit written in Python. It is designed to help you kickstart your Python CLI project using [click](https://github.com/pallets/click/) and following AWS CLI structure. 

## Getting started

Using PCKS requires Python 3.6 or above. After you clone the project, you need to configure the following.

1. Use your favourite editor to edit ``setup.py``, change the info accordingly. 
2. Rename project name ``pcks`` to ``your_project_name`` and CLI name ``pckscli`` to ``your_cli_name`` 
3. Install the packages by running ``python setup.py install``
4. Run the CLI using ``your_cli_name``. There are built-in two commands ``your_cli_name command1`` and ``your_cli_name command2``

````
Usage: pcskcli [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  command1  This is a short help for command1
  command2  This is a short help for command2
````

### To start writing your commands

1. Go to ``<your_project_name>/commands`` and copy the existing example ``command1`` or ``command2``
2. In the new command folder, modify ``__init__.py`` and ``command.py``
3. Write your CLI logic in ``command.py`` 
- Update ``HELP_TEXT``
- Update ``SHORT_HELP``
- Update the command name in ``@click.command`` and options
- Add your CLI logic in ``do_cli``
4. Go to ``<your_project_name>/cli/command.py``, add the package you just created to ``_COMMAND_PACKAGE``
5. Test your commands


## License 
PCKS is licensed under the MIT license. Check the [LICENSE](https://github.com/wingkwong/pcsk/blob/master/LICENSE) file for details.