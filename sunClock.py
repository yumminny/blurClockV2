from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from time import sleep
from datetime import datetime, timedelta
import datetime as dt
import math
import sys

for arg in sys.argv:
    print(arg)

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.cols = 64
options.disable_hardware_pulsing = 0
options.gpio_slowdown = 4
options.brightness = 100
options.pwm_bits = 11
options.hardware_mapping="adafruit-hat"


matrix = RGBMatrix(options = options)
print ("Matrix initialized")
#starting point


#sunrise time
tR = dt.time(7,23,14)
#sunset time
tS = dt.time(17,31,23)
#now
tN = datetime.now()
#tN = dt.time(14,23,24)
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
sunRad = 10
sunPath = 32
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
    angle += sunMoveRate
    #draw current pixel on path
    cX = cenX + math.cos(curAngle) * sunPath
    cY = cenY + math.sin(curAngle) * sunPath
    matrix.SetPixel(cX, cY,255,0,0)

    #print(cX," ",cY)
    #print("running pixels")


    for j in range(0, 64):
        for i in range (0,32):
            distance = math.sqrt( ((cX-j)**2)+((cY-i)**2))
            if(distance < sunRad):
                matrix.SetPixel(j,i,255,255,255)
            else:
                matrix.SetPixel(j,i,0,0,0)

    sleep(.1)
