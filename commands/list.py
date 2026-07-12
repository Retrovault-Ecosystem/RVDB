from engine.loader import load_entities


def cmd_list(kind):

    try:

        entities = load_entities()


        if kind == "platforms":

            items = sorted(
                e["id"]
                for e in entities
                if e.get("type") == "platform"
            )


        elif kind == "cores":

            items = sorted(
                e["id"]
                for e in entities
                if e.get("type") == "core"
            )


        elif kind == "manufacturers":

            items = sorted(
                e.get("manufacturer")
                for e in entities
                if e.get("manufacturer")
            )


        else:

            print(
                f"Unknown list type: {kind}"
            )

            return


        for item in items:
            print(item)


    except Exception as e:

        print(
            "List error:",
            e
        )
