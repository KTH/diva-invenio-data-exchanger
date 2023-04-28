import json

import pandas as pd


def csv_to_json(csv_path, json_path):
    """CSV_to_JSON."""
    df = pd.read_csv(csv_path)
    with open(json_path, "w", encoding="utf-8") as f:
        f.write(df.to_json(orient="records", indent=4, force_ascii=False))
