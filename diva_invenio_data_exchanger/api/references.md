Intercepting the UI request to check the body structure its sending

without files request

```json
{
    "access": { "record": "public", "files": "public" },
    "metadata": {
        "publication_date": "2023-05-24",
        "publisher": "rdm-test-master",
        "rights": [
            { "id": "cc-by-4.0" },
            { "id": "apache-2.0" },
            { "id": "mit" }
        ],
        "title": "title title title title title",
        "creators": [
            {
                "person_or_org": {
                    "type": "personal",
                    "identifiers": [{ "identifier": "0000-0003-1892-9769" }],
                    "given_name": "Ange-Therese",
                    "family_name": "Akono"
                },
                "affiliations": [{ "name": "Northwestern University" }]
            }
        ],
        "contributors": [
            {
                "person_or_org": {
                    "type": "personal",
                    "identifiers": [{ "identifier": "0000-0003-1892-9769" }],
                    "given_name": "Ange-Therese",
                    "family_name": "Akono"
                },
                "role": { "id": "datacurator" },
                "affiliations": [{ "name": "Northwestern University" }]
            },
            {
                "person_or_org": {
                    "type": "personal",
                    "identifiers": [{ "identifier": "0000-0003-1892-9769" }],
                    "given_name": "Ange-Therese",
                    "family_name": "Akono"
                },
                "role": { "id": "distributor" },
                "affiliations": [{ "name": "Northwestern University" }]
            }
        ],
        "resource_type": { "id": "image-figure" },
        "dates": [
            {
                "date": "1984-11-04",
                "type": { "id": "accepted" },
                "description": "date description"
            }
        ],
        "languages": [{ "id": "eng" }, { "id": "swe" }],
        "identifiers": [
            { "scheme": "isbn", "identifier": "12312312312312" },
            { "scheme": "issn", "identifier": "123123123123" }
        ],
        "related_identifiers": [
            {
                "scheme": "issn",
                "identifier": "123123",
                "relation_type": { "id": "ispreviousversionof" },
                "resource_type": { "id": "poster" }
            },
            {
                "scheme": "igsn",
                "identifier": "12312312",
                "relation_type": { "id": "ispartof" },
                "resource_type": { "id": "presentation" }
            },
            {
                "scheme": "isbn",
                "identifier": "123123123",
                "relation_type": { "id": "isoriginalformof" },
                "resource_type": { "id": "publication-annotationcollection" }
            }
        ],
        "references": [
            { "reference": "qewqrasdfsdfsdsdgsdg" },
            { "reference": "sdgsdgsdgsdgsdg" },
            { "reference": "sdgsdgsdgsd" }
        ],
        "subjects": [
            {
                "id": "http://www.oecd.org/science/inno/38235147.pdf?4.2",
                "subject": "Animal and dairy science"
            },
            {
                "id": "http://www.oecd.org/science/inno/38235147.pdf?6.1",
                "subject": "History and archaeology"
            }
        ],
        "funding": [
            { "funder": { "id": "05k73zm37" } },
            { "funder": { "id": "03n51vw80" } }
        ],
        "version": "v11",
        "description": "<p>description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description</p>"
    },
    "files": { "enabled": true },
    "pids": {},
    "custom_fields": {}
}
```

You need to post the record before you upload the files, as you need the record ID,
PUT `/api/records/<recID>/draft`

POST `/api/records/<recID>/draft/files`

```json
[{ "key": "347805058_1500881493653073_2467532927364653686_n.jpg" }]
```

POST /api/records/<recID>/draft/files/347805058_1500881493653073_2467532927364653686_n.jpg/content

POST /api/records/y4j20-6r010/draft/files/347805058_1500881493653073_2467532927364653686_n.jpg/commit

req JSON body after uploading files and selecting community and submit for review:

```json
{
    "access": {
        "record": "public",
        "files": "public",
        "embargo": { "active": false },
        "status": "open"
    },
    "metadata": {
        "subjects": [
            {
                "id": "http://www.oecd.org/science/inno/38235147.pdf?4.2",
                "subject": "Animal and dairy science"
            },
            {
                "id": "http://www.oecd.org/science/inno/38235147.pdf?6.1",
                "subject": "History and archaeology"
            }
        ],
        "languages": [{ "id": "eng" }, { "id": "swe" }],
        "publication_date": "2023-05-24",
        "creators": [
            {
                "person_or_org": {
                    "type": "personal",
                    "name": "Akono, Ange-Therese",
                    "identifiers": [
                        {
                            "scheme": "orcid",
                            "identifier": "0000-0003-1892-9769"
                        }
                    ],
                    "given_name": "Ange-Therese",
                    "family_name": "Akono"
                },
                "role": { "id": "researcher" },
                "affiliations": [{ "name": "Northwestern University" }]
            }
        ],
        "additional_titles": [
            {
                "title": "asdasdasd",
                "type": { "id": "subtitle" },
                "lang": { "id": "swe" }
            }
        ],
        "references": [
            { "reference": "qewqrasdfsdfsdsdgsdg" },
            { "reference": "sdgsdgsdgsdgsdg" },
            { "reference": "sdgsdgsdgsd" }
        ],
        "funding": [
            { "funder": { "id": "05k73zm37" } },
            { "funder": { "id": "03n51vw80" } }
        ],
        "dates": [
            {
                "date": "1984-11-04",
                "type": { "id": "accepted" },
                "description": "date description"
            }
        ],
        "rights": [
            { "id": "cc-by-4.0" },
            { "id": "apache-2.0" },
            { "id": "mit" }
        ],
        "description": "<p>description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description&nbsp;description</p>",
        "title": "title title title title title",
        "resource_type": { "id": "image-figure" },
        "identifiers": [
            { "scheme": "isbn", "identifier": "12312312312312" },
            { "scheme": "issn", "identifier": "123123123123" }
        ],
        "publisher": "rdm-test-master",
        "related_identifiers": [
            {
                "scheme": "issn",
                "identifier": "123123",
                "relation_type": { "id": "ispreviousversionof" },
                "resource_type": { "id": "poster" }
            },
            {
                "scheme": "igsn",
                "identifier": "12312312",
                "relation_type": { "id": "ispartof" },
                "resource_type": { "id": "presentation" }
            },
            {
                "scheme": "isbn",
                "identifier": "123123123",
                "relation_type": { "id": "isoriginalformof" },
                "resource_type": { "id": "publication-annotationcollection" }
            }
        ],
        "contributors": [
            {
                "person_or_org": {
                    "name": "Akono, Ange-Therese",
                    "identifiers": [
                        {
                            "scheme": "orcid",
                            "identifier": "0000-0003-1892-9769"
                        }
                    ],
                    "type": "personal",
                    "given_name": "Ange-Therese",
                    "family_name": "Akono"
                },
                "role": { "id": "datacurator" },
                "affiliations": [{ "name": "Northwestern University" }]
            },
            {
                "person_or_org": {
                    "name": "Akono, Ange-Therese",
                    "identifiers": [
                        {
                            "scheme": "orcid",
                            "identifier": "0000-0003-1892-9769"
                        }
                    ],
                    "type": "personal",
                    "given_name": "Ange-Therese",
                    "family_name": "Akono"
                },
                "role": { "id": "distributor" },
                "affiliations": [{ "name": "Northwestern University" }]
            }
        ],
        "version": "v11"
    },
    "id": "y4j20-6r010",
    "links": {
        "self": "https://127.0.0.1:5000/api/records/y4j20-6r010/draft",
        "self_html": "https://127.0.0.1:5000/uploads/y4j20-6r010",
        "self_iiif_manifest": "https://127.0.0.1:5000/api/iiif/draft:y4j20-6r010/manifest",
        "self_iiif_sequence": "https://127.0.0.1:5000/api/iiif/draft:y4j20-6r010/sequence/default",
        "files": "https://127.0.0.1:5000/api/records/y4j20-6r010/draft/files",
        "archive": "https://127.0.0.1:5000/api/records/y4j20-6r010/draft/files-archive",
        "record": "https://127.0.0.1:5000/api/records/y4j20-6r010",
        "record_html": "https://127.0.0.1:5000/records/y4j20-6r010",
        "publish": "https://127.0.0.1:5000/api/records/y4j20-6r010/draft/actions/publish",
        "review": "https://127.0.0.1:5000/api/records/y4j20-6r010/draft/review",
        "submit-review": "https://127.0.0.1:5000/api/records/y4j20-6r010/draft/actions/submit-review",
        "versions": "https://127.0.0.1:5000/api/records/y4j20-6r010/versions",
        "access_links": "https://127.0.0.1:5000/api/records/y4j20-6r010/access/links",
        "reserve_doi": "https://127.0.0.1:5000/api/records/y4j20-6r010/draft/pids/doi",
        "communities": "https://127.0.0.1:5000/api/records/y4j20-6r010/communities",
        "communities-suggestions": "https://127.0.0.1:5000/api/records/y4j20-6r010/communities-suggestions",
        "requests": "https://127.0.0.1:5000/api/records/y4j20-6r010/requests"
    },
    "files": {
        "count": 2,
        "entries": {
            "347227817_266945559109294_2319182224917978737_n.jpg": {
                "ext": "jpg",
                "mimetype": "image/jpeg",
                "size": 449340,
                "metadata": { "width": 1536, "height": 2048 },
                "key": "347227817_266945559109294_2319182224917978737_n.jpg"
            },
            "347805058_1500881493653073_2467532927364653686_n.jpg": {
                "ext": "jpg",
                "mimetype": "image/jpeg",
                "size": 1099437,
                "metadata": { "width": 2048, "height": 1385 },
                "key": "347805058_1500881493653073_2467532927364653686_n.jpg"
            }
        },
        "total_bytes": 1548777,
        "enabled": true
    },
    "parent": {
        "review": {
            "id": "370f3129-75f2-4014-bcc1-bf99bfac07ad",
            "status": "created",
            "receiver": { "community": "5147278c-8074-46bf-8e04-5c09b9850e22" },
            "type": "community-submission"
        },
        "id": "pf90r-d5237",
        "access": { "owned_by": [{ "user": 3 }] }
    },
    "pids": {},
    "custom_fields": {}
}
```
