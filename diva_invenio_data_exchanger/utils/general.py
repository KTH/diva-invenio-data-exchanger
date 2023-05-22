import argparse
import re

import click


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


def display_message(message, color="green"):
    """Helper function to display messages with specified color.
    available colors: green, red, yellow, blue, magenta, cyan, white.
    :param message: message to display
    :param color: color of message to display
    :return: None

    """
    click.secho(message, fg=color)


def remove_html_tags(text):
    """Remove HTML tags."""
    return re.sub("<.*?>", "", text)


class Dotdict(dict):
    """Access dictionary using dot notation."""

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def is_valid_url(url):
    """validate url"""
    url_pattern = re.compile(
        r"^(?:http|https)://"  # Scheme (http or https)
        r"(?:(?:[A-Z0-9_](?:[A-Z0-9_-]{0,61}[A-Z0-9_])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # Domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or IP
        r"(?::\d+)?"  # Optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    return re.match(url_pattern, url) is not None


def is_orcid(id):
    """Test ORCID patterns"""
    orcid_pattern = re.compile(
        r"\b[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{3}[0-9A-Fa-fXx]\b"
    )
    x = orcid_pattern.findall(id)
    return x
