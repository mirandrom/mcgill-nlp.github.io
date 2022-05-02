import os
import json
from urllib.request import urlopen

import yaml

from . import parse_issue_body
from .add_publication import format_parsed_content, write_content_to_file
from .add_publication_by_id import wrangle_fetched_content

issue_body = """
### Start

2020

### End

2020

### Author ID

145732771
"""

parsed = parse_issue_body(issue_body)

url = urlopen(
    f"https://api.semanticscholar.org/graph/v1/author/{parsed['author_id']}?fields=papers.title,papers.venue,papers.year,papers.authors,papers.externalIds,papers.url,papers.abstract,papers.externalIds"
)
data = json.loads(url.read())

for paper_json in data['papers']:
    start = int(parsed['start'])
    end = int(parsed['end'])
    year = int(paper_json['year'])

    if year >= start and year <= end:
        paper_json = wrangle_fetched_content(parsed, paper_json) # in-place
        formatted = format_parsed_content(paper_json)
        write_content_to_file(formatted)