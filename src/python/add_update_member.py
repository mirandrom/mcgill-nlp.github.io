import os

from ruamel.yaml import YAML

from . import save_url_image, parse_issue_body


def format_site_label(name):
    if name == "github":
        return "GitHub"
    elif name in ["twitter", "scholar", "website"]:
        return name.title()
    else:
        return name


def format_parsed_content(parsed):
    """
    Format the parsed content into a string.
    """
    parsed["categories"] = "Publications"
    parsed["alumni"] = parsed["status"] == "Alumni"

    parsed["links"] = [
        {"label": format_site_label(key), "url": parsed[key]}
        for key in ["website", "twitter", "github", "scholar"]
        if parsed[key] != "_No response_"
    ]

    keys_removed = ["status", "website", "twitter", "github", "scholar", "action"]

    return {
        k: v
        for k, v in parsed.items()
        if v != "_No response_" and k not in keys_removed
    }


def main(issue_body):
    parsed = parse_issue_body(issue_body)
    profile = format_parsed_content(parsed)

    yaml = YAML()
    authors = yaml.load(open("_data/authors.yml"))
    name_to_username = {authors[username]["name"]: username for username in authors}

    if parsed['action'] == 'Add member':
        if profile["name"] not in authors:
            key = profile["name"]
        else:
            n = 2
            while (k := f'{profile["name"]} {n}') in authors:
                n += 1
            key = k

        save_url_image(fname=key, profile=profile, key="avatar", path="assets/images/bio")

        with open("_data/authors.yml", "a") as f:
            f.write("\n")
            yaml.dump({key: profile}, f)
    else:
        if profile['name'] not in name_to_username:
            raise ValueError(f'{profile["name"]} not in authors')
        
        username = name_to_username[profile['name']]
        authors[username].update(profile)
        
        save_url_image(fname=username, profile=authors[username], key="avatar", path="assets/images/bio")
        
        with open("_data/authors.yml", "w") as f:
            yaml.safe_dump(authors, f, sort_keys=False)


if __name__ == "__main__":
    issue_body = os.environ["ISSUE_BODY"]
    main(issue_body)
