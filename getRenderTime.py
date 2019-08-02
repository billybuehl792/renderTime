#!python3
#getRenderTime.py - calculate render time given frame render time

class bcolors:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

def getRenderTime(frameRenderTime, frameRate):
    renderTimes = []
    increments = [1, 5, 10, 30, 60]

    for increment in increments:
        #value in seconds
        renderTime = (float(frameRenderTime) * float(frameRate)) * increment

        #value in hours
        if renderTime > 3600:
            renderTime = (renderTime/60) / 60
            if renderTime > 7:
                renderTimes.append(bcolors.RED + str(round(renderTime, 2)) + bcolors.ENDC + 'h')
            else:
                renderTimes.append(bcolors.YELLOW + str(round(renderTime, 2)) + bcolors.ENDC + 'h')
        
        #value in minutes
        elif renderTime > 60:
            renderTime = renderTime/60
            renderTimes.append(bcolors.GREEN + str(round(renderTime, 2)) + bcolors.ENDC + 'm')

    return renderTimes