import pyautogui
import time

tg = int(input('Thoi gian cho (s): '))
delay = int(input('So lan spam: '))
cau = str(input('Cau spam: '))
te = int(input('Thoi gian cho moi lan spam (s): '))

time.sleep(tg)
for i in range(0, delay):
    time.sleep(te/60)
    pyautogui.typewrite(cau)
    pyautogui.press('enter')

