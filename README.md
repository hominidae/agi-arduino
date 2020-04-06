# Welcome, what is agi-arduino?

agi-arduino is intended to perform temperature measurements using DS18B20 temperature sensors and logging
that data via a USB connection to a PC.

# How do I use this?

First, install the Arduino IDE. You can download that [here.](http://www.arduino.cc/)

Next, you need to install two libraries to interface with the DS18B20 temperature sensors.

On the github pages for these libraries, select the green "Clone/Download Zip" on the mid-right of the
page. Save the zip files to "C:\Users\<Your usename>\Documents\Arduino\libraries\" folder, then go there
and unzip the files. You can also remove the "-master" portion.

 - Dallas OneWire i2c interface library, https://github.com/PaulStoffregen/OneWire
  This library gives the Arduino microcontroller the ability to communicate with the DS18B20 temperature sensor.

 - Arduino Temperature Control Library, https://github.com/milesburton/Arduino-Temperature-Control-Library
  This library is written to communicate with the DS18B20 temperature sensor itself.

So, one library sets up the framework for how the Arduino and the DS18B20 talk to each and the other gives the
Arduino the language that they speak to each other in.

# Instructons to follow

There are several projects that serve as excellent guides for working with the DS18B20 temperature sensors.

We'll be using them as a starting ground for accomplishing the objective of connecting an Arduino to a PC and
logging the temperature of any connected sensors for a long period of time.

https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806

https://create.arduino.cc/projecthub/iotboys/how-to-use-ds18b20-water-proof-temperature-sensor-2adecc

https://randomnerdtutorials.com/guide-for-ds18b20-temperature-sensor-with-arduino/



