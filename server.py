# 服务器，提供 /index.html 和 /send 接口

from http.server import BaseHTTPRequestHandler, HTTPServer
from message_sender import MessageSender
import urllib.parse
from json import loads
from threading import Lock

sender = MessageSender()
lock = Lock()

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
        if id != 'password': # password here
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return

        message = f"{nickname}: {content}"

        successfully_acquired = lock.acquire(False)
        if not successfully_acquired:
            self.send_response(503)
            self.end_headers()
            message = "等待其他消息发送完成"
            self.wfile.write(message.encode('utf-8'))
            return
        
        sender.send(message)
        self.send_response(200)
        self.end_headers()
        message = "消息发送成功"
        self.wfile.write(message.encode('utf-8'))
        lock.release()

if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8080), RequestHandler)
    httpd.serve_forever()
