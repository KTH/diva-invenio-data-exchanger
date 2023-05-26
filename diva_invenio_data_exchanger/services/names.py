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
        """
        Abstract method to parse data.
        """


class NamesParser(Parser):
    """
    Class to parse the names of creators.
    """

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
        output = []
        for creator in creators:
            if creator.strip() == "":
                continue

            output.append(self.parse_creator(creator))

        return output

    def parse_creator(self, creator):
        """
        Parses a creator's name string into its constituent parts.
        """
        # Split the string at parentheses, capturing the content in between
        parts = re.split(r"\s*\(\s*(.*?)\s*\)\s*", creator, maxsplit=1)

        name_id_part = parts[0].strip().split("[")
        first_last_name = name_id_part[0].strip().split(",")
        last_name = first_last_name[0].strip()
        first_name = first_last_name[1].strip() if len(first_last_name) > 1 else ""
        # TODO flip kth_id True when it's populated in Invenio
        identifiers = self.parse_identifiers(parts[0], kth_id=False)

        affiliations = []
        if len(parts) > 1:
            aff_part = parts[1].replace(")", "").replace("(", "")
            affiliations = [{"name": aff.strip()} for aff in aff_part.split(",")]

        person_or_org = {
            "given_name": first_name,
            "family_name": last_name,
            "type": "personal",
        }

        if identifiers:
            person_or_org["identifiers"] = identifiers

        if affiliations:
            person_or_org["affiliations"] = affiliations

        result = {"person_or_org": person_or_org}
        return result

    @staticmethod
    def parse_identifiers(string, kth_id=True):
        """
        Parses identifiers in a string.
        """
        res = []
        # Find all identifiers in brackets
        ids = re.findall(r"\[(.*?)\]", string)
        kthid = ids[0] if len(ids) > 0 else None
        orcid = ids[1] if len(ids) > 1 else None

        if not kthid and not orcid:
            return None

        if kth_id and kthid:
            res.append({"identifier": kthid, "scheme": "kthid"})

        if orcid:
            res.append({"identifier": orcid, "scheme": "orcid"})

        return res


def parse_name(creator_names):
    """
    Parses and cleans creator names using the NamesParser class.
    """

    creators = NamesParser(creator_names)
    return creators.parse()
