import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)


def iscollide(data):
    # Draw rectangle to detect collision with cactus
    for i in range(460, 510):
        for j in range(290, 330):
            if data[i, j] < 100:
                hit('up')
                return True

    # Draw rectangle to detect collision with bird
    for i in range(460, 510):
        for j in range(250, 290):
            if data[i, j] < 100:
                hit('down')
                return True
    return False


if __name__ == '__main__':
    time.sleep(2)
    # hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)

    # # Draw rectangle to detect collision with cactus
    #     for i in range(480, 510):
    #         for j in range(290, 330):
    #             data[i, j] = 0
    #
    # # Draw rectangle to detect collision with bird
    #     for i in range(450, 480):
    #         for j in range(250, 290):
    #             data[i, j] = 171
    #
    #     image.show()
    #     break
