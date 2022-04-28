import urllib.request

def save_url_image(fname, profile, key, path):
    if key in profile and profile[key].startswith("http"):
        ext = profile[key].split(".")[-1]
        file_path = f"{path}/{fname}.{ext}"
        urllib.request.urlretrieve(profile[key], file_path)
        profile[key] = "/" + file_path