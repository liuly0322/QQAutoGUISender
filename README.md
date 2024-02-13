# QQ forward bot

Forward messages from web to QQ group.

Can be used as a anonymous chat forward bot.

Based on pyautogui and pyperclip, so you need a GUI environment to run this.

## Usage

```shell
# first install qq for linux from https://im.qq.com/linuxqq
sudo apt install xclip
pip install -r requirements.txt
python server.py
```

The server is at `http://localhost:8080`.

You can use [frp](https://github.com/fatedier/frp) or deploy it on a VPS with public IP.

### Content format

The content support image with `![](url)` format.
