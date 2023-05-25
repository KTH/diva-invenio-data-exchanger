# pylint: disable=unused-import
import json
import os
import sys
from unittest.mock import patch

import pytest

from diva_invenio_data_exchanger.utils.general import parse_arguments
from tests.fixtures.output_fixtures import clear_output_file
from main import main
import os

# Get the absolute path of the directory containing the test file
current_dir = os.path.dirname(os.path.abspath(__file__))


def test_main_raises_error_without_arguments():
    """Test that main() should raise SystemExit if no arguments passed."""
    with pytest.raises(SystemExit):
        main()


@pytest.mark.usefixtures("clear_output_file")
def test_main_runs_without_errors():
    """Test that main() runs without raising any exceptions when arguments passed."""
    input_file = os.path.join(current_dir, "fixtures/input/fixture.csv")
    output_file = os.path.join(current_dir, "fixtures/output/fixture.json")

    with patch("sys.argv", ["prog_name", input_file, output_file]):
        # This will fail the test if main() raises an exception
        main()


@pytest.mark.usefixtures("clear_output_file")
def test_main_creates_output_file():
    """Test that main() creates an output file."""
    input_file = os.path.join(current_dir, "fixtures/input/fixture.csv")
    output_file = os.path.join(current_dir, "fixtures/output/fixture.json")

    with patch("sys.argv", ["prog_name", input_file, output_file]):
        main()
        assert os.path.exists(output_file), "Output file was not created"


@pytest.mark.usefixtures("clear_output_file")
def test_main_output_file_contains_json_array():
    """Test that the output file created by main() contains a JSON array."""
    input_file = os.path.join(current_dir, "fixtures/input/fixture.csv")
    output_file = os.path.join(current_dir, "fixtures/output/fixture.json")

    with patch("sys.argv", ["prog_name", input_file, output_file]):
        main()
        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert isinstance(data, list), "Output file does not contain a JSON array"
            assert len(data) > 0, "Output file does not contain any JSON objects"
