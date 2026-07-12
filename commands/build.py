from engine.context import get_engine


def cmd_build():

    try:

        engine = get_engine()

        graph = engine.graph

        print(f"Graph Nodes : {len(graph.nodes)}")
        print(f"Graph Edges : {len(graph.edges)}")

        print("\nBuild complete.")

    except Exception as e:
        print("Build error:", e)
