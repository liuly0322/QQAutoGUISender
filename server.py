# 服务器，提供 /index.html 和 /send 接口

from http.server import BaseHTTPRequestHandler, HTTPServer
from message_sender import MessageSender
import urllib.parse
from json import loads
from threading import Lock
import re
import requests
import os

sender = MessageSender()
lock = Lock()
regex = re.compile(r'(?P<full>!\[\]\((?P<url>.*?)\))')

os.makedirs("tmp", exist_ok=True)


def download_image(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
    else:
        print("Error: Unable to download image.")


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/index.html" or self.path == "/":
            with open("index.html", "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        message = post_data.decode('utf-8')
        message = urllib.parse.unquote(message)
        message = loads(message)
        nickname, content, id = message['nickname'], message['content'], message['id']
        if id != 'password':  # password here
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return

        successfully_acquired = lock.acquire(False)
        if not successfully_acquired:
            self.send_response(503)
            self.end_headers()
            message = "等待其他消息发送完成"
            self.wfile.write(message.encode('utf-8'))
            return

        matches = regex.finditer(content)
        if matches:
            picturePaths = []
            for i, match in enumerate(matches):
                pictureURLPath = match.group("url")
                picturePath = os.path.join("tmp", f"{i}")
                download_image(pictureURLPath, picturePath)
                picturePaths += [picturePath]
                content = content.replace(match.group("full"), f"[image: {i}]")
            message = f"{nickname}: {content}"
            sender.send(message, picturePaths)
            self.send_response(200)
            self.end_headers()
            message = "消息发送成功"
            self.wfile.write(message.encode('utf-8'))
        else:
            message = f"{nickname}: {content}"
            sender.send(message)
            self.send_response(200)
            self.end_headers()
            message = "消息发送成功"
            self.wfile.write(message.encode('utf-8'))
        lock.release()


if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8080), RequestHandler)
    print("server started at http://localhost:8080/")
    httpd.serve_forever()
