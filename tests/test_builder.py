from rvdb.build.builder import RVDBBuilder


builder = RVDBBuilder()

builder.load()

output = builder.export_json()

print(
    f"Generated: {output}"
)
