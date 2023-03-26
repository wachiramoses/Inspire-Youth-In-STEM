from machine import UART
from DCMotor import DCMotor 
from machine import Pin, PWM
from time import sleep
import bluetooth
from ble_uart_peripheral import BLEUART

import time
import utime
frequency = 15000       
pin1 = Pin(22, Pin.OUT)    
pin2 = Pin(21, Pin.OUT)  
pin3 = Pin(19, Pin.OUT)    
pin4 = Pin(18, Pin.OUT) 
 
enable = PWM(Pin(23), frequency)  
enable1 = PWM(Pin(5), frequency)
dc_motor = DCMotor(pin1, pin2, enable)      
dc_motor = DCMotor(pin1, pin2, enable, 350, 1023)
dc_motor1 = DCMotor(pin3, pin4, enable1)      
dc_motor1 = DCMotor(pin3, pin4, enable1, 350, 1023)

# Create BLE object
ble = bluetooth.BLE()
# Open UART session for BLE
uart = BLEUART(ble)
# Define ISR for an UART input on BLE connection
def on_rx():
    # Read UART string, AppInventor sends raw bytes
    uart_in = uart.read() # lire le message recu du Smartphone via Bluetooth
    print("UART IN: ", uart_in.decode()) # afficher le message recu du Smartphone sur le console de Thonny
    if (uart_in.decode().find('forward')==0): 
       dc_motor.forward(100) # the car moves forward
       dc_motor1.forward(100)
    if (uart_in.decode().find('right')==0): 
       dc_motor.forward(100) # the car turns right
       dc_motor1.forward(10)
    if (uart_in.decode().find('left')==0): 
       dc_motor.forward(10) # the car turns left
       dc_motor1.forward(100)
    if (uart_in.decode().find('backward')==0): 
       dc_motor.backwards(100) # the car backs up
       dc_motor1.backwards(100)
    if (uart_in.decode().find('stop')==0): 
       dc_motor.stop() # la voiture tourne a droite
       dc_motor1.stop()    

# Map ISR to UART read interrupt
uart.irq(handler=on_rx)
uart.close()