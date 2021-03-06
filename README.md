# Welcome, what is agi-arduino?

agi-arduino is intended to perform temperature measurements using DS18B20 temperature sensors and logging
that data via a USB connection to a PC.

# What do I need?

You will need an Arduino. And the DS18B20 temperature sensor IC's.

You'll also need a breadboard and a few jumper wires to connect everything.

See the following tutorial's on how to wire them up:

https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806

https://create.arduino.cc/projecthub/iotboys/how-to-use-ds18b20-water-proof-temperature-sensor-2adecc

https://randomnerdtutorials.com/guide-for-ds18b20-temperature-sensor-with-arduino/

https://www.tweaking4all.com/hardware/arduino/arduino-ds18b20-temperature-sensor/

# How do I use this?

First, install the Arduino IDE. You can download that [here.](http://www.arduino.cc/)

Next, you need to install two libraries to interface with the DS18B20 temperature sensors.

On the github pages for these libraries, select the green "Clone/Download Zip" on the mid-right of the
page.

Save the zip files for those two libraries to your "C:\Users\<Your usename>\Documents\Arduino\libraries\" folder.

Next, open your file browers, go to that directory and unzip the files. You can optionally remove the "-master"
that was appended to the folder name.

Alternatively, download the libraries from this github repository and move the contents of the "libraries" folder to
your Arduino library folder.

# Here are what the two pre-requisite libraries that are needed do:

 - Dallas OneWire i2c interface library, https://github.com/PaulStoffregen/OneWire

  This library gives the Arduino microcontroller the ability to communicate with the DS18B20 temperature sensor.

 - Arduino Temperature Control Library, https://github.com/milesburton/Arduino-Temperature-Control-Library

  This library is written to communicate with the DS18B20 temperature sensor itself.

So, one library sets up the framework for how the Arduino and the DS18B20 talk to each and the other gives the
Arduino the language that they speak to each other in.

# Todo:
 - Figure out data logging problem:
 
    Currently, the Python script will run for several days and the script will hang until a keyboard prompt wakes the
   script up. Then, the serial data in memory will be dumped and issued an incorrect timestamps.
   
    A potential solution would be to construct the records in memory, issuing them a timestamp and storing both the sensor
   values and the timestamp in the same tuple.
   
   Note: Currently running the Python datalogger script with the following command: pyton -m trace --trace SerialLogger.py
    to determine the cause of intermittent hanging. It could be the lack of proper watchdogging.

# Serial Data Logging:
I found this github repository with a simple datalogger written in Python, I had a number of problems with it.

https://github.com/pedrominatel/py_serial_datalogger

The modifications I made to it that serial communications data from Serial.readline() are converted to utf-8, and comma's are added and a new line for each entry.

Simply modify SerialLogger.py with your Arduino com port specific info.

The data is dumped into a CSV file.

# Preliminary use questions:

Question: Can a single 4.7K resistor work for more than one sensor?

Answer: Yes. When placed between the 5VDC power input wire and the single data line that goes to both sensors, it does.
