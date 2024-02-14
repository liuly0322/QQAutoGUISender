import re
import os
import time
import requests

os.makedirs("tmp", exist_ok=True)

class ImageHandler:
    @staticmethod
    def download_image(url, filename):
        response = requests.get(url, stream=True, timeout=(4, 4))
        if response.status_code != 200:
            raise ValueError(f"下载失败喵: {response.status_code}")

        size = 0
        maximum_size = 1024 * 1024 * 50
        start = time.time()
        receive_timeout = 20

        def write_chunk(file, chunk):
            nonlocal size
            size += len(chunk)
            if size > maximum_size:
                raise ValueError("图片太大了喵")

            if time.time() - start > receive_timeout:
                raise TimeoutError("下载超时喵")

            file.write(chunk)

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                write_chunk(file, chunk)

    @staticmethod
    def handle_content(content: str):
        matches = re.compile(r'(?P<full>!\[\]\((?P<url>.*?)\))').finditer(content)
        picture_paths = []
        if matches:
            for i, match in enumerate(matches):
                picture_url_path = match.group("url")
                picture_path = os.path.join("tmp", f"{i}")
                ImageHandler.download_image(picture_url_path, picture_path)
                picture_paths += [picture_path]
                content = content.replace(match.group("full"), f"[image: {i}]")
        return content, picture_paths

