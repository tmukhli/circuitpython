# Write your code here :-)
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.3



while True:
    print("Make it yellow!")
    dot.fill((255,255,0))
    time.sleep(1)

    print("Make it blue!")
    dot.fill((0,0,255))
    time.sleep(1)