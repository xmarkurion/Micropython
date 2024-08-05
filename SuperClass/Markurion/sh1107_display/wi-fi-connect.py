import network
import Markurion.secret as secrets
from Markurion.sh1107_display.wifi_message import WiFiDisplay
from time import sleep
import ubinascii

import sh1107
import machine

class Wifi:
    def __init__(self):
        self.ssid = ""
        self.password = ""
        self.IP = ""
        self.MASK = ""
        self.GATE = ""
        self.DNS = ""
        self.MAC = ""
        
        self.sta_if = None
        
        # Display controll
        self.screen = self.setupDisplay()
    
    def setupDisplay(self):
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

        display.sleep(False)
        display.fill(0)
        return WiFiDisplay(display)
        
    def setSSID(self, ssid):
        self.ssid = ssid
    
    def setPASSWORD(self, password):
        self.password = password
        
    def disconnect(self):
        self.sta_if.disconnect()

    def connect(self):
        if (len(self.ssid) == 0 ):
            print(f"Please set SSID .setSSID(\"your SSID\")")
            return False
        
        if (len(self.password) == 0 ):
            print(f"Please set pass .setPASSWORD(\"your password\")")
            return False
        
        # Inform user that wi-fi attempt is beeing made....
        self.screen.show_connecting()
        sleep(1)
        
        import network
        q = 0
        self.sta_if = network.WLAN(network.STA_IF)
        if not self.sta_if.isconnected():
            self.sta_if.active(True)
            self.sta_if.connect(self.ssid,self.password)
            while not self.sta_if.isconnected():
                if(q >= 6):
                    return 0
                if(q <= 5):
                    print(f"Can't connect retry ..{q}")
                    self.screen.show_retry(q) 
                    sleep(1) 
                q += 1
                pass # wait till connection
        self.IP, self.MASK, self.GATE, self.DNS = self.sta_if.ifconfig()
        self.MAC = ubinascii.hexlify(self.sta_if.config('mac'),':').decode().upper()
        MACC = ubinascii.hexlify(self.sta_if.config('mac'),':').decode().upper().split(":")
        MAC_one_line = ""
        for letter in MACC:
            MAC_one_line += letter
        print("\n")
        print(f"{'Network':_^23}")
        print(f"{'MAC': <6}{self.MAC}")
        print(f"{'IP': <6}{self.IP}\n{'MASK': <6}{self.MASK}\n{'Gate': <6}{self.GATE}\n{'Dns': <6}{self.DNS}")
        print(f"\n{'Connected':_^23}")
        
        self.screen.show_config(MAC_one_line,self.IP,self.MASK,self.GATE,self.DNS)
        sleep(2)
        self.screen.show_connected()
        sleep(1)

        return 1
            
if __name__ == "__main__":
    network = Wifi()
    network.setSSID(secrets.SSID)
    network.setPASSWORD(secrets.PASSWORD)
    network.connect()
    
    sleep(1)
    network.disconnect()
    