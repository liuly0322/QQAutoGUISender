from flask import Flask, request, send_from_directory
from message_sender import MessageSender
from image_handler import ImageHandler
from reply_handler import ReplyHandler
import threading
import os

app = Flask(__name__)
sender = MessageSender()
replyer = ReplyHandler()
lock = threading.Lock()
password = os.environ.get('PASSWORD')

@app.route('/<path:path>', methods=['POST'])
def post_message(path):
    data = request.json
    nickname, content, id = data.get('nickname'), data.get('content'), data.get('id')
    if id != password:
        return "验证未通过喵", 404

    successfully_acquired = lock.acquire(False)
    if not successfully_acquired:
        return "有其他消息正在发送", 503

    try:
        content, picture_paths = ImageHandler.replace_image(content)
        content = replyer.replace_reply(content)

        message = nickname + ": "
        if "\n" in content:
            message += "\n"
        message += content

        sender.send(message, picture_paths)

        replyer.add_history(nickname, message)
    except Exception as e:
        lock.release()
        return f"消息发送失败: {e}", 500

    lock.release()
    return "消息发送成功", 200

@app.route('/')
def index():
    return send_from_directory('asset', 'index.html')
    

@app.route('/<path:filename>')
def asset(filename):
    return send_from_directory('asset', filename)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
