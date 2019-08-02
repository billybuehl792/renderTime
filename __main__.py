#!python3
#renderTime.py - get render time given img render time

import getRenderTime

def isFloat(val):
    try:
        float(val)
        return True
    except:
        return False

#script start
print(getRenderTime.bcolors.BOLD + 'Enter \'x\' to exit' + getRenderTime.bcolors.ENDC)
quitters = ['x', 'clear', 'exit']

#main loop
while True:
    #get data
    frameRenderTime = input('Frame render time (in seconds): ')
    if frameRenderTime in quitters:
        break
    frameRate = input('Enter frame rate: ')
    if frameRate in quitters:
        break
    
    #ensure data are floats
    if not (isFloat(frameRenderTime) and (isFloat(frameRate))):
        continue

    #get render times
    renderTimes = getRenderTime.getRenderTime(frameRenderTime, frameRate)
    
    #output
    print('1 second video: ' + renderTimes[0])
    print('5 second video: ' + renderTimes[1])
    print('10 second video: ' + renderTimes[2])
    print('30 second video: ' + renderTimes[3])
    print('1 minute video: ' + renderTimes[4])
    print('\n')

print(getRenderTime.bcolors.BLUE + 'Done.' + getRenderTime.bcolors.ENDC)