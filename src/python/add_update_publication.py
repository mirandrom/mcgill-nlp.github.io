import json
import os
from io import StringIO
from textwrap import dedent

from ruamel.yaml import YAML

from . import save_url_image, parse_issue_body


def front_matters_from_dict(d):
    # Convert to dict
    d = json.loads(json.dumps(d))

    file_object = StringIO()
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.dump(d, file_object)
    front_matter = file_object.getvalue()

    return front_matter


def front_matters_to_dict(front_matter):
    file_object = StringIO(front_matter)
    yaml = YAML()
    yaml.preserve_quotes = True
    d = yaml.load(file_object)
    return d


def get_filename(parsed):
    return "-".join([parsed[k] for k in ["year", "month", "day", "shorthand"]]) + ".md"


def preprocess_parsed(parsed, keys_removed):
    """
    Removes any key with a value of "_No response_" or in `keys_removed`.
    """

    # First need to add some keys
    parsed["categories"] = "Publications"

    # Sanitize some keys
    parsed["shorthand"] = parsed["title"].replace("/", "-").lower()

    # Then, modify some keys
    if parsed["tags"] != "_No response_":
        parsed["tags"] = [x.strip() for x in parsed["tags"].split(",")]

    if parsed["abstract"] == "_No response_":
        parsed["abstract"] = "_Unavailable_"

    # Then, remove keys
    return {
        k: v
        for k, v in parsed.items()
        if v != "_No response_" and k not in keys_removed
    }


def generate_publication_post(parsed):
    """
    Format the parsed content into a string.
    """

    d = preprocess_parsed(
        parsed, keys_removed=["year", "month", "day", "shorthand", "abstract", "action"]
    )

    front_matter = front_matters_from_dict(d)
    top = dedent(f"---\n{front_matter}\n---\n")

    bottom = dedent(
        """
    *{{ page.names }}*

    **{{ page.venue }}**

    {% include display-publication-links.html pub=page %}

    ## Abstract
    
    """
    )

    return {
        "filename": get_filename(parsed),
        "content": top + bottom + parsed.get("abstract", ""),
    }


def update_publication_post(parsed):
    new_data = preprocess_parsed(
        parsed, keys_removed=["year", "month", "day", "shorthand", "abstract", "action"]
    )

    filename = get_filename(parsed)

    with open(os.path.join("_posts", "papers", filename), "r") as f:
        lines = f.read()

    _, front_matter, bottom = lines.split("---", 2)

    old_data = front_matters_to_dict(front_matter)
    old_data.update(new_data)

    front_matter = front_matters_from_dict(old_data)
    top = f"---\n{front_matter}\n---\n"

    return {
        "filename": filename,
        "content": top + bottom,
    }


def write_content_to_file(formatted):
    with open(os.path.join("_posts", "papers", formatted["filename"]), "w") as f:
        f.write(formatted["content"])


def main(issue_body):
    parsed = parse_issue_body(issue_body)
    save_url_image(
        fname=parsed["shorthand"],
        profile=parsed,
        key="thumbnail",
        path="assets/images/papers",
    )
    if parsed["action"] == "Add publication":
        formatted = generate_publication_post(parsed)
    else:
        formatted = update_publication_post(parsed)
    write_content_to_file(formatted)

    return formatted


if __name__ == "__main__":
    issue_body = os.environ["ISSUE_BODY"]
    main(issue_body)
