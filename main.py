import argparse

from diva_invenio_data_exchanger.converter import csv_to_json


def main():
    """Initiate the app."""
    parser = argparse.ArgumentParser(description="Convert CSV file to JSON")
    parser.add_argument(
        "input",
        default="data/input/pub.csv",
        help="Path to read the CSV file",
        type=str,
    )
    parser.add_argument(
        "output",
        default="data/output/pub.json",
        help="Path to write the JSON file",
        type=str,
    )
    args = parser.parse_args()

    csv_to_json(args.input, args.output)


if __name__ == "__main__":
    main()
