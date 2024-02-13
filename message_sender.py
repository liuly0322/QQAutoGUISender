import pyautogui
import pyperclip
import time
import subprocess


class MessageSender:
    def __init__(self) -> None:
        text_box_position = pyautogui.locateOnScreen('asset/text_box.png')
        if not text_box_position:
            print("无法找到文本框")
            exit(1)
        self.text_box_x, self.text_box_y = pyautogui.center(text_box_position)

    def send(self, message, picture_paths=None) -> None:
        pyperclip.copy(message)
        time.sleep(1)
        pyautogui.click(self.text_box_x, self.text_box_y)
        pyautogui.hotkey('ctrl', 'v')
        if picture_paths:
            for picture_path in picture_paths:
                subprocess.run(
                    ["xclip", "-selection", "clipboard", "-t", "image/png", "-i", f"{picture_path}"]
                )
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)
        pyautogui.press('enter')


if __name__ == "__main__":
    sender = MessageSender()
    sender.send("hello!")
    sender.send("hello.png: ", ["asset/hello.png", "asset/hello.png"])
    sender.send("这里是自动发送的消息。")
