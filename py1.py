### The required libraries in this code are: PySerial, time###
import serial
import time
Arduino = serial.Serial('COM1',9600)
print(Arduino.readline())

print("Message from Arduino ")

while 1:
    var =  raw_input()
    if(var > 0):
        Arduino.write('1')
        print("Recieved transmission")
        time.sleep(1)
    if(var == 0):
        Arduino.write('0')
        print("LED turned OFF")
        time.sleep(1)
    if(var == "im fine and you"):
        print("im fine too")
    
