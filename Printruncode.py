#to send a file of gcode to the printer
from multiprocessing import Process
from printrun.printcore import printcore
from printrun import gcoder
import serial 
import time
from gpiozero import LED
p=printcore('/dev/ttyUSB0', 115200) # or p.printcore('COM3',115200) on Windows
led = LED(12)
#gcode=[i.strip() for i in open('filename.gcode')] # or pass in your own array of gcode lines instead of reading from a file
#gcode = gcoder.LightGCode(gcode)
# startprint silently exits if not connected yet 
 

def Lightingmicroscopebottom():
       while True:         
          led.on() 
def gcoderunner(p): 
    print("running g_code")
    while not p.online:
       time.sleep(0.1) 
    p.send_now("M302 P0") # this will send M105 immediately, ahead of the rest of the print
    p.send_now("M302 S0")
    p.send_now("M106 S190")
    p.send_now("G0 X280 Y650 Z50 E20") # Y max 820
    p.send_now("G0 X0 Y0 Z0 E0")
    led.off()
    #p.send_now("M106 S0")
    p.pause() # use these to pause/resume the current print
    p.resume()
    p.disconnect() # this is how you disconnect from the printer once you are done. This will also stop running prints.
    
if __name__ == '__main__':         
        g = Process(target=gcoderunner(p))
        j = Process(target=Lightingmicroscopebottom) 
        g.start() 
        g.join() 
        j.start() 
        g.join()
          
