import os
import json
from urllib.request import urlopen

import yaml

from . import parse_issue_body
from .add_publication import format_parsed_content, write_content_to_file
from .add_publication_by_id import wrangle_fetched_content

def fetch_content(parsed):

    url = urlopen(
        f"https://api.semanticscholar.org/graph/v1/author/{parsed['author_id']}?fields=papers.title,papers.venue,papers.year,papers.authors,papers.externalIds,papers.url,papers.abstract,papers.externalIds"
    )
    data = json.loads(url.read())

    return data

def main(issue_body):
    ignored_ids = set(json.loads(open("ignored/semantic_scholar_paper_ids.json").read()))
    parsed = parse_issue_body(issue_body)
    fetched = fetch_content(parsed)

    for paper_json in fetched['papers']:
        start = int(parsed['start'])
        end = int(parsed['end'])
        year = int(paper_json['year'])

        if year >= start and year <= end and paper_json['paperId'] not in ignored_ids:
            ignored_ids.add(paper_json['paperId'])
            paper_json = wrangle_fetched_content(parsed, paper_json) # in-place
            formatted = format_parsed_content(paper_json)
            write_content_to_file(formatted)
        
    with open("ignored/semantic_scholar_paper_ids.json", "w") as f:
        json.dump(list(ignored_ids), f, indent=2)

if __name__ == '__main__':
    issue_body = os.environ['ISSUE_BODY']
