# 服务器，提供 /index.html 和 /send 接口

from http.server import BaseHTTPRequestHandler, HTTPServer
from message_sender import MessageSender
from image_handler import ImageHandler
import urllib.parse
import json
import threading

sender = MessageSender()
lock = threading.Lock()

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
        message = json.loads(message)
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

        try:
            content, picture_paths = ImageHandler.handle_content(content)
            message = f"{nickname}: {content}"
            sender.send(message, picture_paths)
            self.send_response(200)
            self.end_headers()
            message = "消息发送成功"
            self.wfile.write(message.encode('utf-8'))
        finally:
            lock.release()


if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8080), RequestHandler)
    print("server started at http://localhost:8080/")
    httpd.serve_forever()
