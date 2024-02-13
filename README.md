# QQ Auto GUI Sender

Forward anonymous messages from a website to QQ based on pyautogui and pyperclip.

You need a desktop environment to run this.

## Usage

```shell
# first install qq for linux from https://im.qq.com/linuxqq
sudo apt install xclip
pip install -r requirements.txt
python server.py
```

The server is now running on `http://localhost:8080`.

## deploy

You can deploy it on a VPS with public IP or use [frp](https://github.com/fatedier/frp) to make it public.

### Content format

The content support image with `![](url)` format.
