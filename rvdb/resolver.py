def resolve_id(
    category,
    value
):

    if value is None:
        return None


    if "." in value:
        return value


    return f"{category}.{value}"
