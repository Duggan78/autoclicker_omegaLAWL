import keyboard
import mouse

# TODO: when a key is pressed trigger autoclicker( some type of loop)
# when a different key is break loop.

if keyboard.read_key('p'):
    press_true = 'true'
    if press_true == 'true':
        while press_true == 'true':
            mouse.click('left')
            print("Hello World")
        if keyboard.read_key('o'):
            press_true = 'false'
