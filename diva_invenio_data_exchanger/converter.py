import pandas as pd

from diva_invenio_data_exchanger.utils.general import remove_html_tags


class DataMapper:
    """Data mapper class.
    Args:
        mapping (dict): Mapping of new column names to old column names and
            functions to be applied to the old column.
    """

    def __init__(self, mapping):
        self.mapping = mapping

    def map(self, df):
        """Applies mapping to dataframe.
        Args:
            df (pd.DataFrame): Dataframe to be mapped.
        Returns:
            pd.DataFrame: Dataframe with mapped columns.
        """
        for new, info in self.mapping.items():
            df[new] = df[info["old"]].apply(info["func"])
        return df


class CsvToJsonConverter:
    """CSV to JSON converter"""

    def __init__(self, csv_path, json_path, metadata_mapper):
        self.csv_path = csv_path
        self.json_path = json_path
        self.metadata_mapper = metadata_mapper
        self.df = self.load_data()

    def load_data(self):
        """Loads data from CSV file and converts to string type.
        Returns:
            pd.DataFrame: Dataframe with string type.
        """
        df = pd.read_csv(self.csv_path, encoding="utf-8")
        df = df.astype(str)
        # Gloably applied functions
        df = df.applymap(remove_html_tags)
        return df

    def convert(self):
        """Converts CSV to JSON and saves it to file."""
        self.df = self.metadata_mapper.map(self.df)
        # Nest mapped data under metadata key
        self.df["metadata"] = self.df[
            list(self.metadata_mapper.mapping.keys())
        ].to_dict("records")
        # keep only metadata column
        df_selected = self.df[["metadata"]]
        # TODO add the rest of the columns

        # Convert to JSON and save to file
        df_selected.to_json(
            self.json_path, orient="records", indent=4, force_ascii=False
        )
