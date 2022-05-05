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

def merge_links(old_links, new_links):
    new_labels = {link["label"] for link in new_links}
    out_links = [
        link for link in old_links
        if link["label"] not in new_labels
    ]

    out_links.extend(new_links)

    return out_links

def main(issue_body):
    parsed = parse_issue_body(issue_body)
    profile = format_parsed_content(parsed)

    yaml = YAML()
    yaml.preserve_quotes = True
    with open("_data/authors.yml") as f:
        authors = yaml.load(f)
    name_to_username = {authors[username]["name"]: username for username in authors}

    if parsed['action'] == 'Add member':
        if profile["name"] not in authors:
            username = profile["name"]
        else:
            n = 2
            while (k := f'{profile["name"]} {n}') in authors:
                n += 1
            username = k

        authors[username] = profile
    
    else:
        if profile['name'] not in name_to_username:
            raise ValueError(f'{profile["name"]} not in authors')
        
        username = name_to_username[profile['name']]
        profile['links'] = merge_links(authors[username].get('links', []), profile.get('links', []))
        authors[username].update(profile)
    
    save_url_image(fname=username, profile=authors[username], key="avatar", path="assets/images/bio")

    with open("_data/authors.yml", "w") as f:
        yaml.dump(authors, f)

    return authors


if __name__ == "__main__":
    issue_body = os.environ["ISSUE_BODY"]
    main(issue_body)
