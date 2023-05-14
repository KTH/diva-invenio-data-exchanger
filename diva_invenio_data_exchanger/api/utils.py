import re


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


def remove_html_tags(text):
    """Remove HTML tags."""
    return re.sub("<.*?>", "", text)
