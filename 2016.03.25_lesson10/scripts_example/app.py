# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.script import Manager, Command, Option

__author__ = 'sobolevn'


app = Flask(__name__)
manager = Manager(app)


@manager.command
def runserver(host='http://127.0.0.1', port=5000):
    app.run(host=host, port=port)


class InfoCommand(Command):
    """
    This command prints info about the server.
    """

    option_list = (
        Option('--verbose', '-v', dest='verbose'),
    )

    def run(self, verbose=False):
        print('This is a test server with scripts.')
        if verbose:
            print('Runs in verbose mode.')

manager.add_command('info', InfoCommand)

if __name__ == '__main__':
    manager.run()
