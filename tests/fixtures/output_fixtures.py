import os

import pytest


@pytest.fixture(autouse=True)
def clear_output_file():
    # Setup: Nothing to do before the test

    yield  # This is where the testing happens

    # Teardown: Remove the output file after the test
    output_file = "tests/fixtures/output/fixture.json"
    if os.path.exists(output_file):
        with open(output_file, "w") as f:
            f.truncate(0)
