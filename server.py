from flask import Flask, request, send_from_directory
from message_sender import MessageSender
from image_handler import ImageHandler
from at_handler import AtHandler
from reply_handler import ReplyHandler
from dotenv import load_dotenv
import threading
import os

load_dotenv(".env")
WHITELIST_GROUPS = os.getenv("WHITELIST_GROUPS").split(",")

app = Flask(__name__)
sender = MessageSender(os.getenv("HTTP_PORT"))
replyer = ReplyHandler()
lock = threading.Lock()

@app.route('/<path:path>', methods=['POST'])
def post_message(path):
    data = request.json
    nickname, content, group_id = data.get('nickname'), data.get('content'), data.get('id')
    image = data.get('image')

    if group_id not in WHITELIST_GROUPS:
        return "验证未通过喵", 404

    successfully_acquired = lock.acquire(False)
    if not successfully_acquired:
        return "有其他消息正在发送", 503

    try:
        content = ImageHandler.replace_image(content)
        content = ImageHandler.add_user_upload_image(content, image)
        content = AtHandler.replace_at(content)
        content = replyer.replace_reply(content)

        message = nickname + ": "
        if "\n" in content:
            message += "\n"
        message += content

        sender.send(group_id, message)

        replyer.add_history(nickname, message)
    except Exception as e:
        lock.release()
        return f"消息发送失败: {e}", 500

    lock.release()
    return "消息发送成功", 200

@app.route('/')
def index():
    return send_from_directory('asset', 'index.html', max_age=86400)


@app.route('/<path:filename>')
def asset(filename):
    return send_from_directory('asset', filename, max_age=86400)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
