from rvdb.build.builder import RVDBBuilder


def main():

    builder = RVDBBuilder()

    output = builder.build()

    print(
        f"Generated: {output}"
    )


if __name__ == "__main__":
    main()
