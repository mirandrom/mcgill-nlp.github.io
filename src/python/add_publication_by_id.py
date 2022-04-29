import os
import json
from urllib.request import urlopen

import yaml

from .add_publication import parse_issue_body, format_parsed_content, write_content_to_file



def fetch_content(di):
    lab_members = yaml.safe_load(open("_data/authors.yml"))

    method = di["method"]
    identifier = di["identifier"]
    month = di["month"]
    day = di["day"]
        
    url = urlopen(
        f"https://api.semanticscholar.org/graph/v1/paper/{method}:{identifier}?fields=title,venue,year,authors.name,externalIds,url,abstract"
    )
    data = json.loads(url.read())

    author_names = [di['name'] for di in data['authors']]
    data['names'] = ", ".join(author_names).replace("\n", " ")
    data['tags'] = data['venue']
    data['venue'] = f"{data['venue']} {data['year']}"
    data['shorthand'] = str(data['paperId'])
    data['year'] = str(data['year'])
    data['month'] = month
    data['day'] = day
    data['link'] = data['url']

    if 'ArXiv' in data['externalIds']:
        data['link'] = f"https://arxiv.org/abs/{data['externalIds']['ArXiv']}"
        data['shorthand'] = data['externalIds']['ArXiv']

    lab_members_names = {di['name'] for di in lab_members.values()}
    lab_members_ids = {di['semantic_scholar_id'] for di in lab_members.values() if 'semantic_scholar_id' in di}

    for author in data['authors']:
        if author['authorId'] in lab_members_ids or author['name'] in lab_members_names:
            data['author'] = author['name']
            break

    del data['externalIds'], data['paperId'], data['url']

    return data

if __name__ == "__main__":
    issue_body = os.environ['ISSUE_BODY']

    parsed = parse_issue_body(issue_body)
    fetched = fetch_content(parsed)
    formatted = format_parsed_content(fetched)
    write_content_to_file(formatted)


