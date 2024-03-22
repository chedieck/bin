import pyautogui as pag
import math
import random
import os

PID = os.getpid()
with open(f"/tmp/mousefuck.{PID}.pid", "w") as f:
    f.write(str(PID))

pag.PAUSE = 0.005
wid, hei = pag.size()

def circle():
    midwid, midhei = (wid // 2, hei // 2)
    R = min([midwid, midhei]) // 2
    quarter = round(math.sqrt(2) * R)

    while 1:
        for q in range(4 * quarter):
            x = midwid + round(quarter * math.cos(math.pi * q/(2 * quarter)))
            y = midhei + round(quarter * math.sin(math.pi * q/(2 * quarter)))
            pag.moveTo(x,y)


def cluster(spread=10):
    while 1:
        x, y = pag.position()
        mx, my = [spread * random.gauss(0, 1) for _ in range(2)]
        pag.moveTo(x + mx, y + my)




def strip():
    while 1:
        _, y = pag.position()
        x = random.randint(0, wid - 1)
        pag.moveTo(x, y)


if __name__ == '__main__':
    f = random.choice([circle, cluster, strip])
    f()



cluster()
