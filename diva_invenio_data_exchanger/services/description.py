import pandas as pd


def parse_description(x):
    """Clean description field."""
    return x if pd.notnull(x) else ""
