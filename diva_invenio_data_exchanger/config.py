from diva_invenio_data_exchanger.services.description import clean_description
from diva_invenio_data_exchanger.services.keywords import clean_keywords
from diva_invenio_data_exchanger.services.names import clean_name
from diva_invenio_data_exchanger.services.resource_type import \
    translate_resource_type
from diva_invenio_data_exchanger.services.title import clean_title

mapping = {
    "resource_type": {"old": "PublicationType", "func": translate_resource_type},
    "description": {"old": "Abstract", "func": clean_description},
    "subjects": {"old": "Keywords", "func": clean_keywords},
    "creators": {"old": "Name", "func": clean_name},
    "title": {"old": "Title", "func": clean_title},
}
