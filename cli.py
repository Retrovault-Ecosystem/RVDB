#!/usr/bin/env python3

import argparse

from commands.registry import COMMANDS, get_command


def main():

    parser = argparse.ArgumentParser(
        prog="rvdb",
        description="RetroVault Database"
    )


    sub = parser.add_subparsers(
        dest="command",
        metavar="COMMAND"
    )


    # =====================================================
    # BUILD COMMANDS FROM REGISTRY
    # =====================================================

    for command in COMMANDS:

        name = command["name"]

        aliases = command["aliases"]

        parser_cmd = sub.add_parser(
            name,
            aliases=aliases,
            help=command["help"]
        )


        for argument in command["arguments"]:

            parser_cmd.add_argument(
                argument
            )


    # =====================================================
    # PARSE ARGUMENTS
    # =====================================================

    args = parser.parse_args()


    if not args.command:

        parser.print_help()
        return


    # =====================================================
    # FIND HANDLER
    # =====================================================

    command = get_command(
        args.command
    )


    if not command:

        print(
            f"Unknown command: {args.command}"
        )

        return


    handler = command["handler"]


    # =====================================================
    # PASS ONLY USER ARGUMENTS
    # =====================================================

    values = vars(args)

    arguments = []

    for name in command["arguments"]:

        arguments.append(
            values[name]
        )


    handler(
        *arguments
    )


if __name__ == "__main__":

    main()
