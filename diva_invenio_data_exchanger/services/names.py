import re


def clean_name(creator_name):
    """Cleanup name field."""
    name_pattern = re.compile(r"^([\w\s,-]+)")
    orcid_pattern = re.compile(
        r"\b[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{3}[0-9A-Fa-fXx]\b"
    )
    affiliation_pattern = re.compile(r"\(([^)]+)\)")

    authors = creator_name.split(";")

    authors_list = []

    if authors:
        for author in authors:
            name_match = name_pattern.match(author)
            orcid_match = orcid_pattern.search(author)
            affiliation_matches = affiliation_pattern.findall(author)

            name = name_match.group(1).strip() if name_match else "NotProvided"
            orcid = orcid_match.group(0) if orcid_match else "NotProvided"
            affiliations = (
                [aff.strip() for aff in affiliation_matches]
                if affiliation_matches
                else None
            )

            if name and "," in name:
                givenNames = name.split(",")[1]
                familyName = name.split(",")[0]
            else:
                givenNames = "NotProvided"
                familyName = name if name else "NotProvided"

            authors_list.append(
                {
                    "givenNames": givenNames,
                    "familyName": familyName,
                    "identifiers": orcid,
                    "affiliations": affiliations,
                    "role": "Researcher",
                }
            )

    return authors_list
