# pylint: disable=unused-import
import json
import os
from unittest.mock import patch

import pytest
import typer
from typer.testing import CliRunner

from diva_invenio_data_exchanger.config import included_keys
from main import app
from tests.fixtures.output_fixtures import clear_output_file

runner = CliRunner()

# Get the absolute path of the directory containing the test file
current_dir = os.path.dirname(os.path.abspath(__file__))
fixtures_dir = os.path.join(current_dir, "fixtures")

# Define the input file path
input_file = os.path.join(fixtures_dir, "input/fixture.csv")
output_file = os.path.join(fixtures_dir, "output/fixture.json")


def test_main_raises_error_without_arguments():
    """Test that main() should raise SystemExit if no arguments passed."""
    result = runner.invoke(app)
    assert result.exit_code != 0


@pytest.mark.usefixtures("clear_output_file")
def test_main_runs_without_errors():
    """Test that main() runs without raising any exceptions when arguments passed."""
    result = runner.invoke(app, [input_file, output_file])
    assert result.exit_code == 0


@pytest.mark.usefixtures("clear_output_file")
def test_main_creates_output_file():
    """Test that main() creates an output file."""
    runner.invoke(app, [input_file, output_file])
    assert os.path.exists(output_file), "Output file was not created"


@pytest.mark.usefixtures("clear_output_file")
def test_main_output_file_contains_json_array():
    """Test that the output file created by main() contains a JSON array."""
    runner.invoke(app, [input_file, output_file])
    with open(output_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert isinstance(data, list), "Output file does not contain a JSON array"
        assert len(data) > 0, "Output file does not contain any JSON objects"
        # All required keys exist
        for key in included_keys:
            assert data[0][key]
