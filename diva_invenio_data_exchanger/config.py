from diva_invenio_data_exchanger.services.metadata import (parse_description,
                                                           parse_keywords,
                                                           parse_language,
                                                           parse_name,
                                                           parse_resource_type,
                                                           parse_title)

metadata_mapping = {
    "resource_type": {"dataKey": "PublicationType", "func": parse_resource_type},
    "description": {"dataKey": "Abstract", "func": parse_description},
    "subjects": {"dataKey": "Keywords", "func": parse_keywords},
    "creators": {"dataKey": "Name", "func": parse_name},
    "title": {"dataKey": "Title", "func": parse_title},
    "publication_date": {"dataKey": "PublicationDate", "func": parse_title},
    "languages": {"dataKey": "Language", "func": parse_language},
}


invenio_requiered_fields = {
    "access": {"record": "public", "files": "public"},
    "files": {"enabled": False},
    "type": "community-submission",
    "pids": {},
    "custom_fields": {},
}

included_keys = ["access", "files", "type", "metadata"]
