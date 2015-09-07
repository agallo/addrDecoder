#!/usr/bin/python

__author__ = 'agallo'

from time import sleep
import wiringpi2 as wiringpi


# define some pins:

A0 = 11
A1 = 13
A2 = 15

pins = [A0, A1, A2]

# some wiringPi vars to make reading the code easier to read

LOW = 0
HIGH = 1
OUTPUT = 1


def setup():
    wiringpi.wiringPiSetupPhys()
    for pin in pins:
        wiringpi.pinMode(pin, OUTPUT)


# wiringpi.pinMode(A0, OUTPUT)
#    wiringpi.pinMode(A1, OUTPUT)
#    wiringpi.pinMode(A2, OUTPUT)


def sequence(repeat):
    count = 0
    while count <= repeat:
        for pos in range(0, 8):
            if 1 & pos <> 0:
                wiringpi.digitalWrite(A0, HIGH)
            else:
                wiringpi.digitalWrite(A0, LOW)
            if 2 & pos <> 0:
                wiringpi.digitalWrite(A1, HIGH)
            else:
                wiringpi.digitalWrite(A1, LOW)
            if 4 & pos <> 0:
                wiringpi.digitalWrite(A2, HIGH)
            else:
                wiringpi.digitalWrite(A2, LOW)
        count += 1


def AllOff():
    for p in pins:
        wiringpi.digitalWrite(p, LOW)


def cleanup():
    AllOff()


def main():
    setup()
    AllOff()
    #   AllBlink(5)
    sequence(10)
    cleanup()


main()
