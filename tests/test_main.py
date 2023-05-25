# pylint: disable=unused-import
import json
import os
from unittest.mock import patch

import pytest

from diva_invenio_data_exchanger.utils.general import parse_arguments
from main import main
from tests.fixtures.output_fixtures import clear_output_file

# Get the absolute path of the directory containing the test file
current_dir = os.path.dirname(os.path.abspath(__file__))
fixtures_dir = os.path.join(current_dir, "fixtures")

# Define the input file path
input_file = os.path.join(fixtures_dir, "input/fixture.csv")
output_file = os.path.join(fixtures_dir, "output/fixture.json")


def test_main_raises_error_without_arguments():
    """Test that main() should raise SystemExit if no arguments passed."""
    with pytest.raises(SystemExit):
        main()


@pytest.mark.usefixtures("clear_output_file")
def test_main_runs_without_errors():
    """Test that main() runs without raising any exceptions when arguments passed."""
    with patch("sys.argv", ["prog_name", input_file, output_file]):
        # This will fail the test if main() raises an exception
        main()


@pytest.mark.usefixtures("clear_output_file")
def test_main_creates_output_file():
    """Test that main() creates an output file."""
    with patch("sys.argv", ["prog_name", input_file, output_file]):
        main()
        assert os.path.exists(output_file), "Output file was not created"


@pytest.mark.usefixtures("clear_output_file")
def test_main_output_file_contains_json_array():
    """Test that the output file created by main() contains a JSON array."""
    with patch("sys.argv", ["prog_name", input_file, output_file]):
        main()
        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert isinstance(data, list), "Output file does not contain a JSON array"
            assert len(data) > 0, "Output file does not contain any JSON objects"
