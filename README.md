# QQ forward bot

Forward messages from web to QQ group.

Can be used as a anonymous chat forward bot.

Based on pyautogui and pyperclip, so you need a GUI environment to run this.

## Usage

```shell
# first install qq for linux from https://im.qq.com/linuxqq
pip install -r requirements.txt # install dependencies
# you may need to install xclip or xsel (sudo apt install xclip)
python server.py
```

The server is at `http://localhost:8080`.

You can use [frp](https://github.com/fatedier/frp) or deploy it on a VPS with public IP.

### Content format

The content support image with `![](url)` format.

## TODO

- server -> FastAPI/Flask
  - font
  - async support
