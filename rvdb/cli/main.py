import sys


from rvdb.cli.commands import (
    build_command,
    search_command,
    info_command,
    relationships_command,
)



def main():

    if len(sys.argv) < 2:

        print(
            "Usage: rvdb <command>"
        )

        return



    command = sys.argv[1]



    if command == "build":

        build_command()



    elif command == "search":

        if len(sys.argv) < 3:

            print(
                "Usage: rvdb search <title>"
            )

            return


        search_command(
            sys.argv[2]
        )



    elif command == "info":

        if len(sys.argv) < 3:

            print(
                "Usage: rvdb info <id>"
            )

            return


        info_command(
            sys.argv[2]
        )



    elif command == "relationships":

        if len(sys.argv) < 3:

            print(
                "Usage: rvdb relationships <id>"
            )

            return


        relationships_command(
            sys.argv[2]
        )



    else:

        print(
            f"Unknown command: {command}"
        )



if __name__ == "__main__":

    main()
