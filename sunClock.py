from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from time import sleep
from datetime import datetime
import math

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
print ("Matrix initialized\n")
angle = 90
pi = 3.14159265

while (True):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    #set the position of sun path
    cenX = 64 * 0.5
    cenY = 32 * 1.5 
    sunPath = 32
    sunRad = 10
    
    
    #draw past pixel on path and turn it off
    pX = cenX + math.cos(angle) * sunPath
    pY = cenY + math.sin(angle) * sunPath
    #matrix.SetPixel(pX, pY,0,255,0)
    #sleep(0.1)
    #matrix.SetPixel(pX, pY,0,0,0)
    #move the sun
    angle += 0.01
    #draw current pixel on path
    cX = cenX + math.cos(angle) * sunPath
    cY = cenY + math.sin(angle) * sunPath
    matrix.SetPixel(cX, cY,255,0,0)

    print(cX," ",cY)
    print("running pixels")


    for j in range(0, 64):
        for i in range (0,32):
            distance = math.sqrt( ((cX-j)**2)+((cY-i)**2))
            if(distance < sunRad):
                matrix.SetPixel(j,i,255,255,255)
            else:
                matrix.SetPixel(j,i,0,0,0)

    sleep(.1)
