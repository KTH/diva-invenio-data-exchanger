def parse_keywords(subject):
    """Cleanup subject field and return a list of dicts with subject as key."""
    # TODO find a way to match with Invenio subjects
    # {{baseURL}}/api/subjects?suggest={{subject-query}}
    # https://inveniordm.docs.cern.ch/reference/rest_api_vocabularies/#search-vocabularies
    if not subject or subject == "nan":
        return []
    sub = subject.split(";")
    return [{"subject": s} for s in sub]
