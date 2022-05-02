import os
import json
from urllib.request import urlopen

from ruamel.yaml import YAML

from . import parse_issue_body
from .add_publication import format_parsed_content, write_content_to_file


def fetch_content(parsed):

    method = parsed["method"]
    identifier = parsed["identifier"]

    url = urlopen(
        f"https://api.semanticscholar.org/graph/v1/paper/{method}:{identifier}?fields=title,venue,year,authors.name,externalIds,url,abstract"
    )
    data = json.loads(url.read())

    return data


def wrangle_fetched_content(parsed, paper_json):
    with open("_data/authors.yml") as f:
        lab_members = YAML().safe_load(f)

    paper_json["month"] = parsed.get("month", "01")
    paper_json["day"] = parsed.get("day", "01")

    author_names = [parsed["name"] for parsed in paper_json["authors"]]
    paper_json["names"] = ", ".join(author_names)
    paper_json["tags"] = paper_json["venue"]
    paper_json["venue"] = f"{paper_json['venue']} {paper_json['year']}"
    paper_json["shorthand"] = str(paper_json["paperId"])
    paper_json["year"] = str(paper_json["year"])
    paper_json["link"] = paper_json["url"]

    if "ArXiv" in paper_json["externalIds"]:
        paper_json[
            "link"
        ] = f"https://arxiv.org/abs/{paper_json['externalIds']['ArXiv']}"
        paper_json["shorthand"] = paper_json["externalIds"]["ArXiv"]
    elif "DOI" in paper_json["externalIds"]:
        paper_json["link"] = f"https://doi.org/{paper_json['externalIds']['DOI']}"
        paper_json["shorthand"] = paper_json["externalIds"]["DOI"]
    elif "ACL" in paper_json["externalIds"]:
        paper_json["shorthand"] = paper_json["externalIds"]["ACL"]

    for key in ["title", "names", "tags", "venue", "shorthand", "link"]:
        paper_json[key] = paper_json[key].replace("\n", " ")

    lab_members_names = {parsed["name"] for parsed in lab_members.values()}
    lab_members_ids = {
        parsed["semantic_scholar_id"]
        for parsed in lab_members.values()
        if "semantic_scholar_id" in parsed
    }

    for author in paper_json["authors"]:
        if author["authorId"] in lab_members_ids or author["name"] in lab_members_names:
            paper_json["author"] = author["name"]
            break

    del (
        paper_json["externalIds"],
        paper_json["paperId"],
        paper_json["url"],
        paper_json["authors"],
    )

    return paper_json


def main(issue_body):
    parsed = parse_issue_body(issue_body)
    paper_json = fetch_content(parsed)
    paper_json = wrangle_fetched_content(parsed, paper_json)  # in-place
    formatted = format_parsed_content(paper_json)
    write_content_to_file(formatted)


if __name__ == "__main__":
    issue_body = os.environ["ISSUE_BODY"]
    main(issue_body)
