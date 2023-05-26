import re
from abc import ABC, abstractmethod


class CreatorParserStrategy(ABC):
    @abstractmethod
    def parse(self, creator):
        """Parse creator."""


class StringExtractor(ABC):
    """String extractor."""

    @abstractmethod
    def extract(self, identifier):
        """Extract identifier."""


class OrcidExtractor(StringExtractor):
    """Extract ORCID from identifier."""

    ORCID_PATTERN = re.compile(
        r"\b[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{3}[0-9A-Fa-fXx]\b"
    )

    def extract(self, identifier):
        if self.ORCID_PATTERN.match(identifier):
            return "orcid", identifier
        return None, None


class KthidExtractor(StringExtractor):
    """Extract KTHID from identifier."""

    KTHID_PATTERN = re.compile(r"\b[a-zA-Z0-9]{8}\b")

    def extract(self, identifier):
        if self.KTHID_PATTERN.match(identifier):
            return "kthid", identifier
        return None, None


class PersonOrOrgParserStrategy(CreatorParserStrategy):
    """Parse person or organization."""

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
        if not identifiers:
            return None

        creator_data["person_or_org"]["identifiers"] = [
            self._extract_identifier(identifier)
            for identifier in identifiers
            if self._extract_identifier(identifier) is not None
        ]

    def _extract_identifier(self, identifier):
        for extractor in self.identifier_extractors:
            scheme, identifier_value = extractor.extract(identifier)
            if scheme:
                return {"identifier": identifier_value, "scheme": scheme}
        return None

    # TODO needs imporvment
    # replace [id] with corresponding value
    def _add_affiliations(self, creator_data, split_data):
        if len(split_data) <= 1:
            return

        affiliations = split_data[1]
        creator_data["affiliations"] = self._create_affiliations(affiliations)

    def _create_affiliations(self, affiliations):
        affiliation_list = re.split(r",\s*(?=[A-Z])", affiliations)
        return [
            {"name": affiliation.strip()}
            for affiliation in affiliation_list
            if affiliation.strip()  # Exclude empty names
        ]


class CreatorParser:
    """
    Parser for creator strings.
    """

    def __init__(self, parser_strategy: CreatorParserStrategy = None):
        if parser_strategy is None:
            # TODO: Add KTHID when it's implemented in invenio instance
            # identifier_extractors = [OrcidExtractor(), KthidExtractor()]
            parser_strategy = PersonOrOrgParserStrategy(
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

    # Split the input on semicolon to get the individual creators.
    creators = creator_name.split(";")

    output = []
    for creator in creators:
        if creator.strip() == '':
            continue
        # Split on the first occurrence of parenthesis to separate name, id and affiliations
        parts = re.split(r'\s*\(\s*(.*?)\s*\)\s*', creator, maxsplit=1)
        # import pdb; pdb.set_trace()

        # Handling the part outside of parentheses
        # Extracting the name, kthid and orcid
        name_id_part = parts[0].strip().split('[')
        first_last_name = name_id_part[0].strip().split(',')
        last_name = first_last_name[0].strip()
        first_name = first_last_name[1].strip() if len(first_last_name) > 1 else ''


        def parse_identifiers(string, kth_id=True):
            res = []
            ids = re.findall(r'\[(.*?)\]', string)
            kthid = ids[0] if len(ids) > 0 else None
            orcid = ids[1] if len(ids) > 1 else None

            if not kthid and not orcid:
                return None

            if kth_id and kthid:
                res.append({
                    'identifier': kthid,
                    "scheme": "kthid"
                })

            if not orcid:
                return res

            res.append({
                    "identifier": orcid,
                    "scheme": "orcid"
                })
            return res

        identifiers = parse_identifiers(parts[0],  kth_id=False)
        # Handling the part inside of parentheses
        affiliations = []
        if len(parts) > 1:
            aff_part = parts[1].replace(')', '')
            affiliations = [{"name": aff.strip()} for aff in aff_part.split(',')]
        result = {
            'given_name': first_name,
            'family_name': last_name,
            'affiliations': affiliations
            }

        if identifiers:
            result['identifiers'] = identifiers

        output.append(result)

    return output
