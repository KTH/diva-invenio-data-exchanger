import argparse

from diva_invenio_data_exchanger.converter import csv_to_json


def main():
    """Initiate the app."""
    parser = argparse.ArgumentParser(description='Convert CSV file to JSON')
    parser.add_argument('input', help='Path to CSV file')
    parser.add_argument('output', help='Path to JSON file')
    args = parser.parse_args()

    csv_to_json(args.input, args.output)
    # csv_to_json("data/input/pub.csv", "data/output/pub.json")

if __name__ == "__main__":
    main()
