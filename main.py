#!python
import torch
import logging
import pickle
from sys import argv
from src.config import defaults, makeconfig, print_help


def train():
    ...


def test():
    ...


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Rudimentary argument parser for command line arguments.
    # Lets us have otherwise complicated behaviour, like chaining commands.
    actions = list()
    params = list()
    for arg in argv[1:]:
        if arg == "help":
            print_help()
        elif arg.startswith("--"):
            params.append(arg[2:])
        else:
            actions.append(arg)

    # Build default config params
    makeconfig(params)

    model = None
    ns = None
    for command in actions:
        if command == "train":
            train()
        
        elif command == "test":
            test()
        
        else:
            print(f"Unknown command `{command}`")
            print_help()
    exit(0)