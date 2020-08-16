#! python3
# stopWatch.py - A simple stopwatch program.

import time, pyperclip, pprint

def stopWatch():

    # Display the program's instructions.

    print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press CTRL-C')
    input()
    print('Started...')
    startTime = time.time()
    lastTime = startTime
    lapNum = 1
    content = []
    # Start tracking the lap times.

    while True:
        try:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            print('Lap %s'.ljust(8 - len(str(lapNum)),' ') % (lapNum) + ': ' + '%s('.rjust(9 - len(str(lapTime)),' ') % (lapTime) + '%s)'.rjust(8 - len(str(totalTime)),' ') % (totalTime),end='')
            content.append(str('Lap %s'.ljust(8 - len(str(lapNum)),' ') % (lapNum) + ': ' + '%s('.rjust(9 - len(str(lapTime)),' ') % (lapTime) + '%s)'.rjust(8 - len(str(totalTime)),' ') % (totalTime)))
            lapNum += 1
            lastTime = time.time()
        except KeyboardInterrupt:
            print('\nDone')
            break
    print(content)
    pyperclip.copy(pprint.pformat(content))

stopWatch()

