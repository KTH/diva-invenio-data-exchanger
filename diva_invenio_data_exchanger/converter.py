import re

import pandas as pd


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


def remove_html_tags(text):
    """Remove HTML tags."""
    return re.sub("<.*?>", "", text)


def clean_keywords(subject):
    """Cleanup subject field and return a list of dicts with subject as key."""
    sub = subject.split(";")
    return [{"subject": s} for s in sub]


def csv_to_json(csv_path, json_path):
    """CSV_to_JSON."""
    df = pd.read_csv(csv_path, encoding="utf-8")
    df = df.astype(str)
    df = df.applymap(remove_html_tags)

    # Define the mapping between old and new columns and their respective functions
    column_mapping = {
        "creators": {"old": "Name", "func": clean_name},
        "subjects": {"old": "Keywords", "func": clean_keywords},
        "title": {"old": "Title", "func": lambda x: x},  # No transformation function for title
        "description": {"old": "Abstract", "func": lambda x: x},
    }

    # Apply the transformations
    for new, info in column_mapping.items():
        df[new] = df[info['old']].apply(info['func'])

    # Create a metadata column that nests creators, subjects, and title
    df["metadata"] = df[list(column_mapping.keys())].to_dict('records')

    df_selected = df[["metadata"]]
    df_selected.to_json(json_path, orient="records", indent=4, force_ascii=False)
