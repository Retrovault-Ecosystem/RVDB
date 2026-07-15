from .version import cmd_version
from .validate import cmd_validate
from .build import cmd_build
from .query import cmd_query
from .search import cmd_find
from .list import cmd_list
from .show import cmd_show
from .info import cmd_info
from .create import cmd_create
from .relationships import (
    cmd_cores,
    cmd_who_uses,
    cmd_related,
)

from .reverse import (
    cmd_developed_by,
    cmd_published_by,
    cmd_games_on,
)


# =========================================================
# COMMAND REGISTRY
# =========================================================

COMMANDS = [

    {
        "name": "version",
        "handler": cmd_version,
        "aliases": ["ver"],
        "help": "Show version",
        "arguments": []
    },


    {
        "name": "validate",
        "handler": cmd_validate,
        "aliases": ["v"],
        "help": "Validate database",
        "arguments": []
    },


    {
        "name": "build",
        "handler": cmd_build,
        "aliases": [],
        "help": "Build database",
        "arguments": []
    },


    {
        "name": "query",
        "handler": cmd_query,
        "aliases": ["q"],
        "help": "Query entity",
        "arguments": [
            "entity"
        ]
    },


    {
        "name": "list",
        "handler": cmd_list,
        "aliases": [],
        "help": "List objects",
        "arguments": [
            "type"
        ]
    },


    {
        "name": "show",
        "handler": cmd_show,
        "aliases": [],
        "help": "Show full entity details",
        "arguments": [
            "entity"
        ]
    },


    {
        "name": "info",
        "handler": cmd_info,
        "aliases": ["i"],
        "help": "Show detailed entity information",
        "arguments": [
            "entity"
        ]
    },


    {
        "name": "cores",
        "handler": cmd_cores,
        "aliases": [],
        "help": "Show cores for platform",
        "arguments": [
            "platform"
        ]
    },


    {
        "name": "who-uses",
        "handler": cmd_who_uses,
        "aliases": [],
        "help": "Show platforms using a core",
        "arguments": [
            "core"
        ]
    },


    {
        "name": "related",
        "handler": cmd_related,
        "aliases": ["rel"],
        "help": "Show related entities",
        "arguments": [
            "entity"
        ]
    },


    {
        "name": "find",
        "handler": cmd_find,
        "aliases": [
            "search",
            "s"
        ],
        "help": "Fuzzy search entities",
        "arguments": [
            "term"
        ]
    },


    {
        "name": "developed-by",
        "handler": cmd_developed_by,
        "aliases": [],
        "help": "Show games by developer",
        "arguments": [
            "developer"
        ]
    },


    {
        "name": "published-by",
        "handler": cmd_published_by,
        "aliases": [],
        "help": "Show games by publisher",
        "arguments": [
            "publisher"
        ]
    },


    {
        "name": "games-on",
        "handler": cmd_games_on,
        "aliases": [],
        "help": "Show games on platform",
        "arguments": [
            "platform"
        ]
    },

    {
        "name": "create",
        "handler": cmd_create,
        "aliases": [],
        "help": "Create entity from template",
        "arguments": [
            "type",
            "id",
            "name"
        ]
    },

]


# =========================================================
# LOOKUP FUNCTIONS
# =========================================================

def get_command(name):

    for command in COMMANDS:

        if command["name"] == name:
            return command

        if name in command["aliases"]:
            return command

    return None



def list_commands():

    return sorted(
        command["name"]
        for command in COMMANDS
    )
