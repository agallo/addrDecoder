#!/usr/bin/python

__author__ = 'agallo'

from time import sleep
import wiringpi2 as wiringpi


# define some pins:
# variable = PhyPin (B+)        T-Cobbler Plus  Breadboard
A0 = 11                         # GPIO17        A6
A1 = 13                         # GPIO27        A7
A2 = 15                         # GPIO22        A8

pins = [A0, A1, A2]

# some wiringPi vars to make reading the code easier to read

LOW = 0
HIGH = 1
OUTPUT = 1


def setup():
    wiringpi.wiringPiSetupPhys()
    for pin in pins:
        wiringpi.pinMode(pin, OUTPUT)


def sequence(repeat):
    count = 0
    while count <= repeat:
        for pos in range(0, 8):
            print "Decimal Position (Selected Chip): " + str(pos)
            # this print statement prints the binary pattern (or High-Low) pattern
            # sent to the address decoders input pins (A0 - A2)
            # it converts the int var 'pos' to a binary, strips off the two leading
            # characters ([2:]) (which are always 0b to signify a binary value)
            # and then left pads the resulting value with zeros to make a 3-digit binary
            print "Binary address: " + str(bin(pos)[2:].zfill(3))
            if 1 & pos != 0:
                wiringpi.digitalWrite(A0, HIGH)
                print "     A0 Active : 1 True"
            else:
                wiringpi.digitalWrite(A0, LOW)
                print "     A0 Active : 0 False"
            if 2 & pos != 0:
                wiringpi.digitalWrite(A1, HIGH)
                print "     A1 Active : 1 True"
            else:
                wiringpi.digitalWrite(A1, LOW)
                print "     A1 Active : 0 False"
            if 4 & pos != 0:
                wiringpi.digitalWrite(A2, HIGH)
                print "     A2 Active : 1 True"
            else:
                wiringpi.digitalWrite(A2, LOW)
                print "     A2 Active : 0 False"
            print "*****************"
            sleep(.5)
        count += 1


def AllOff():
    # this sets all address decoder address input pins (A0 - A2) to low
    # this does not, however, cause all address decorder output pins
    # to go low.  To set all output pins (Y0 - Y7) to low,
    # you need to set E1-E2-E3 is a state OTHER than Low-Low-High
    for p in pins:
        wiringpi.digitalWrite(p, LOW)


def cleanup():
    AllOff()


def main():
    setup()
    AllOff()
    #   AllBlink(5)
    sequence(205)
    cleanup()


main()
