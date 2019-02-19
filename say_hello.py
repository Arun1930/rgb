#!/usr/bin/env python3.5
import sys

from termcolor import cprint
from pyfiglet import figlet_format


def main():
    cprint(
        figlet_format('Hello!', font='starwars'),
        'yellow',
        'on_red',
        attrs=['bold'])


if __name__ == "__main__":
    main()
