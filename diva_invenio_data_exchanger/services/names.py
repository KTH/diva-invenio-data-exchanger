import json
import re
from abc import ABC, abstractmethod

import pandas as pd


class CreatorParserStrategy(ABC):
    @abstractmethod
    def parse(self, creator):
        pass


class IdentifierExtractor(ABC):
    @abstractmethod
    def extract(self, identifier):
        pass


class OrcidExtractor(IdentifierExtractor):
    ORCID_PATTERN = re.compile(
        r"\b[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{3}[0-9A-Fa-fXx]\b"
    )

    def extract(self, identifier):
        if self.ORCID_PATTERN.match(identifier):
            return "orcid", identifier
        return None, None


class KthidExtractor(IdentifierExtractor):
    KTHID_PATTERN = re.compile(r"\b[a-zA-Z0-9]{8}\b")

    def extract(self, identifier):
        if self.KTHID_PATTERN.match(identifier):
            return "kthid", identifier
        return None, None


class DefaultCreatorParserStrategy(CreatorParserStrategy):
    def __init__(self, identifier_extractors=None):
        if identifier_extractors is None:
            identifier_extractors = [OrcidExtractor(), KthidExtractor()]
        self.identifier_extractors = identifier_extractors

    def parse(self, creator):
        parts = creator.split(";")
        parsed_creators = []

        for part in parts:
            creator_data = self._parse_part(part)
            parsed_creators.append(creator_data)

        return parsed_creators

    def split_name(self, name):
        """Parse name."""
        if not name:
            return None, None

        parts = [part.strip() for part in name.split(",")]
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else None

        return first_name, last_name

    def _parse_part(self, part):
        creator_data = {}
        # split the part by parentheses and remove the parenthese
        split_data = re.split(r"\(.*?\)", part)
        # Etracting all bracketed expressions from the first item after the split
        identifiers = re.findall(r"\[(.*?)\]", split_data[0])
        # Remove the bracketed expressions
        name = re.sub(r"\[.*?\]", "", split_data[0]).strip()
        first_name, last_name = self.split_name(name)

        creator_data["person_or_org"] = {
            "family_name": last_name,
            "given_name": first_name,
            "name": f"{first_name} {last_name}",
            "type": "personal",
        }

        self._add_identifiers(creator_data, identifiers)
        self._add_affiliations(creator_data, split_data)

        return creator_data

    def _add_identifiers(self, creator_data, identifiers):
        if identifiers:
            creator_data["person_or_org"]["identifiers"] = []

            for identifier in identifiers:
                # identifier = identifier.strip()
                for extractor in self.identifier_extractors:
                    scheme, identifier_value = extractor.extract(identifier)
                    if scheme:
                        creator_data["person_or_org"]["identifiers"].append(
                            {"identifier": identifier_value, "scheme": scheme}
                        )
                        break
    # TODO needs imporvment
    def _add_affiliations(self, creator_data, split_data):
        if len(split_data) > 1:
            affiliations = split_data[1]
            creator_data["affiliations"] = [
                {"name": affiliation.strip()}
                for affiliation in re.split(r",\s*(?=[A-Z])", affiliations)
            ]


class CreatorParser:
    """
    Parser for creator strings.
    """

    def __init__(self, parser_strategy: CreatorParserStrategy = None):
        if parser_strategy is None:
            # TODO: Add KTHID when it's implemented in invenio instance
            # identifier_extractors = [OrcidExtractor(), KthidExtractor()]
            parser_strategy = DefaultCreatorParserStrategy(
                identifier_extractors=[OrcidExtractor()]
            )
        self.parser_strategy = parser_strategy

    def parse(self, creators):
        """
        Parse a list of creator strings.
        """
        return self.parser_strategy.parse(creators)


class MetadataBuilderStrategy(ABC):
    """
    Metadata builder strategy.
    """

    @abstractmethod
    def build_metadata(self, data, field):
        """Build metadata."""


class CreatorMetadataBuilderStrategy(MetadataBuilderStrategy):
    """
    Metadata builder for creators.
    """

    def __init__(self, creator_parser: CreatorParser):
        self.creator_parser = creator_parser

    def build_metadata(self, data, field="creators"):
        creators = self.creator_parser.parse(data["Name"])
        data[field] = creators
        return data


class MetadataBuilder:
    """
    Metadata builder.
    """

    def __init__(self, metadata_builder_strategy: MetadataBuilderStrategy):
        self.metadata_builder_strategy = metadata_builder_strategy

    def build_metadata(self, data, field):
        """
        Build metadata.
        """
        return self.metadata_builder_strategy.build_metadata(data, field)


def parse_name(creator_name):
    """
    Cleans a creator name string.
    """
    creator_parser = CreatorParser()

    return creator_parser.parse(creator_name)
