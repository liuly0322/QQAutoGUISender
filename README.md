# QQ forward bot

Forward messages from web to QQ group.

Can be used as a anonymous chat forward bot.

Based on pyautogui and pyperclip, so you need a GUI environment to run this.

## Usage

```shell
# first install qq for linux, for ubuntu you download .deb and install with dpkg
pip install pyautogui
pip install pyperclip # may need apt install xclip first
python server.py
```

Then a web server is opened at `http://localhost:8080`.

You can frp to this server to make it public, or deploy it on a VPS with public IP.

## content format

The content support image with `![](url)` format.