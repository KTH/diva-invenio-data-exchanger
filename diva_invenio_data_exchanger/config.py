from diva_invenio_data_exchanger.services.description import parse_description
from diva_invenio_data_exchanger.services.keywords import parse_keywords
from diva_invenio_data_exchanger.services.language import parse_language
from diva_invenio_data_exchanger.services.names import parse_name
from diva_invenio_data_exchanger.services.resource_type import \
    parse_resource_type
from diva_invenio_data_exchanger.services.title import parse_title

metadata_mapping = {
    "resource_type": {"old": "PublicationType", "func": parse_resource_type},
    "description": {"old": "Abstract", "func": parse_description},
    "subjects": {"old": "Keywords", "func": parse_keywords},
    "creators": {"old": "Name", "func": parse_name},
    "title": {"old": "Title", "func": parse_title},
    "publication_date": {"old": "PublicationDate", "func": parse_title},
    "languages": {"old": "Language", "func": parse_language},
}


invenio_requiered_fields = {
    "access": {"record": "public", "files": "public"},
    "files": {"enabled": False},
    "type": "community-submission",
    "pids": {},
    "custom_fields": {},
}
