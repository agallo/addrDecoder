#!/usr/bin/python

__author__ = 'agallo'

from time import sleep
import wiringpi2 as wiringpi


# define some pins:
# addrDecoder   PhyPin (B+)     T-Cobbler Plus  Breadboard
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
            print "Binary address: " + str(bin(pos)[2:].zfill(3))
            if 1 & pos != 0:
                wiringpi.digitalWrite(A0, HIGH)
                print "     A0 Active : " + str(1 & pos)
            else:
                wiringpi.digitalWrite(A0, LOW)
                print "     A0 Active : " + str(1 & pos)
            if 2 & pos != 0:
                wiringpi.digitalWrite(A1, HIGH)
                print "     A1 Active : " + str(2 & pos)
            else:
                wiringpi.digitalWrite(A1, LOW)
                print "     A1 Active : " + str(2 & pos)
            if 4 & pos != 0:
                wiringpi.digitalWrite(A2, HIGH)
                print "     A2 Active : " + str(4 & pos)
            else:
                wiringpi.digitalWrite(A2, LOW)
                print "     A2 Active : " + str(4 & pos)
            print "*****************"
            sleep(1)
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
    sequence(5)
    cleanup()


main()
