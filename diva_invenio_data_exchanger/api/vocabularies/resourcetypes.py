# Can be deleted after on the first release
# Unique values found in Diva data.
# TODO collect a full list to map it to the available ones in Invenio
diva_resourcetypes_json = [
    "Kapitel i bok, del av antologi"
    "Artikel, forskningsöversikt"
    "Samlingsverk (redaktörskap)"
    "Proceedings (redaktörskap)"
    "Artikel i tidskrift"
    "Artikel, recension"
    "Konferensbidrag"
    "Rapport"
    "Övrigt"
    "Patent"
    "Bok"
]

#
resourcetypes_titles = [
    "Annotation collection"
    "Data management plan"
    "Project deliverable"
    "Project milestone"
    "Conference paper"
    "Journal article"
    "Book section"
    "Presentation"
    "Publication"
    "Preprint"
    "Proposal"
    "Dataset"
    "Diagram"
    "Drawing"
    "Figure"
    "Lesson"
    "Poster"
    "Patent"
    "Image"
    "Other"
    "Other"
    "Other"
    "Photo"
    "Book"
    "Plot"
]

resource_type_ids = [
    "publication-annotationcollection"
    "publication-datamanagementplan"
    "publication-deliverable"
    "publication-milestone"
    "publication-preprint"
    "publication-section"
    "publication-proposal"
    "publication-article"
    "publication-patent"
    "publication-paper"
    "publication-other"
    "publication-book"
    "image-diagram"
    "image-drawing"
    "image-figure"
    "presentation"
    "image-other"
    "image-photo"
    "publication"
    "image-plot"
    "dataset"
    "image"
    "lesson"
    "poster"
    "other"
]

# For reference can be deleted later
# API responses for Invenio resources types
# {{baseURL}}/api/vocabularies/resourcetypes
resourcetypes_json_response = {
    "hits": {
        "hits": [
            {
                "id": "publication-annotationcollection",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.648031+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-annotationcollection"
                },
                "props": {
                    "csl": "report",
                    "datacite_general": "Collection",
                    "datacite_type": "",
                    "openaire_resourceType": "9",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/technicalDocumentation",
                    "schema.org": "https://schema.org/Collection",
                    "subtype": "publication-annotationcollection",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Annotation collection", "de": "Anmerkungssammlung"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.665849+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-book",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.646664+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-book"
                },
                "props": {
                    "csl": "book",
                    "datacite_general": "Text",
                    "datacite_type": "Book",
                    "openaire_resourceType": "2",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/book",
                    "schema.org": "https://schema.org/Book",
                    "subtype": "publication-book",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Book", "de": "Buch"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.664264+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-section",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.651184+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-section"
                },
                "props": {
                    "csl": "chapter",
                    "datacite_general": "Text",
                    "datacite_type": "Book section",
                    "openaire_resourceType": "13",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/bookPart",
                    "schema.org": "https://schema.org/ScholarlyArticle",
                    "subtype": "publication-section",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Book section", "de": "Buchkapitel"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.676484+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-paper",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.654529+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-conferencepaper"
                },
                "props": {
                    "csl": "paper-conference",
                    "datacite_general": "Text",
                    "datacite_type": "Conference paper",
                    "openaire_resourceType": "4",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/conferencePaper",
                    "schema.org": "https://schema.org/ScholarlyArticle",
                    "subtype": "publication-conferencepaper",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Conference paper", "de": "Konferenzbeitrag"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.671067+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-datamanagementplan",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.661492+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-datamanagementplan"
                },
                "props": {
                    "csl": "report",
                    "datacite_general": "Text",
                    "datacite_type": "Data management plan",
                    "openaire_resourceType": "9",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/technicalDocumentation",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "publication-datamanagementplan",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Data management plan", "de": "Datenmanagementplan"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.679658+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "dataset",
                "icon": "table",
                "created": "2023-05-15T21:45:49.769172+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/dataset"
                },
                "props": {
                    "csl": "dataset",
                    "datacite_general": "Dataset",
                    "datacite_type": "",
                    "openaire_resourceType": "21",
                    "openaire_type": "dataset",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/Dataset",
                    "subtype": "",
                    "type": "dataset",
                },
                "revision_id": 1,
                "title": {"en": "Dataset", "de": "Datensatz"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.793176+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "image-diagram",
                "icon": "chart bar outline",
                "created": "2023-05-15T21:45:49.807696+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/image-diagram"
                },
                "props": {
                    "csl": "figure",
                    "datacite_general": "Image",
                    "datacite_type": "Diagram",
                    "openaire_resourceType": "25",
                    "openaire_type": "dataset",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/ImageObject",
                    "subtype": "image-diagram",
                    "type": "image",
                },
                "revision_id": 1,
                "title": {"en": "Diagram", "de": "Diagramm"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.824457+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "image-drawing",
                "icon": "chart bar outline",
                "created": "2023-05-15T21:45:49.797932+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/image-drawing"
                },
                "props": {
                    "csl": "graphic",
                    "datacite_general": "Image",
                    "datacite_type": "Drawing",
                    "openaire_resourceType": "25",
                    "openaire_type": "dataset",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/ImageObject",
                    "subtype": "image-drawing",
                    "type": "image",
                },
                "revision_id": 1,
                "title": {"en": "Drawing", "de": "Zeichnung"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.813062+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "image-figure",
                "icon": "chart bar outline",
                "created": "2023-05-15T21:45:49.769436+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/image-figure"
                },
                "props": {
                    "csl": "figure",
                    "datacite_general": "Image",
                    "datacite_type": "Figure",
                    "openaire_resourceType": "25",
                    "openaire_type": "dataset",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/ImageObject",
                    "subtype": "image-figure",
                    "type": "image",
                },
                "revision_id": 1,
                "title": {"en": "Figure", "de": "Abbildung"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.789737+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "image",
                "icon": "chart bar outline",
                "created": "2023-05-15T21:45:49.767787+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/image"
                },
                "props": {
                    "csl": "figure",
                    "datacite_general": "Image",
                    "datacite_type": "",
                    "openaire_resourceType": "25",
                    "openaire_type": "dataset",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/ImageObject",
                    "subtype": "",
                    "type": "image",
                },
                "revision_id": 1,
                "title": {"en": "Image", "de": "Bild"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.788958+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-article",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.662993+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-article"
                },
                "props": {
                    "csl": "article-journal",
                    "datacite_general": "Text",
                    "datacite_type": "Journal article",
                    "openaire_resourceType": "1",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/article",
                    "schema.org": "https://schema.org/ScholarlyArticle",
                    "subtype": "publication-article",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Journal article", "de": "Zeitschriftenartikel"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.681440+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "lesson",
                "icon": "graduation",
                "created": "2023-05-15T21:45:49.831426+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/lesson"
                },
                "props": {
                    "csl": "speech",
                    "datacite_general": "InteractiveResource",
                    "datacite_type": "",
                    "openaire_resourceType": "10",
                    "openaire_type": "other",
                    "eurepo": "info:eu-repo/semantics/lecture",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "",
                    "type": "lesson",
                },
                "revision_id": 1,
                "title": {"en": "Lesson", "de": "Unterrichtseinheit"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.849751+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-other",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.764941+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-other"
                },
                "props": {
                    "csl": "article",
                    "datacite_general": "Text",
                    "datacite_type": "Other",
                    "openaire_resourceType": "20",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "publication-other",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Other", "de": "Sonstige"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.783019+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "image-other",
                "icon": "chart bar outline",
                "created": "2023-05-15T21:45:49.821180+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/image-other"
                },
                "props": {
                    "csl": "graphic",
                    "datacite_general": "Image",
                    "datacite_type": "Other",
                    "openaire_resourceType": "25",
                    "openaire_type": "dataset",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/ImageObject",
                    "subtype": "image-other",
                    "type": "image",
                },
                "revision_id": 1,
                "title": {"en": "Other", "de": "Sonstiges"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.837260+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "other",
                "icon": "asterisk",
                "created": "2023-05-15T21:45:49.822181+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/other"
                },
                "props": {
                    "csl": "article",
                    "datacite_general": "Other",
                    "datacite_type": "",
                    "openaire_resourceType": "20",
                    "openaire_type": "other",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "",
                    "type": "other",
                },
                "revision_id": 1,
                "title": {"en": "Other", "de": "Sonstige"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.840224+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-patent",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.672783+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-patent"
                },
                "props": {
                    "csl": "patent",
                    "datacite_general": "Text",
                    "datacite_type": "Patent",
                    "openaire_resourceType": "19",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/patent",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "publication-patent",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Patent", "de": "Patent"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.694577+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "image-photo",
                "icon": "chart bar outline",
                "created": "2023-05-15T21:45:49.814324+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/image-photo"
                },
                "props": {
                    "csl": "graphic",
                    "datacite_general": "Image",
                    "datacite_type": "Photo",
                    "openaire_resourceType": "25",
                    "openaire_type": "dataset",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/Photograph",
                    "subtype": "image-photo",
                    "type": "image",
                },
                "revision_id": 1,
                "title": {"en": "Photo", "de": "Foto"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.832521+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "image-plot",
                "icon": "chart bar outline",
                "created": "2023-05-15T21:45:49.789505+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/image-plot"
                },
                "props": {
                    "csl": "figure",
                    "datacite_general": "Image",
                    "datacite_type": "Plot",
                    "openaire_resourceType": "25",
                    "openaire_type": "dataset",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/ImageObject",
                    "subtype": "image-plot",
                    "type": "image",
                },
                "revision_id": 1,
                "title": {"en": "Plot", "de": "Plot"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.806619+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "poster",
                "icon": "columns",
                "created": "2023-05-15T21:45:49.764905+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/poster"
                },
                "props": {
                    "csl": "graphic",
                    "datacite_general": "Text",
                    "datacite_type": "Poster",
                    "openaire_resourceType": "4",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/conferencePoster",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "",
                    "type": "poster",
                },
                "revision_id": 1,
                "title": {"en": "Poster", "de": "Poster"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.786479+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-preprint",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.676034+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-preprint"
                },
                "props": {
                    "csl": "article",
                    "datacite_general": "Text",
                    "datacite_type": "Preprint",
                    "openaire_resourceType": "16",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/preprint",
                    "schema.org": "https://schema.org/ScholarlyArticle",
                    "subtype": "publication-preprint",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Preprint", "de": "Preprint"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.695516+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "presentation",
                "icon": "group",
                "created": "2023-05-15T21:45:49.765056+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/presentation"
                },
                "props": {
                    "csl": "speech",
                    "datacite_general": "Text",
                    "datacite_type": "Presentation",
                    "openaire_resourceType": "4",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/lecture",
                    "schema.org": "https://schema.org/PresentationDigitalDocument",
                    "subtype": "",
                    "type": "presentation",
                },
                "revision_id": 1,
                "title": {"en": "Presentation", "de": "Präsentation"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.783221+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-deliverable",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.683106+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-deliverable"
                },
                "props": {
                    "csl": "report",
                    "datacite_general": "Text",
                    "datacite_type": "Project deliverable",
                    "openaire_resourceType": "34",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/report",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "publication-deliverable",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Project deliverable", "de": "Projektergebnis"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.700827+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-milestone",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.691810+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-milestone"
                },
                "props": {
                    "csl": "report",
                    "datacite_general": "Text",
                    "datacite_type": "Project milestone",
                    "openaire_resourceType": "35",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/report",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "publication-milestone",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Project milestone", "de": "Projektmeilenstein"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.706040+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication-proposal",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.699878+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication-proposal"
                },
                "props": {
                    "csl": "article",
                    "datacite_general": "Text",
                    "datacite_type": "Proposal",
                    "openaire_resourceType": "36",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/researchProposal",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "publication-proposal",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Proposal", "de": "Antrag"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.714219+00:00",
                "type": "resourcetypes",
            },
            {
                "id": "publication",
                "icon": "file alternate",
                "created": "2023-05-15T21:45:49.642779+00:00",
                "links": {
                    "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes/publication"
                },
                "props": {
                    "csl": "report",
                    "datacite_general": "Text",
                    "datacite_type": "",
                    "openaire_resourceType": "17",
                    "openaire_type": "publication",
                    "eurepo": "info:eu-repo/semantics/other",
                    "schema.org": "https://schema.org/CreativeWork",
                    "subtype": "",
                    "type": "publication",
                },
                "revision_id": 1,
                "title": {"en": "Publication", "de": "Publikation"},
                "tags": ["depositable", "linkable"],
                "updated": "2023-05-15T21:45:49.660979+00:00",
                "type": "resourcetypes",
            },
        ],
        "total": 33,
    },
    "sortBy": "title",
    "links": {
        "self": "https://127.0.0.1:5000/api/vocabularies/resourcetypes?page=1&size=25&sort=title",
        "next": "https://127.0.0.1:5000/api/vocabularies/resourcetypes?page=2&size=25&sort=title",
    },
}
