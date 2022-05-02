import os
from io import StringIO
from textwrap import dedent

import yaml

from . import save_url_image, parse_issue_body


def format_parsed_content(parsed):
    """
    Format the parsed content into a string.
    """
    # First need to add some keys
    parsed["categories"] = "Publications"

    # Then, modify some keys
    parsed["tags"] = [x.strip() for x in parsed["tags"].split(",")]

    # Remove keys and create the front matter
    keys_removed = ["year", "month", "day", "shorthand", "abstract"]
    file_object = StringIO()
    yaml.dump(
        {
            k: v
            for k, v in parsed.items()
            if v != "_No response_" and k not in keys_removed
        },
        file_object,
    )
    front_matter = file_object.getvalue()

    top = dedent(f"---\n{front_matter}\n---\n")

    bottom = dedent(
        """
    *{{ page.names }}*

    **{{ page.venue }}**

    {% include display-publication-links.html pub=page%}

    ## Abstract
    
    """
    )

    return {
        "filename": "-".join([parsed[k] for k in ["year", "month", "day", "shorthand"]])
        + ".md",
        "content": top + bottom + parsed["abstract"],
    }


def write_content_to_file(formatted):
    with open(os.path.join("_posts", "papers", formatted["filename"]), "w") as f:
        f.write(formatted["content"])


if __name__ == "__main__":
    issue_body = os.environ["ISSUE_BODY"]

    parsed = parse_issue_body(issue_body)
    save_url_image(
        fname=parsed["shorthand"],
        profile=parsed,
        key="thumbnail",
        path="assets/images/papers",
    )
    formatted = format_parsed_content(parsed)
    write_content_to_file(formatted)
