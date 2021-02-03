#! python3
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    sumValueX = 5
    sumValueY = 5
    while True:
        x, y = pyautogui.position()
        
        if x < 10 or x > 1910:
            sumValueX *= -1

        if y < 10 or y > 1070:
            sumValueY *= -1

        x += sumValueX
        y += sumValueY

        pyautogui.moveTo(x, y)

        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        
except KeyboardInterrupt:
    print('\n')