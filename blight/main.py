import argparse
import logging
import blight.server
import blight.client


def configure_logging(args):
    level = getattr(logging, args.log_level.upper())
    fh = logging.FileHandler("server.log", mode="w")
    sh = logging.StreamHandler()

    logging.basicConfig(level=level, handlers=[fh, sh])


def main():
    parser = argparse.ArgumentParser()
    parser.set_defaults(command="client")

    subparsers = parser.add_subparsers(dest="command")
    blight.server.attach_subparser(subparsers)
    blight.client.attach_subparser(subparsers)

    args = parser.parse_args()

    if "func" in args:
        configure_logging(args)
        args.func(args)
    else:
        parser.print_help()
