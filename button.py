import machine
import time
button = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
button3 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)

debounce_time=0
count=0

# Callback for intterupt pin

def callback(pin):
    global debounce_time, count
    if (time.ticks_ms()-debounce_time) > 500:
        count += 1
        debounce_time=time.ticks_ms()
        print(f"Pin is: {pin}")
        print(debounce_time)
        print(f"Count is: {count}")
    elif (time.ticks_ms()-debounce_time) > 200:
        debounce_time=time.ticks_ms()
        print("Double click")


# Setup interupt instrucitons
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)
button2.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)
button3.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)

while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        print('Button 1 pressed!')
    elif not first and second:
        print('Button 1 released!')
