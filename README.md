# simple_pico_clock
![Alt text](images/clock_image.webp)
A simple Raspberry Pi Pico project of a digital clock using a 128x32 OLED display, coded in MicroPython

# How to Make the Clock
[My instructable]() shows steps to make this clock.

# Usage
Scrpits for the clock are in `src`. `src/main.py` contains all processins to display time, `src/digits.py` contains hexadecimal digit arrays to be displayed, and `src/ssd1306.py` is the ssd1306 driver from [stlehmann's micropython-ssd1306 fork](https://github.com/stlehmann/micropython-ssd1306/tree/master). 
> [!NOTE]
> ssd1306 is supposed to be included in [MicroPython's main repository](https://github.com/micropython/micropython/tree/master), but I'm having hard time finding it.

## Parameters in `src/main.py`
To run the script `main.py`, you need to set parameters bordered by `Parameters =======` in lines 10 to 33. The firs two parameters are I<sup>2<\sup>C serial clock and data pins.These are GPIO numbers (labeled GP# in the [pinout](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) 0 to 28), not pin numbers (1 to 40).
```python:src/main.py [10-11]
SCLpin = 3 # I2C clock pin assignment
SDApin = 2 # I2C data pin assignment
```

If your Pico board has a user-configurable switch (not the BOOTSEL button, official Pico board doesn't have this but some alternative RP2040 boards do) or if you decided to add an external push button, then you need to set 

# Description of Code
SCLpin and SDApin are used to initialize the I<sup>2<\sup>C instance, which is used to initialize ```SSD1306_I2C()``` instance
```python:src/main.py[124]
i2c = I2C(1,scl=Pin(SCLpin),sda=Pin(SDApin),freq=200000)
```
