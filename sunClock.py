from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from time import sleep
from datetime import datetime, timedelta
import datetime as dt
import math
import sys

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.cols = 64
options.disable_hardware_pulsing = 0
options.gpio_slowdown = 3
options.brightness = 100
options.pwm_bits = 11
options.hardware_mapping="adafruit-hat"


matrix = RGBMatrix(options = options)
print ("Matrix initialized")

#converting strings into sunrise time object
myString1 = sys.argv[1].replace('"','')
mySunRise = myString1.split(':')
tRh = int(mySunRise[0])
tRm = int(mySunRise[1])
tRs = int(mySunRise[2])
tR = dt.time(tRh, tRm, tRs)
#converting strings into sunset time object
myString2 = sys.argv[2].replace('"','')
mySunSet = myString2.split(':')
tSh = int(mySunSet[0])
tSm = int(mySunSet[1])
tSs = int(mySunSet[2])
tS = dt.time(tSh, tSm, tSs)

#manual input sunrise time
#tR = dt.time(7,9,14)
#manual input sunset time
#tS = dt.time(16,28,23)

#now
tN = dt.time(4,30,30)#datetime.now()
#sum of time
tRS = tR.hour * 3600 + tR.minute * 60 + tR.second 
tSS = tS.hour * 3600 + tS.minute * 60 + tS.second 
tNS = tN.hour * 3600 + tN.minute * 60 + tN.second 


angle = -2.67794872
pi = 3.14159265
sunMoveRate = 2 * pi / 86400
totalSunTime = tSS - tRS
currnetSunTime = tNS - tRS
currentSunLoc = currnetSunTime / totalSunTime
print(currentSunLoc)

cenX = 64 * 0.5
cenY = 32 * 1.5 
sunRad = 8
sunPath = 35
totalSunPathAngle = 2.21429744
sunAngle = currentSunLoc * totalSunPathAngle

print(sunAngle)
curAngle = angle + sunAngle
while (True):
    now = datetime.now()
    #print(now)
    current_time = now.strftime("%H:%M:%S")
    #print("Current Time =", current_time)

    #set the position of sun path
    
    #draw past pixel on path and turn it off
    pX = cenX + math.cos(curAngle) * sunPath
    pY = cenY + math.sin(curAngle) * sunPath
    #matrix.SetPixel(pX, pY,0,255,0)
    #sleep(0.1)
    #matrix.SetPixel(pX, pY,0,0,0)

    #move the sun
    curAngle += .05
    #draw current pixel on path
    cX = cenX + math.cos(curAngle) * sunPath
    cY = cenY + math.sin(curAngle) * sunPath
    matrix.SetPixel(cX, cY,255,0,0)

    #print(cX," ",cY)
    #print("running pixels")

    distanceFromMiddle = math.sqrt(((cX-32)**2) + ((cY-20)**2))
    print(distanceFromMiddle)

    for j in range(0, 64):
        for i in range (0,32):
            distance = math.sqrt( ((cX-j)**2)+((cY-i)**2))
            if(distance < sunRad+distanceFromMiddle*.1):
                matrix.SetPixel(j,i,255,255,255)
            else:
                matrix.SetPixel(j,i,0,0,0)

    sleep(.1)




