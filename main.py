from diva_invenio_data_exchanger.config import mapping
from diva_invenio_data_exchanger.converter import (CsvToJsonConverter,
                                                   DataMapper)
from diva_invenio_data_exchanger.utils.general import (display_message,
                                                       parse_arguments)


def main():
    """Initiate the app."""
    args = parse_arguments()

    try:
        data_mapper = DataMapper(mapping)
        converter = CsvToJsonConverter(args.input, args.output, data_mapper)
        display_message(f"converting... from {args.input} to {args.output}", "blue")
        converter.convert()
        display_message("conversion completed successfully! \nYou can find the result in:")
        display_message(f"{args.output}", "yellow")

    # pylint: disable=broad-exception-caught
    except Exception as e:
        display_message(f"conversion failed: {e}", "red")


if __name__ == "__main__":
    main()
