"""Simple test of version import."""


def test_version():
    """Test version import."""
    from diva_invenio_data_exchanger import __version__

    assert __version__
