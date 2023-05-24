def clean_language(language):
    """Clean language."""
    return [{"id": language.strip().lower()}]
