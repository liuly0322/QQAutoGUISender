<div align="center">
   <img width="160" src="asset/mahiro.png" alt="logo"></br>

# 緒山まひろBot & QQ Auto GUI Sender

Forward anonymous messages from a website to QQ groups based on **onebot-11 protocol**.

</div>

> [!NOTE]  
> There is also a **pyautogui** based implementation in `pyautogui` branch, that's why it is titled "Auto GUI Sender". This way requires a Linux desktop environment.

## Usage

### Installation

1. install any protocol implementation like [NapCatQQ](https://github.com/NapNeko/NapCatQQ). It is not recommended to use the "headless launch" method, as it is more likely to be forced offline and offers less stability. Set up the configuration to **enable the HTTP service**, then log in to activate the server port as `HTTP_PORT` which will be used in `.env` configuration.
2. install dependencies
   ```shell
   pip install -r requirements.txt
   ```
3. edit `sample.env` and rename it to `.env`
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
