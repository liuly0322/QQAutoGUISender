import re
import os
import requests

os.makedirs("tmp", exist_ok=True)

class ImageHandler:
    @staticmethod
    def download_image(url, filename):
        response = requests.get(url, stream=True, timeout=(4, 4))
        if response.status_code != 200 or \
            not response.headers['Content-Type'].startswith('image') or \
            int(response.headers['Content-Length']) > 50 * 1024 * 1024:
            return False

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        return True

    @staticmethod
    def handle_content(content: str):
        matches = re.compile(r'(?P<full>!\[\]\((?P<url>.*?)\))').finditer(content)
        picture_paths = []
        if matches:
            for i, match in enumerate(matches):
                picture_url_path = match.group("url")
                picture_path = os.path.join("tmp", f"{i}")
                if ImageHandler.download_image(picture_url_path, picture_path):
                    picture_paths += [picture_path]
                    content = content.replace(match.group("full"), f"[image: {i}]")
        return content, picture_paths

