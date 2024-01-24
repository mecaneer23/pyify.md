#!/usr/bin/env python3
"""
Represent a MarkDown file (.md) as Python objects.
"""

from argparse import ArgumentParser, Namespace
from pathlib import Path


def parse_args() -> Namespace:
    """Parse command line arguments for pyify"""
    parser = ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_file(filename: Path) -> list[str]:
    """Read a MarkDown file, returning a list of its lines"""
    with filename.open("r", encoding="utf-8") as file:
        return file.read().splitlines()


def print_lines(lines: list[str]) -> None:
    """For debugging: print list of lines"""
    for line in lines:
        print(line)


def main():
    """
    Entry point for pyify.md
    """

    filename = Path(parse_args().filename)

    lines = read_file(filename)

    print_lines(lines)


if __name__ == "__main__":
    main()
