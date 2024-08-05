import machine
import time

#Class optimised for 3 buttons
#To use it just override an btn action methods.

class Buttons:
    def __init__(self, btn1, btn2, btn3):
        self.btn1 = btn1
        self.btn2= btn2
        self.btn3 = btn3
        self.debounce_time=0
        self.setup_interupt()
        
    # Setup interupt instrucitons
    def setup_interupt(self):
        self.btn1.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.callback)
        self.btn2.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.callback)
        self.btn3.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.callback)
    
    def btn1_action(self):
        print(f"Exceutte btn 1 action override this method.... ")
    
    def btn2_action(self):
        print(f"Exceutte btn 2 action override this method.... ")
    
    def btn3_action(self):
        print(f"Exceutte btn 3 action override this method.... ")
    
    # Select the proper button action
    def select_callback(self,pin):
        if pin == btn1:
            self.btn1_action()
        elif pin == btn2:
            self.btn2_action()
        elif pin == btn3:
            self.btn3_action()

    def callback(self, pin):
        if (time.ticks_ms()- self.debounce_time) > 500:
            self.debounce_time=time.ticks_ms()
            self.select_callback(pin)


if __name__ == "__main__":
    btn1 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
    btn2 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
    btn3 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
    
    # Overriding of btn methods
    # Best to do it in other file, here just as example in same file
    class Controller(Buttons):
        def __init__(self,btn1,btn2,btn3):
            super().__init__(btn1,btn2,btn3) 
        def btn1_action(self):
            print("Ha btn 1")
        def btn2_action(self):
            print("Ha btn 2")
        def btn3_action(self):
            print("Ha btn 3")
    
    # Real part now we created an controller with differnet methods
    # So this should work well
    btn_controll_class = Controller(btn1, btn2, btn3)
    
    while True:
    # Infinite loop to show interupt callback in action
        first = btn1.value()
        time.sleep(0.01)
        second = btn1.value()

