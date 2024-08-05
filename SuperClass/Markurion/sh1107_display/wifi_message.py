import sh1107
import machine
import time
import sys


import machine
import sh1107

class WiFiDisplay:
    def __init__(self,display):
        self.display = display
        
    def main(self):
        self.show_retry()
        
    def show_connected(self):
        self.clear()
        value = "CONNECTED :)"
        self.display.text(f"{value:^17}", 0, 60, 1)
        self.display.show()
        
    def show_connecting(self):
        self.clear()
        value = "Connecting"
        self.display.text(f"{value:^17}", 0, 60, 1)
        value = "To Wi-Fi"
        self.display.text(f"{value:^17}", 0, 80, 1)
        self.display.show()
        
    def show_retry(self, counter=None):
        self.clear()
        value = "Failed"
        self.display.text(f"{value:^17}", 0, 60, 1)
        value = "Trying again"
        self.display.text(f"{value:^17}", 0, 80, 1)
        
        if counter != None:
            self.display.text(f"{counter:^17}", 0, 100, 1)
        
        self.display.show()
        
    def show_config(self,MAC,IP,MASK,GATE,DNS):
        self.clear()
        self.display.text(f"{"MAC":^17}", 0, 0, 1)
        self.display.text(f"{MAC:^17}", 0, 10, 1)
        self.display.text(f"{"IP":^17}", 0, 25, 1)
        self.display.text(f"{IP:^17}", 0, 35, 1)
        self.display.text(f"{"MASK":^17}", 0, 50, 1)
        self.display.text(f"{MASK:^17}", 0, 60, 1)
        self.display.text(f"{"GATE":^17}", 0, 75, 1)
        self.display.text(f"{GATE:^17}", 0, 85, 1)
        self.display.text(f"{"DNS":^17}", 0, 100, 1)
        self.display.text(f"{DNS:^17}", 0, 110, 1)
        self.display.show()
        
    def clear(self):
        self.display.fill(0)
    
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

    bar = WiFiDisplay(display)
    display.sleep(False)
    display.fill(0)
    
    bar.main()
    display.show()
