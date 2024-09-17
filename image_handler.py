import re
import os
import time
from typing import Optional, List
from base64 import b64decode


class ImageHandler:

    @staticmethod
    def replace_image(content: str):
        matches = re.compile(r'(?P<full>!\[\]\((?P<url>.*?)\))').finditer(content)
        if matches:
            for i, match in enumerate(matches):
                picture_url_path = match.group("url")
                content = content.replace(
                    match.group("full"), f"[CQ:image,file={picture_url_path}]"
                )
        return content

    @staticmethod
    def add_user_upload_image(content: str, image: Optional[str]):
        if not image:
            return content

        image = image.split(",")[1]

        content = content + f"[CQ:image,file=base64://{image}]"
        return content
