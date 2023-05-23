import re


class AuthorBuilder:
    """
    Builds a dictionary of author information from a string.
    """

    def __init__(self, author):
        self.author = author
        self.author_dict = {}

        self.name_pattern = re.compile(r"^([\w\s,-]+)")
        self.orcid_pattern = re.compile(
            r"\b[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{3}[0-9A-Fa-fXx]\b"
        )
        self.affiliation_pattern = re.compile(r"\(([^)]+)\)")

        self.name_match = self.name_pattern.match(author)
        self.orcid_match = self.orcid_pattern.search(author)
        self.affiliation_matches = self.affiliation_pattern.findall(author)

    def build_name(self):
        """Build name."""
        name = self.name_match.group(1).strip() if self.name_match else ""
        if name and "," in name:
            givenName = name.split(",")[1].strip()
            familyName = name.split(",")[0].strip()
        else:
            givenName = "NotProvided"
            familyName = name if name else "NotProvided"

        self.author_dict["person_or_org"] = {
            "family_name": familyName,
            "given_name": givenName,
            "name": f"{givenName} {familyName}",
            "type": "personal",
        }

        return self

    def build_orcid(self):
        """Build ORCID."""
        orcid = self.orcid_match.group(0) if self.orcid_match else ""
        if orcid:
            self.author_dict["person_or_org"]["identifiers"] = [
                {"identifier": orcid, "scheme": "orcid"}
            ]

        return self

    def build_affiliations(self):
        affiliations = (
            [aff.strip() for aff in self.affiliation_matches]
            if self.affiliation_matches
            else []
        )
        if affiliations:
            self.author_dict["affiliations"] = [
                {"name": affiliation} for affiliation in affiliations
            ]

        return self

    def build(self):
        """Build the author dictionary."""
        return self.author_dict


def clean_name(creator_name):
    """
    Cleans a creator name string.
    """
    authors = creator_name.split(";")
    authors_list = []

    for author in authors:
        builder = AuthorBuilder(author)
        author_dict = builder.build_name().build_orcid().build_affiliations().build()
        authors_list.append(author_dict)

    return authors_list
