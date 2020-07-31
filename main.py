import keyboard
import mouse

# TODO: when a key is pressed trigger autoclicker( some type of loop)
# when a different key is break loop.

clicks = 0

if keyboard.read_key('p'):
    press_true = 'true'
    if press_true == 'true':
        while press_true == 'true' and clicks <= 100:
            mouse.click('left')
            clicks = clicks + 1
            print(int(clicks))

