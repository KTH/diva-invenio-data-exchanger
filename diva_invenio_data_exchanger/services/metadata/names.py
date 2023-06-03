import re
from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Abstract class for a generic parser.

    This class is meant to be subclassed by any class that needs to
    parse data. The subclass is required to implement the parse method.
    """

    @abstractmethod
    def parse(self):
        """Abstract method to parse data."""


class NamesParser(Parser):
    """Class to parse the names of creators."""

    def __init__(self, creator_name):
        """
        Initializes the NamesParser with a creator name.
        """
        self.creator_name = creator_name

    def parse(self):
        """
        Splits the creator's name into individual parts and parses each part.
        """
        creators = self.creator_name.split(";")
        return [self.parse_creator(creator) for creator in creators if creator.strip()]

    @staticmethod
    def _extract_name_parts(name_id_part):
        """Extracts the first and last name from the given name_id_part."""
        first_last_name = name_id_part.strip().split(",")
        last_name = first_last_name[0].strip()
        first_name = first_last_name[1].strip() if len(first_last_name) > 1 else ""
        return first_name, last_name

    @staticmethod
    def _build_person_or_org(first_name, last_name, identifiers, affiliations):
        """Builds a dictionary representing a person or organization."""
        person_or_org = {
            "given_name": first_name,
            "family_name": last_name,
            "type": "personal",  # TODO make this required field dynamic
        }

        if identifiers:
            person_or_org["identifiers"] = identifiers

        if affiliations:
            person_or_org["affiliations"] = affiliations

        return {"person_or_org": person_or_org}

    def parse_creator(self, creator):
        """Parses a creator's name string into its constituent parts."""
        # Split the string at parentheses, capturing the content in between
        parts = re.split(r"\s*\(\s*(.*?)\s*\)\s*", creator, maxsplit=1)
        name_id_part = parts[0].strip().split("[")

        # Extract the first and last name from name_id_part
        first_name, last_name = self._extract_name_parts(name_id_part[0])

        # TODO flip kth_id True when it's populated in Invenio
        identifiers = self.parse_identifiers(parts[0], kth_id=False)

        # Process affiliations
        affiliations = self.process_affiliation(parts)

        # Build and return the result
        return self._build_person_or_org(
            first_name, last_name, identifiers, affiliations
        )

    def process_affiliation(self, parts):
        """Parses affiliations from a list of parts."""
        if len(parts) <= 1:
            return []

        # Remove parentheses
        aff_part = re.sub(r"[()]", "", parts[1])

        # Split at commas and build a list of affiliations
        return [{"name": aff.strip()} for aff in aff_part.split(",")]

    @staticmethod
    def is_orcid(orcid):
        """Validates an ORCID string."""
        pattern = r"^\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"
        return bool(re.match(pattern, orcid))

    @staticmethod
    def parse_identifiers(string, kth_id=True):
        """Parses identifiers in a string."""
        res = []
        # Find all identifiers in brackets
        ids = re.findall(r"\[(.*?)\]", string)
        kthid = ids[0] if len(ids) > 0 else None
        orcid = ids[1] if len(ids) > 1 and NamesParser.is_orcid(ids[1]) else None

        if not kthid and not orcid:
            return None

        if kth_id and kthid:
            res.append({"identifier": kthid, "scheme": "kthid"})

        if orcid:
            res.append({"identifier": orcid, "scheme": "orcid"})

        return res


def parse_name(creator_names):
    """Parses and cleans creator names using the NamesParser class."""

    creators = NamesParser(creator_names)
    return creators.parse()
