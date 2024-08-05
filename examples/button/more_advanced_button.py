# This example was tested on MicroPython v1.23.0 on 2024-06-02; LOLIN_C3_MINI with ESP32-C3FH4
# 2024/08/05

import machine
import time
btn1 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
btn2 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
btn3 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)

# Time elapsed between two consecutive button presses if multiple 
# inputs occur within a certain time interval,only one input is registered. 
debounce_time=0

# Callback for intterupt pin
def btn1_callback():
    print(f"Exceutte btn 1 action ")
    
def btn2_callback():
    print(f"Exceutte btn 2 action ")
    
def btn3_callback():
    print(f"Exceutte btn 3 action ")

# Select the proper button action
def select_callback(pin):
    if pin == btn1:
        btn1_callback()
    elif pin == btn2:
        btn2_callback()
    elif pin == btn3:
        btn3_callback()

def callback(pin):
    global debounce_time
    if (time.ticks_ms()-debounce_time) > 500:
        debounce_time=time.ticks_ms()
        select_callback(pin)

# Setup interupt instrucitons
btn1.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)
btn2.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)
btn3.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)

while True:
    # Infinite loop to show interupt callback in action
    first = btn1.value()
    time.sleep(0.01)
    second = btn1.value()
#     if first and not second:
#         print('Button 1 pressed!')
#     elif not first and second:
#         print('Button 1 released!')
