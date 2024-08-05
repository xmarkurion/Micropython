import sh1107
import machine
import time
import sys
import framebuf
import array
import images.kaktus as img
import framebuf

import machine
import sh1107

class Bar:
    def __init__(self,display):
        self.display = display
        
    def main(self,value):
        if value > 0 or value < 100:
            self.show(value)
        
        if value > 80:
            self.h_100()
        elif value > 70:
            self.h_70()
        elif value > 40:
            self.h_40()
        elif value > 20:
            self.h_20()
        elif value > 10:
            self.h_10()
        elif value > 1:
            self.h_5()
        else:
            self.empty()
        
    def show(self,value):
        self.display.rect(107,10, 20, 100, 1)
        screen_down = int( self.translate(value,0,100,107,12) )
        bar_down = int( self.translate(value,0,100,1,96) )
        self.display.fill_rect(109,screen_down,16,bar_down,1) 
        self.display.text(f"{value:>3}%", 95, 115, 1)
        
    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin
        valueScaled = float(value - leftMin) / float(leftSpan)
        return rightMin + (valueScaled * rightSpan)
    
    def empty(self):
        buffer = bytearray(img.humid_unknown)
        fb = framebuf.FrameBuffer(buffer, 63, 117, framebuf.MONO_HLSB)
        self.display.blit(fb,20,10)
        
    def h_5(self):
        buffer = bytearray(img.humid_5)
        fb = framebuf.FrameBuffer(buffer, 63, 117, framebuf.MONO_HLSB)
        self.display.blit(fb,20,10)
        
    def h_10(self):
        buffer = bytearray(img.humid_10)
        fb = framebuf.FrameBuffer(buffer, 63, 117, framebuf.MONO_HLSB)
        self.display.blit(fb,20,10)
        
    def h_20(self):
        buffer = bytearray(img.humid_20)
        fb = framebuf.FrameBuffer(buffer, 63, 117, framebuf.MONO_HLSB)
        self.display.blit(fb,20,10)
        
    def h_40(self):
        buffer = bytearray(img.humid_40)
        fb = framebuf.FrameBuffer(buffer, 63, 117, framebuf.MONO_HLSB)
        self.display.blit(fb,20,10)
        
    def h_70(self):
        buffer = bytearray(img.humid_70)
        fb = framebuf.FrameBuffer(buffer, 63, 117, framebuf.MONO_HLSB)
        self.display.blit(fb,20,10)
        
    def h_100(self):
        buffer = bytearray(img.humid_100)
        fb = framebuf.FrameBuffer(buffer, 63, 117, framebuf.MONO_HLSB)
        self.display.blit(fb,20,10)
    
if __name__ == "__main__":
    sdaPIN=machine.Pin(8)
    sclPIN=machine.Pin(9)
    i2c=machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
    display = sh1107.SH1107_I2C(128, 
                                128, 
                                i2c, 
                                res=None, 
                                address=0x3c, 
                                rotate=90, 
                                external_vcc=False,
                                delay_ms=200)

    bar = Bar(display)
    display.sleep(False)
    display.fill(0)
    
    for x in range(101):
        time.sleep(0.1)
        display.fill(0)
        bar.main(x)
        display.show()
