#!/usr/bin/env python3

import argparse

from commands.registry import get_command


def main():

    parser = argparse.ArgumentParser(
        prog="rvdb",
        description="RetroVault Database"
    )


    sub = parser.add_subparsers(
        dest="command",
        metavar="COMMAND"
    )


    # -------------------------
    # CORE COMMANDS
    # -------------------------

    sub.add_parser(
        "version",
        aliases=["ver"],
        help="Show version"
    )

    sub.add_parser(
        "validate",
        aliases=["v"],
        help="Validate database"
    )

    sub.add_parser(
        "build",
        help="Build database"
    )


    q = sub.add_parser(
        "query",
        aliases=["q"],
        help="Query entity"
    )

    q.add_argument(
        "entity"
    )


    l = sub.add_parser(
        "list",
        help="List objects"
    )

    l.add_argument(
        "type",
        choices=[
            "platforms",
            "cores",
            "manufacturers"
        ]
    )


    # -------------------------
    # SMART COMMANDS
    # -------------------------

    s = sub.add_parser(
        "show",
        help="Show full entity details"
    )

    s.add_argument(
        "entity"
    )


    i = sub.add_parser(
        "info",
        aliases=["i"],
        help="Show detailed entity information"
    )

    i.add_argument(
        "entity"
    )


    c = sub.add_parser(
        "cores",
        help="Show cores for platform"
    )

    c.add_argument(
        "platform"
    )


    w = sub.add_parser(
        "who-uses",
        help="Show platforms using a core"
    )

    w.add_argument(
        "core"
    )


    r = sub.add_parser(
        "related",
        aliases=["rel"],
        help="Show related entities"
    )

    r.add_argument(
        "entity"
    )


    f = sub.add_parser(
        "find",
        aliases=["search", "s"],
        help="Fuzzy search entities"
    )

    f.add_argument(
        "term"
    )


    # -------------------------
    # REVERSE GRAPH COMMANDS
    # -------------------------

    d = sub.add_parser(
        "developed-by",
        help="Show games by developer"
    )

    d.add_argument(
        "developer"
    )


    p = sub.add_parser(
        "published-by",
        help="Show games by publisher"
    )

    p.add_argument(
        "publisher"
    )


    g = sub.add_parser(
        "games-on",
        help="Show games on platform"
    )

    g.add_argument(
        "platform"
    )


    # -------------------------
    # PARSE COMMAND
    # -------------------------

    args = parser.parse_args()


    command = get_command(
        args.command
    )


    if command:

        arguments = vars(args)

        values = [
            value
            for key, value in arguments.items()
            if key != "command"
        ]

        command(
            *values
        )


    else:

        parser.print_help()



if __name__ == "__main__":
    main()
