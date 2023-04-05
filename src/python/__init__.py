import os
from urllib.request import urlopen, urlretrieve

from PIL import Image


def center_square_crop(im):
    # Do a center crop
    width, height = im.size
    if width > height:
        left = (width - height) / 2
        right = left + height
        top = 0
        bottom = height
    else:
        left = 0
        right = width
        top = (height - width) / 2
        bottom = top + width
    im = im.crop((left, top, right, bottom))

    return im


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text  # or whatever


def parse_issue_body(body):
    """
    Parse the body of the issue and return a dictionary of the parsed data.
    """
    parsed = {}
    k = None

    for line in body.split("\n"):
        if line.startswith("###"):
            k = remove_prefix(line, prefix="###").strip().lower().replace(" ", "_")
            parsed[k] = ""
        else:
            if k is not None:
                parsed[k] += line.strip()

    return parsed


def save_url_image(
    fname,
    profile,
    key,
    image_dir,
    size=(400, 400),
    crop_center=False,
    png_to_jpg=False,
    jpg_quality=80,
):
    if key in profile and profile[key].startswith("http"):
        url = profile[key]
        # Get the extension of the file
        ext = os.path.splitext(url)[1][1:]
        if ext == "jpeg":
            ext = "jpg"

        if ext == "":
            raise Exception(f"Could not get extension from {url}")

        # Download the image
        file_path = os.path.join(image_dir, f"{fname}.{ext}")

        os.makedirs(image_dir, exist_ok=True)
        urlretrieve(url, file_path)

        if ext in ["svg", "gif"]:
            return "/" + file_path
        else:
            im = Image.open(file_path)
            if crop_center:
                im = center_square_crop(im)
            im.thumbnail(size)

            if ext == "jpg":
                im.save(file_path, quality=jpg_quality)
            elif ext == "png" and png_to_jpg:
                im = im.convert("RGB")
                file_path = file_path.replace(".png", ".jpg")
                im.save(file_path, quality=jpg_quality)
            else:
                im.save(file_path)

            return "/" + file_path


def write_content_to_file(formatted, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    with open(os.path.join(save_dir, formatted["filename"]), "w") as f:
        f.write(formatted["content"])


def remove_items_with_values(dictionary, value):
    return {k: v for k, v in dictionary.items() if v != value}


def remove_keys(dictionary, keys_to_remove):
    keys_to_remove = set(keys_to_remove)

    return {k: v for k, v in dictionary.items() if k not in keys_to_remove}
