import network
import Markurion.secret as secrets
import urequests

class Wifi:
    def __init__(self):
        print("wi-fi")
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(secrets.SSID,secrets.PASSWORD)
        print(dir(self.wlan.status))
        self.status()
        
    def status(self):
        status = self.wlan.ifconfig()
        print('IP address = ' + status[0])
        print('subnet mask = ' + status[1])
        print('gateway  = ' + status[2])
        print('DNS server = ' + status[3])
            
        
if __name__ == "__main__":
    x = Wifi()
    
