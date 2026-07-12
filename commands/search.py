from engine.context import get_engine


def cmd_find(term):

    try:

        engine = get_engine()

        results = engine.search(term)

        if not results:

            print(f"No results for '{term}'")
            return


        print("\nSEARCH RESULTS")
        print("--------------")


        for result in results:

            entity = result["entity"]
            score = result["score"]
            reasons = result["reasons"]


            print(
                f"\n{entity.get('id')}"
                f" | {entity.get('name','')}"
            )


            print(
                f"score: {score:.1f}"
            )


            for reason in reasons:

                print(
                    f"  + {reason}"
                )


    except Exception as e:

        print(
            "Search error:",
            e
        )
