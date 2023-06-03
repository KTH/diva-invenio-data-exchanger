import argparse
import re

from rich.console import Console

console = Console()


def parse_arguments():
    """Parse command-line arguments."""
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
    return parser.parse_args()


def display_message(message, color="green", **kwargs):
    """Helper function to display messages with specified color.
    available colors: green, red, yellow, blue, magenta, cyan, white.
    :param message: message to display
    :param color: color of message to display
    :return: None

    """
    console.print(message, style=color, **kwargs)


def remove_html_tags(text):
    """Remove HTML tags."""
    return re.sub("<.*?>", "", text)
