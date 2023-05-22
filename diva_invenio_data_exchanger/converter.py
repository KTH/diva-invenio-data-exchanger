import pandas as pd

from diva_invenio_data_exchanger.api.vocabularies.resourcetypes import \
    translate_resource_type
from diva_invenio_data_exchanger.services.description import clean_description
from diva_invenio_data_exchanger.services.keywords import clean_keywords
from diva_invenio_data_exchanger.services.names import clean_name
from diva_invenio_data_exchanger.utils.general import remove_html_tags


class MetadataMapper:
    def __init__(self, mapping):
        self.mapping = mapping

    def map(self, df):
        for new, info in self.mapping.items():
            df[new] = df[info["old"]].apply(info["func"])
        return df


class CsvToJsonConverter:
    def __init__(self, csv_path, json_path, metadata_mapper):
        self.csv_path = csv_path
        self.json_path = json_path
        self.metadata_mapper = metadata_mapper
        self.df = self.load_data()

    def load_data(self):
        df = pd.read_csv(self.csv_path, encoding="utf-8")
        df = df.astype(str)
        df = df.applymap(remove_html_tags)
        return df

    def convert(self):
        self.df = self.metadata_mapper.map(self.df)
        self.df["metadata"] = self.df[
            list(self.metadata_mapper.mapping.keys())
        ].to_dict("records")
        df_selected = self.df[["metadata"]]
        df_selected.to_json(
            self.json_path, orient="records", indent=4, force_ascii=False
        )


# def csv_to_json(csv_path, json_path):
#     """CSV_to_JSON."""
#     df = pd.read_csv(csv_path, encoding="utf-8")
#     df = df.astype(str)
#     df = df.applymap(remove_html_tags)

#     # Define the mapping between old and new columns and their respective functions
#     metadata_column_mapping = {
#         "creators": {"old": "Name", "func": clean_name},
#         "subjects": {"old": "Keywords", "func": clean_keywords},
#         "resource_type": {"old": "PublicationType", "func": translate_resource_type},
#         "title": {
#             "old": "Title",
#             "func": lambda x: x,
#         },  # No transformation function for title
#         "description": {"old": "Abstract", "func": clean_description},
#     }

#     # Apply the transformations
#     for new, info in metadata_column_mapping.items():
#         df[new] = df[info["old"]].apply(info["func"])

#     # Create a metadata column that nests creators, subjects, and title
#     df["metadata"] = df[list(metadata_column_mapping.keys())].to_dict("records")
#     df_selected = df[["metadata"]]
#     df_selected.to_json(json_path, orient="records", indent=4, force_ascii=False)
