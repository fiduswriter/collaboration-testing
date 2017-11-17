from xdo import Xdo
from time import sleep
from loremipsum import get_sentences
from random import randint
xdo = Xdo()
sleep(5)
win_id = xdo.get_focused_window()
while True:
    texts = get_sentences(randint(1,5))
    speed = randint(50000, 1000000)
    for text in texts:
        xdo.enter_text_window(win_id, text, speed)
    xdo.send_keysequence_window(win_id, "Return")
