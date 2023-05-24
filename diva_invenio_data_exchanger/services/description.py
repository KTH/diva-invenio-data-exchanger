import pandas as pd


def parse_description(x):
    """Clean description field."""
    # TODO fix show nan on empty descriptions
    return x if pd.notnull(x) else ""
