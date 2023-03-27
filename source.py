import time
import pyautogui as pgui

# Google Chromeへ移動する
def go_page() -> None:
    pgui.keyDown('alt')
    pgui.press('tab')
    pgui.keyUp('alt')

# 指定した画像をクリックする
def click_image(image_path: str) -> tuple:

    try:
        locate : tuple = pgui.locateOnScreen(image_path, grayscale=True, confidence=0.7)
        pgui.click(locate, duration=0.5)
        return locate

    except pgui.ImageNotFoundException:
        pgui.alert(text='画像が見つかりません', title='エラー', button='OK')

# main
def main():

        # 価格を一桁減らす
        click_image('./image/syouhinnnohensyuu.png')
        time.sleep(5)

        pgui.press('end')
        time.sleep(2)

        # 価格を一桁増やす
        click_image('./image/hanbaikakaku.png')
        pgui.press('end')
        pgui.write('0')
        pgui.press('enter')
        time.sleep(3)

        click_image('./image/syouhinnnohensyuu.png')
        time.sleep(5)

        pgui.press('end')
        time.sleep(2)

        click_image('./image/hanbaikakaku.png')
        pgui.press('end')
        pgui.press('backspace')
        pgui.press('enter')
        time.sleep(3)

        pgui.hotkey('ctrl', 'w')

if __name__ == '__main__':

    page_count = input('実施件数を入力してください >>> ')
    go_page()

    for _ in range(int(page_count)):
        main()