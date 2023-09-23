import argparse
import logging
import blight.server.cli
import blight.client.cli


def configure_logging(args):
    level = getattr(logging, args.log_level.upper())
    fh = logging.FileHandler("server.log", mode="w")
    sh = logging.StreamHandler()

    logging.basicConfig(level=level, handlers=[fh, sh])


def main():
    parser = argparse.ArgumentParser()
    parser.set_defaults(command="client")

    subparsers = parser.add_subparsers(dest="command")
    blight.server.cli.attach_subparser(subparsers)
    blight.client.cli.attach_subparser(subparsers)

    args = parser.parse_args()
    configure_logging(args)

    if "func" in args:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
