import requests


class MessageSender:

    def __init__(self, url) -> None:
        self.url = url + "/send_group_msg"

    def send(self, group_id, message) -> None:
        post_json = {
            "group_id": group_id,
            "message": message,
        }
        response = requests.post(f"http://{self.url}", json=post_json)
