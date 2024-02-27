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

        search_box_position = pyautogui.locateOnScreen('asset/search_box.png')
        if not search_box_position:
            print("无法找到搜索框")
            exit(1)
        self.search_box_x, self.search_box_y = pyautogui.center(search_box_position)

        self.current_group_id = None

    def switch_group(self, group_id) -> None:
        if group_id == self.current_group_id:
            return

        pyautogui.click(self.search_box_x, self.search_box_y)
        time.sleep(0.1)
        pyperclip.copy(group_id)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(0.1)

        self.current_group_id = group_id

    def send(self, group_id, message, picture_paths=None, at_numbers=None) -> None:
        self.switch_group(group_id)
        pyautogui.click(self.text_box_x, self.text_box_y)

        pyperclip.copy(message)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')

        for picture_path in picture_paths or []:
            subprocess.run(
                ["xclip", "-selection", "clipboard", "-t", "image/png", "-i", f"{picture_path}"]
            )
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)

        for at_number in at_numbers or []:
            pyautogui.write(f"@{at_number}")
            pyautogui.press('enter')
            time.sleep(1)

        pyautogui.press(['esc', 'enter'])


if __name__ == "__main__":
    sender = MessageSender()
    sender.send("hello!")
    sender.send("hello.png: ", ["asset/hello.png", "asset/hello.png"])
    sender.send("这里是自动发送的消息。")
