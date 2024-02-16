<div align="center">
   <img width="160" src="asset/mahiro.png" alt="logo"></br>

# 緒山まひろBot & QQ Auto GUI Sender

Forward anonymous messages from a website to QQ groups based on pyautogui and pyperclip.

You need a **linux desktop environment** to run this.

</div>

## Usage

### Installation

1. install [linuxqq](https://im.qq.com/linuxqq), login and open a chat window.
2. install dependencies
   ```shell
   sudo apt install xclip
   pip install -r requirements.txt
   ```
3. edit `sample.env` to config allow-groups and rename it to `.env`
4. start the server
   ```shell
   python server.py
   ```

The website is now running on `http://localhost:8080`.

### Support Commands

- `![](url)`: Send a image from url.
- `@{qq_number}`: Mention a QQ user.
- `> {user}\n`: Reply to a latest message from (anonymous) `{user}`.

`\n` above means you need to start a new line after the command.