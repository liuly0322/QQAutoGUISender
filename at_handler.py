import re

class AtHandler:
    @staticmethod
    def replace_at(content: str):
        matches = re.compile(r'(?P<full>@(?P<number>\d+))').finditer(content)
        at_numbers = []
        if matches:
            for i, match in enumerate(matches):
                at_number = match.group("number")
                at_numbers += [at_number]
                content = content.replace(match.group("full"), f"[at: {i}]")
        return content, at_numbers