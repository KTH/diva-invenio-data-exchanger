import pandas as pd


def clean_description(x):
    """Clean description field."""
    return x if pd.notnull(x) else None
