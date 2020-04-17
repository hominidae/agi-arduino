#!/usr/bin/python

from datetime import datetime
import serial
import csv

serial_ob = serial.Serial(port="COM6",baudrate=9600)
filename = datetime.now().strftime("datalog_%Y%m%d_%H%M%S")

def stripline():
    string = serial_ob.readline()
    decoded_bytes = str(string[0:len(string)-2].decode("utf-8"))
    print(decoded_bytes)
    return(decoded_bytes)

try:
    while True:
        serial_log = open(filename + '.csv','a')
        serial_log.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                +str((","))
                +str(stripline())
                +str((","))
                +str(("\n")))
        serial_log.close()
except KeyboardInterrupt:
    pass
