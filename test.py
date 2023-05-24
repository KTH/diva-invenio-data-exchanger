import pandas as pd
import re
import json
from abc import ABC, abstractmethod

class CreatorParserStrategy(ABC):
    @abstractmethod
    def parse(self, creator):
        pass

class DefaultCreatorParserStrategy(CreatorParserStrategy):
    def parse(self, creator):
        parts = creator.split(";")
        parsed_creators = []

        for part in parts:
            creator_data = {}
            #  re -> splits the input string at each pair of parentheses ().
            split_data = re.split(r'\(.*?\)', part)

            last_name, first_name, *other = split_data[0].split(',')

            creator_data['person_or_org'] = {
                'family_name': last_name.strip(),
                'given_name': first_name.strip(),
                'name': f"{first_name.strip()} {last_name.strip()}",
                'type': 'personal'
            }
            # re -> finds all substrings enclosed within square brackets [].
            if other and re.findall(r'\[.*\]', other[0]):
                creator_data['person_or_org']['identifiers'] = [{
                    'identifier': re.findall(r'\[.*\]', other[0])[0][1:-1],
                    'scheme': 'orcid'
                }]

            if len(split_data) > 1:
                affiliations = split_data[1]
                creator_data['affiliations'] = [
                    {'name': affiliation.strip()}
                    # Splits the string at commas followed by a whitespace, only if the next character is an uppercase letter.
                    for affiliation in re.split(r',\s*(?=[A-Z])', affiliations)
                ]

            parsed_creators.append(creator_data)
        return parsed_creators


class CreatorParser:
    def __init__(self, parser_strategy: CreatorParserStrategy = None):
        if parser_strategy is None:
            parser_strategy = DefaultCreatorParserStrategy()
        self.parser_strategy = parser_strategy

    def parse(self, creators):
        return self.parser_strategy.parse(creators)


class MetadataBuilder:
    def __init__(self, creator_parser: CreatorParser):
        self.creator_parser = creator_parser

    def build_metadata(self, data, field="creators"):
        """Build metadata.
        field can take creators or contributors"""
        creators = self.creator_parser.parse(data['Name'])
        data[field] = creators  # 'metadata' key is not used here
        return data


def main():
    df = pd.read_csv('data/input/pub.csv')
    data = df.to_dict(orient='records')[0]

    metadata_builder = MetadataBuilder(CreatorParser())
    processed_data = metadata_builder.build_metadata(data, field="contributors")

    print(json.dumps(processed_data, indent=4))


if __name__ == "__main__":
    main()
