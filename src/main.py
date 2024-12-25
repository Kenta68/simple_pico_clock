# RP Pico 128x32 OLED display (SSD 1306) clock using RP2040's internal RTC

import framebuf
from time import sleep
from machine import Pin,I2C,RTC
from ssd1306 import SSD1306_I2C
from digits import *

# Parameters (check these before executing) ============================
SCLpin = 3 # I2C clock pin assignment
SDApin = 2 # I2C data pin assignment

timesetbutton = True # True if the pico board has a push button for setting time, otherwise false (if false, set time by editing the settime variable below)
buttonpin = 24 # push button (for setting time) pin assignment
buttontype = False # True if the push button is pull down (normally 0), False if pull up (normally 1)

settime = (2024,8,2,4,16,22,0,0) # Enter the time to be set here as a tuple (year,month,day,weekday(Monday=0),hour,minutes,second,sub-second)

show24h = False # False to diaplay time only in 0:00 to 12:59 with AM/PM

mybirthday = (6,22) # (month,date) of your birthday so that the clock can celebrate it

autodsave = True # True to enable auto-correcting for daylight saving time (auto-correction is not executed when the script starts)
dsavestart = (3,6,2) # daylight saving time start date (month,weekday,weekday count from the beginning of month), for example, "second sunday in March" = (3,6,1)
dsaveend = (11,6,1) # daylight saving time end date (month,weekday,weekday count from the beginning of month), weekday is the index of the "weekdays" array
dsavetime = (2,0) # (hours,minutes), the starting and ending time of the daylight saving time
# Note: if dsavetime[0] +/- dsavehourshift <0 or > 24, daylight saving time correction will not work
dsavehourshift = 1 # [hour], how many hours to shift by the daylight saving time

WIDTH  = 128 # OLED pixel definition (WxH)
HEIGHT = 32

contrast = 200 # display contrast (0 to 255)
# Parameters (end) ====================================================

weekdays = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# Digit arrays
dsize = (32,24) # (height,width) of the digit arrays
csize = (32,8) # (height,width) of colon
cakesize = (16,24) # (height,width) of the birthday cake
d0 = bytearray(d0)
d1 = bytearray(d1)
d2 = bytearray(d2)
d3 = bytearray(d3)
d4 = bytearray(d4)
d5 = bytearray(d5)
d6 = bytearray(d6)
d7 = bytearray(d7)
d8 = bytearray(d8)
d9 = bytearray(d9)
colon = bytearray(colon)
cake = bytearray(cake)
d0 = framebuf.FrameBuffer(d0,dsize[1],dsize[0],framebuf.MONO_HLSB)
d1 = framebuf.FrameBuffer(d1,dsize[1],dsize[0],framebuf.MONO_HLSB)
d2 = framebuf.FrameBuffer(d2,dsize[1],dsize[0],framebuf.MONO_HLSB)
d3 = framebuf.FrameBuffer(d3,dsize[1],dsize[0],framebuf.MONO_HLSB)
d4 = framebuf.FrameBuffer(d4,dsize[1],dsize[0],framebuf.MONO_HLSB)
d5 = framebuf.FrameBuffer(d5,dsize[1],dsize[0],framebuf.MONO_HLSB)
d6 = framebuf.FrameBuffer(d6,dsize[1],dsize[0],framebuf.MONO_HLSB)
d7 = framebuf.FrameBuffer(d7,dsize[1],dsize[0],framebuf.MONO_HLSB)
d8 = framebuf.FrameBuffer(d8,dsize[1],dsize[0],framebuf.MONO_HLSB)
d9 = framebuf.FrameBuffer(d9,dsize[1],dsize[0],framebuf.MONO_HLSB)
colon = framebuf.FrameBuffer(colon,csize[1],csize[0],framebuf.MONO_HLSB)
cake = framebuf.FrameBuffer(cake,cakesize[1],cakesize[0],framebuf.MONO_HLSB)

def givedbuff(num):
    """Returns the FrameBuffer corresponding to num"""
    if num == 0:
        return d0
    elif num == 1:
        return d1
    elif num == 2:
        return d2
    elif num == 3:
        return d3
    elif num == 4:
        return d4
    elif num == 5:
        return d5
    elif num == 6:
        return d6
    elif num == 7:
        return d7
    elif num == 8:
        return d8
    elif num == 9:
        return d9

def buttonevent(button,timeout=2):
    """
    Waits for button press and release event
    Arguments:
        button: machine.Pin(_,machine.Pin.IN) instance
        timeout: [s], float, longest time to wait for button event
    Returns:
        time: [s], float, the duration for which the button was pressed, 0 if timeout
    """
    interval = 0.01 # [s], float, time interval between event check
    buttonstate = False # bool, True if button is pressed, False otherwise
    oncount = 0 # int, count of number of intervals for which the button was on
    while True: # wait for button to be unpressed
        if not ((buttontype and button.value()) or not (buttontype or button.value())):
            break
    while True:
        if not buttonstate and ((buttontype and button.value()) or not (buttontype or button.value())): # button pressed
            buttonstate = True
        elif buttonstate and not ((buttontype and button.value()) or not (buttontype or button.value())): # button released
            return oncount*interval
        elif buttonstate: # increment oncount
            oncount += 1
        if buttonstate and oncount*interval > timeout: # button press event when timeout
            return (oncount+1)*interval
        elif not buttonstate and oncount*interval > timeout: # no button press event detected before timeout
            return 0
        sleep(interval)

if buttontype:
    button = Pin(buttonpin,Pin.IN,Pin.PULL_DOWN) # define a push button for setting time
else:
    button = Pin(buttonpin,Pin.IN,Pin.PULL_UP) # define a push button for setting time

# Initialize the I2C and display
i2c = I2C(1,scl=Pin(SCLpin),sda=Pin(SDApin),freq=200000)
display = SSD1306_I2C(WIDTH,HEIGHT,i2c)
display.contrast(contrast)

rtc = RTC()
rtc.datetime(settime) # set time

datetime = (0,0,0,0,0,0) # (year,month,day,weekday(Monday=0),hour,minutes)
while True:
    datetime2 = rtc.datetime()[:6] # (year,month,day,weekday(Monday=0),hour,minute)
    if datetime2 != datetime: # time changed by at least a minute
        datetime = datetime2

        # Daylight saving time correction
        if autodsave and datetime[4:6] == dsavetime: # detect (hour,minute) of daylight saving time
            if (datetime[1],datetime[3]) == dsavestart[0:2]: # check (month,weekday)
                if datetime[2]//7 + 1 == dsavestart[2]:
                    datetime3 = rtc.datetime()
                    rtc.datetime((datetime3[0],datetime3[1],datetime3[2],datetime3[3],datetime3[4]+dsavehourshift,datetime3[5],datetime3[6],datetime3[7]))
            elif (datetime[1],datetime[3]) == dsaveend[0:2]: # check (month,weekday)
                if datetime[2]//7 + 1 == dsaveend[2]:
                    datetime3 = rtc.datetime()
                    rtc.datetime((datetime3[0],datetime3[1],datetime3[2],datetime3[3],datetime3[4]-dsavehourshift,datetime3[5],datetime3[6],datetime3[7]))


        display.fill(0) # erace the display

        # Calculate time digits and display
        if show24h:
            h2 = datetime[4]%10 # the second digit of hour
            h1 = (datetime[4]-h2)//10 # the first digit of hour
        else:
            if datetime[4] > 12: # afternoon (after 12:00 PM)
                h2 = (datetime[4]-12)%10 # the second digit of hour
                h1 = (datetime[4]-12-h2)//10 # the first digit of hour
                display.text("PM",0,24)
            else: # morning (before 12:00 PM)
                h2 = datetime[4]%10 # the second digit of hour
                h1 = (datetime[4]-h2)//10 # the first digit of hour
                display.text("AM",0,24)

        m2 = datetime[5]%10 # the second digit of minutes
        m1 = (datetime[5]-m2)//10 # the first digit of minutes

        if h1 > 0: # afternoon
            display.blit(givedbuff(h1),WIDTH-dsize[1]*4-csize[1],0)
        display.blit(givedbuff(h2),WIDTH-dsize[1]*3-csize[1],0) # display hour and minute digits
        display.blit(colon,WIDTH-dsize[1]*2-csize[1],0)
        display.blit(givedbuff(m1),WIDTH-dsize[1]*2,0)
        display.blit(givedbuff(m2),WIDTH-dsize[1],0)

        if datetime[1:3] == mybirthday: # detect birthday
            display.blit(cake,0,HEIGHT-cakesize[0])

 #       display.text(str(datetime[1]),0,0) # display month
        display.text(str(datetime[2]),0,0) # display day
        display.text(weekdays[datetime[3]],0,12) # display week
        display.show()

    sleep(1) # sleep 1 sec


    # Detect button press event and edit time
    if timesetbutton: # if time setting button exists
        if (buttontype and button.value()) or not (buttontype or button.value()): # button pressed
            newdatetime = [datetime[0],datetime[1],datetime[2],datetime[3],datetime[4],datetime[5]] # [year,month,day,weekday(Monday=0),hour,minutes], var for keeping new time
            # Show hot to set time
            display.fill(0)
            display.text("<1s press-> inc.",0,0)
            display.text(">2s press-> next",0,12)
            display.text("Press to start..",0,24)
            display.show()
            while True:
                presstime = buttonevent(button)
                if presstime > 0.001 and presstime < 1: # short press -> set time

                    # set day
                    display.fill(0) # erace the display
                    display.text("Date: "+str(newdatetime[2]),0,0) # display day
                    display.text("1 s press-> dec.",0,12)
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> increment day by 1
                            newdatetime[2] = (newdatetime[2])%31+1
                            display.fill(0) # erace the display
                            display.text("Date: "+str(newdatetime[2]),0,0) # display day
                            display.text("1 s press-> dec.",0,12)
                            display.show()
                        if presstime >= 1 and presstime < 2: # short button press -> increment day by 1
                            if newdatetime[2] > 1:
                                newdatetime[2] = newdatetime[2]-1
                                display.fill(0) # erace the display
                                display.text("Date: "+str(newdatetime[2]),0,0) # display day
                                display.text("1 s press-> dec.",0,12)
                                display.show()
                        elif presstime > 2: # long button press -> exit loop and go to month setting
                            break

                    # set month
                    display.fill(0) # erace the display
                    display.text("Month: "+str(newdatetime[1]),0,0) # display month
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> increment month by 1
                            newdatetime[1] = (newdatetime[1])%12+1
                            display.fill(0) # erace the display
                            display.text("Month: "+str(newdatetime[1]),0,0) # display month
                            display.show()
                        elif presstime > 1: # long button press -> exit loop and go to year setting
                            break

                    # set year
                    display.fill(0) # erace the display
                    display.text("Year: "+str(newdatetime[0]),0,0) # display year
                    display.text("1 s press-> dec.",0,12) # display year
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> increment year by 1
                            newdatetime[0] = newdatetime[0]+1
                            display.fill(0) # erace the display
                            display.text("Year: "+str(newdatetime[0]),0,0) # display year
                            display.text("1 s press-> dec.",0,12)
                            display.show()
                        elif presstime >= 1 and presstime < 2: # intermediate button press -> decreemnt year by 1
                            if newdatetime[0] > 1:
                                newdatetime[0] = newdatetime[0]-1
                                display.fill(0) # erace the display
                                display.text("Year: "+str(newdatetime[0]),0,0) # display year
                                display.text("1 s press-> dec.",0,12)
                                display.show()
                        elif presstime > 2: # long button press -> go to weekday setting
                            break

                    # set weekday
                    display.fill(0) # erace the display
                    display.text("Weekday: "+weekdays[newdatetime[3]],0,12) # display weekday
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> increment weekday by 1
                            newdatetime[3] = (newdatetime[3]+1)%7
                            display.fill(0) # erace weekday
                            display.text("Weekday: "+weekdays[newdatetime[3]],0,12) # display month
                            display.show()
                        elif presstime > 1: # long button press -> go to hour setting
                            break

                   # Set hour
                    display.fill(0) # erace the display
                    h2 = newdatetime[4]%10 # the second digit of hour
                    h1 = (newdatetime[4]-h2)//10 # the first digit of hour
                    display.blit(givedbuff(h1),WIDTH-dsize[1]*4-csize[1],0) # display hour digits
                    display.blit(givedbuff(h2),WIDTH-dsize[1]*3-csize[1],0)
                    display.blit(colon,WIDTH-dsize[1]*2-csize[1],0)
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> increment hour
                            newdatetime[4] = (newdatetime[4]+1)%24 #  increment hour
                            display.fill(0) # erace the display
                            h2 = newdatetime[4]%10 # the second digit of hour
                            h1 = (newdatetime[4]-h2)//10 # the first digit of hour
                            display.blit(givedbuff(h1),WIDTH-dsize[1]*4-csize[1],0) # display hour digits
                            display.blit(givedbuff(h2),WIDTH-dsize[1]*3-csize[1],0)
                            display.blit(colon,WIDTH-dsize[1]*2-csize[1],0)
                            display.show()
                        elif presstime > 2: # long button press -> exit loop and go to minute setting
                            break

                    # set minutes
                    display.fill(0) # erace the display
                    display.blit(colon,WIDTH-dsize[1]*2-csize[1],0)
                    display.blit(givedbuff(m1),WIDTH-dsize[1]*2,0)
                    display.blit(givedbuff(m2),WIDTH-dsize[1],0)
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> increment minute by 1
                            newdatetime[5] = (newdatetime[5]+1)%60 #  increment minute
                            display.fill(0) # erace the display
                            m2 = newdatetime[5]%10 # the second digit of minutes
                            m1 = (newdatetime[5]-m2)//10 # the first digit of minutes
                            display.blit(givedbuff(m1),WIDTH-dsize[1]*2,0)
                            display.blit(givedbuff(m2),WIDTH-dsize[1],0)
                            display.blit(colon,WIDTH-dsize[1]*2-csize[1],0)
                            display.show()
                        if presstime >= 1 and presstime < 2: # intermediate button press -> increment minute by 10
                            newdatetime[5] = (newdatetime[5]+10)%60 #  increment minute
                            display.fill(0) # erace the display
                            m2 = newdatetime[5]%10 # the second digit of minutes
                            m1 = (newdatetime[5]-m2)//10 # the first digit of minutes
                            display.blit(givedbuff(m1),WIDTH-dsize[1]*2,0)
                            display.blit(givedbuff(m2),WIDTH-dsize[1],0)
                            display.blit(colon,WIDTH-dsize[1]*2-csize[1],0)
                            display.show()
                        elif presstime > 2: # long button press -> exit setting
                            break


                    rtc.datetime((newdatetime[0],newdatetime[1],newdatetime[2],newdatetime[3],newdatetime[4],newdatetime[5],0,0)) # set new time
                    datetime = (0,0,0,0,0,0) # (year,month,day,weekday(Monday=0),hour,minutes) reset datetime to show new time on display
                    break


                if presstime > 1: # long press -> set other things

                    # set 12h/24h
                    display.fill(0) # erace the display
                    display.text("Show 24h: "+str(show24h),0,0) # display show24h
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> change show24h
                            show24h = not show24h
                            display.fill(0) # erace the display
                            display.text("Show 24h: "+str(show24h),0,0) # display show24h
                            display.show()
                        elif presstime > 1: # long button press -> break
                            break

                    # set birthday
                    display.fill(0) # erace the display
                    display.text("Birth month: "+str(mybirthday[0]),0,0) # display month of birthday
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> change show24h
                            mybirthday = (mybirthday[0]%12+1,mybirthday[1])
                            display.fill(0) # erace the display
                            display.text("Birth month: "+str(mybirthday[0]),0,0) # display month of birthday
                            display.show()
                        elif presstime > 1: # long button press -> break
                            break

                    display.fill(0) # erace the display
                    display.text("Birthday: "+str(mybirthday[0])+"/"+str(mybirthday[1]),0,0) # display month of birthday
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> change show24h
                            mybirthday = (mybirthday[0],mybirthday[1]%31+1)
                            display.fill(0) # erace the display
                            display.text("Birthday: "+str(mybirthday[0])+"/"+str(mybirthday[1]),0,0) # display month of birthday
                            display.show()
                        elif presstime > 1: # long button press -> break
                            break

                    # enable/disable daylight saving time
                    display.fill(0) # erace the display
                    display.text("Correct daylight",0,0) #
                    display.text("savint time:",0,12) #
                    display.text(str(autodsave),0,24) #
                    display.show()
                    while True:
                        presstime = buttonevent(button)
                        if presstime > 0.001 and presstime < 1: # short button press -> change show24h
                            autodsave = not autodsave
                            display.fill(0) # erace the display
                            display.text("Correct daylight",0,0) #
                            display.text("savint time:",0,12) #
                            display.text(str(autodsave),0,24) #
                            display.show()
                        elif presstime > 1: # long button press -> break
                            break
                            
                    datetime = (0,0,0,0,0,0) # (year,month,day,weekday(Monday=0),hour,minutes) reset datetime to show new time on display
                    break
