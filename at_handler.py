import re

class AtHandler:
    @staticmethod
    def replace_at(content: str):
        matches = re.compile(r'(?P<full>@(?P<number>\d+))').finditer(content)
        if matches:
            for i, match in enumerate(matches):
                at_number = match.group("number")
                content = content.replace(match.group("full"), f"[CQ:at,qq={at_number}]")
        return content
