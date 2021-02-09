import serial as s
import io
try:
    ser = s.Serial('COM3', 9600)
   
except s.SerialException:
    print("NO connection detected")
ser = s.serial_for_url('', timeout = 1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
class s.Serial:
    def __init__(port='COM1', baudrate=9600, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE, timeout=None,rtscts=False):
        
