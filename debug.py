import json
import re
from abc import ABC, abstractmethod

import pandas as pd

# TODO delete this file
# For debugging purposes only

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

    def _parse_part(self, part):
        creator_data = {}
        split_data = re.split(r"\(.*?\)", part)

        identifiers = re.findall(r"\[(.*?)\]", split_data[0])
        name = re.sub(r"\[.*?\]", "", split_data[0]).strip()
        last_name, first_name = name.split(",")

        creator_data["person_or_org"] = {
            "family_name": last_name.strip(),
            "given_name": first_name.strip(),
            "name": f"{first_name.strip()} {last_name.strip()}",
            "type": "personal",
        }

        self._add_identifiers(creator_data, identifiers)
        self._add_affiliations(creator_data, split_data)

        return creator_data

    def _add_identifiers(self, creator_data, identifiers):
        if identifiers:
            creator_data["person_or_org"]["identifiers"] = []

            for identifier in identifiers:
                identifier = identifier.strip()
                for extractor in self.identifier_extractors:
                    scheme, identifier_value = extractor.extract(identifier)
                    if scheme:
                        creator_data["person_or_org"]["identifiers"].append(
                            {"identifier": identifier_value, "scheme": scheme}
                        )
                        break

    def _add_affiliations(self, creator_data, split_data):
        if len(split_data) > 1:
            affiliations = split_data[1]
            creator_data["affiliations"] = [
                {"name": affiliation.strip()}
                for affiliation in re.split(r",\s*(?=[A-Z])", affiliations)
            ]


class CreatorParser:
    def __init__(self, parser_strategy: CreatorParserStrategy = None):
        if parser_strategy is None:
            parser_strategy = DefaultCreatorParserStrategy()
        self.parser_strategy = parser_strategy

    def parse(self, creators):
        return self.parser_strategy.parse(creators)


class MetadataBuilderStrategy(ABC):
    @abstractmethod
    def build_metadata(self, data, field):
        pass


class CreatorMetadataBuilderStrategy(MetadataBuilderStrategy):
    def __init__(self, creator_parser: CreatorParser):
        self.creator_parser = creator_parser

    def build_metadata(self, data, field="creators"):
        creators = self.creator_parser.parse(data["Name"])
        data[field] = creators
        return data


class MetadataBuilder:
    def __init__(self, metadata_builder_strategy: MetadataBuilderStrategy):
        self.metadata_builder_strategy = metadata_builder_strategy

    def build_metadata(self, data, field):
        return self.metadata_builder_strategy.build_metadata(data, field)


def main():
    df = pd.read_csv("data/input/pub.csv")
    data = df.to_dict(orient="records")[0]

    creator_parser = CreatorParser()
    metadata_builder_strategy = CreatorMetadataBuilderStrategy(creator_parser)
    metadata_builder = MetadataBuilder(metadata_builder_strategy)
    processed_data = metadata_builder.build_metadata(data, field="contributors")

    print(json.dumps(processed_data, indent=4))


if __name__ == "__main__":
    main()
