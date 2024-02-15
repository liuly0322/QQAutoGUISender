<div align="center">
   <img width="160" src="asset/mahiro.png" alt="logo"></br>

# 緒山まひろBot & QQ Auto GUI Sender

Forward anonymous messages from a website to QQ chat (or group) based on pyautogui and pyperclip.

You need a **linux desktop environment** to run this.

</div>

## Usage

### Installation

```shell
# first install qq for linux from https://im.qq.com/linuxqq
# login and open the chat window you want to send
sudo apt install xclip
pip install -r requirements.txt
PASSWORD={{YourPassword}} python server.py
```

The website is now available on `http://localhost:8080`.

### Image

You can send web image with `![](url)` grammar.

### Reply

You can reply to a latest message from `{user}` with `> {user}\n` grammar.