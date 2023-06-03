import typer
from rich import pretty
from rich.traceback import install

from diva_invenio_data_exchanger.config import metadata_mapping
from diva_invenio_data_exchanger.converter import (CsvToJsonConverter,
                                                   DataMapper)
from diva_invenio_data_exchanger.utils.general import display_message

app = typer.Typer()

# https://rich.readthedocs.io/en/latest/traceback.html#traceback-handler
install(show_locals=True)
# any data structures will be pretty printed and highlighted
pretty.install()


@app.command()
def convert(
    path_in: str = typer.Argument(..., help="Input file path"),
    path_out: str = typer.Argument(..., help="Output file path"),
):  # "..." will make typer see the arguments as required
    """Initiate the app."""
    data_mapper = DataMapper(metadata_mapping)
    converter = CsvToJsonConverter(path_in, path_out, data_mapper)
    display_message(
        f"Converting... from [yellow bold]{path_in}[/yellow bold] to [yellow bold]{path_out}[/yellow bold]",
        "blue",
    )
    converter.convert()
    display_message(
        f"Conversion completed successfully in [yellow bold]{path_out}[/yellow bold]"
    )


if __name__ == "__main__":
    app()
