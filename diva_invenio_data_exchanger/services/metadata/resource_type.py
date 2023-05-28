def parse_resource_type(resource_type):
    """Map Swedish resource type to English."""
    # TODO double check with librarians if this mapping is correct
    translation_mapping = {
        "Konferensbidrag": "publication-other",
        "Artikel i tidskrift": "publication-article",
        "Kapitel i bok, del av antologi": "publication-section",
        "Bok": "publication-book",
        "Rapport": "publication-other",
        "Övrigt": "other",
        "Artikel, forskningsöversikt": "publication-other",
        "Patent": "publication-patent",
        "Proceedings (redaktörskap)": "publication",
        "Artikel, recension": "publication-other",
        "Samlingsverk (redaktörskap)": "publication",
    }
    # TODO Check what is the default value for the resource type when it is not provided
    return {"id": translation_mapping.get(resource_type, "other")}
