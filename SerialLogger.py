#!/usr/bin/python
# This script is a data logger for a connected Arduino Uno.
# Set the COM port to your serial device.
# You will need to use Python to install the pyserial library
# The command to do that is "pip install pyserial"

# Note:
#  On Windows, that serial com port will be COM6 or something similar.
#  On Linux, it's /dev/ttyUSB0

# Import Python libraries for handling datetime information and the serial library
from datetime import datetime
import serial

# Create an object linking the serial library interface to the serial communications port
serial_ob = serial.Serial(port="COM6",baudrate=9600)
# Set the file name with the date and time it was started
filename = datetime.now().strftime("datalog_%Y%m%d_%H%M%S")

# Define a function to decode the serial data
def stripline():
    string = serial_ob.readline()
    decoded_bytes = str(string[0:len(string)-2].decode("utf-8"))
    print(decoded_bytes) # Print the values to screen as well
    return(decoded_bytes) # Otherwise, return the decoded serial data to original function call

# Create a loop for reading and updating fresh data
try:
    while True:
        serial_log = open(filename + '.csv','a') # Create file, with date time and append to it.
        serial_log.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # Use the YMD-HMS format for entries.
                +str((",")) # Add a comma
                +str(stripline()) # Call the stripline function
                +str((",")) # Add anoter comma
                +str(("\n"))) # Finish with a new line.
        serial_log.close()
except KeyboardInterrupt:
    pass
