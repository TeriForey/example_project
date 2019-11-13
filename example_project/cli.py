# -*- coding: utf-8 -*-

"""Console script for example_project."""
import argparse
import sys


def main():
    """Console script for example_project."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "example_project.cli.main")
    print("How could I ever be rude to you?")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
