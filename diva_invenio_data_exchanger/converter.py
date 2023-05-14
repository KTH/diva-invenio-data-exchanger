import re

import pandas as pd


def clean_name(namee):
    """Cleanup name field."""
    name_pattern = re.compile(r"^([\w\s,-]+)")
    orcid_pattern = re.compile(
        r"\b[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{3}[0-9A-Fa-fXx]\b"
    )
    affiliation_pattern = re.compile(r"\(([^)]+)\)")

    authors = namee.split(";")

    authors_list = []

    if authors:
        for author in authors:
            name_match = name_pattern.match(author)
            orcid_match = orcid_pattern.search(author)
            affiliation_matches = affiliation_pattern.findall(author)

            name = name_match.group(1).strip() if name_match else None
            orcid = orcid_match.group(0) if orcid_match else None
            affiliations = (
                [aff.strip() for aff in affiliation_matches]
                if affiliation_matches
                else None
            )

            if name and "," in name:
                givenNames = name.split(",")[1]
                familyName = name.split(",")[0]
            else:
                givenNames = "Not provided"
                familyName = name if name else "Not provided"

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


def csv_to_json(csv_path, json_path):
    """CSV_to_JSON."""
    df = pd.read_csv(csv_path)
    df = df.astype(str)
    df = df.applymap(remove_html_tags)
    df["Name"] = df["Name"].apply(clean_name)
    df["Keywords"] = df["Keywords"].str.split(";")
    # df['Title'] = df['Title'].apply(html.unescape).str.replace(r'<[^<>]*>', '', regex=True)
    df.to_json(json_path, orient="records", indent=4, force_ascii=False)
