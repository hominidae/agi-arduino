# Welcome, what is agi-arduino?

agi-arduino is intended to perform temperature measurements using DS18B20 temperature sensors and logging
that data via a USB connection to a PC.

# What do I need?

You will need an Arduino. And a couple of DS18B20 temperature sensor IC's.

You'll also need a breadboard and a few jumper wires.

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

# A better overview of how to wire the DS18B20 sensors are available from these tutorials:

We'll be using them as a starting ground for accomplishing the objective of connecting an Arduino to a PC and
logging the temperature of any connected sensors for a long period of time.

https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806

https://create.arduino.cc/projecthub/iotboys/how-to-use-ds18b20-water-proof-temperature-sensor-2adecc

https://randomnerdtutorials.com/guide-for-ds18b20-temperature-sensor-with-arduino/

https://www.tweaking4all.com/hardware/arduino/arduino-ds18b20-temperature-sensor/

# Todo:

 - Write code to collect the serial numbers of the DS18B20 sensors for identification purposes
  Here is a write-up on using Python to connect to a serial device
  https://pyserial.readthedocs.io/en/latest/shortintro.html
 - Write an application collect serial communications data from the Arduino


# Preliminary use questions:

Question: Can a single 4.7K resistor work for more than one sensor?

Answer: Yes. When placed between the 5VDC power input wire and the single data line that goes to both sensors, it does.
