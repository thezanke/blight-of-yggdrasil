import argparse
import yggdrasil.server.cli
import yggdrasil.client.cli


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")
    yggdrasil.server.cli.attach_subparser(subparsers)
    yggdrasil.client.cli.attach_subparser(subparsers)

    parser.set_defaults(command="client")
    args = parser.parse_args()

    if "func" in args:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
