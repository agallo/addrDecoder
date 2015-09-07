#!/usr/bin/python

__author__ = 'agallo'

from time import sleep
import wiringpi2 as wiringpi


# define some pins:

OneW = 3
OneB = 5
OneG = 7
OneY = 11
OneR = 13
TwoW = 19
TwoB = 21
TwoG = 23
TwoY = 15
TwoR = 18

pins = [OneW, OneB, OneG, OneY, OneR, TwoW, TwoB, TwoG, TwoY, TwoR]

# some wiringPi vars to make reading the code easier to read

LOW = 0
HIGH = 1
OUTPUT = 1

def setup():
    wiringpi.wiringPiSetupPhys()
    wiringpi.pinMode(OneW, OUTPUT)
    wiringpi.pinMode(OneB, OUTPUT)
    wiringpi.pinMode(OneG, OUTPUT)
    wiringpi.pinMode(OneY, OUTPUT)
    wiringpi.pinMode(OneR, OUTPUT)
    wiringpi.pinMode(TwoW, OUTPUT)
    wiringpi.pinMode(TwoB, OUTPUT)
    wiringpi.pinMode(TwoG, OUTPUT)
    wiringpi.pinMode(TwoY, OUTPUT)
    wiringpi.pinMode(TwoR, OUTPUT)

def AllBlink(repeat):
    count = 0
    while count <= repeat:
        wiringpi.digitalWrite(OneW, LOW)
        wiringpi.digitalWrite(OneB, LOW)
        wiringpi.digitalWrite(OneG, LOW)
        wiringpi.digitalWrite(OneY, LOW)
        wiringpi.digitalWrite(OneR, LOW)
        wiringpi.digitalWrite(TwoW, LOW)
        wiringpi.digitalWrite(TwoB, LOW)
        wiringpi.digitalWrite(TwoG, LOW)
        wiringpi.digitalWrite(TwoY, LOW)
        wiringpi.digitalWrite(TwoR, LOW)
        sleep(1)
        wiringpi.digitalWrite(OneW, HIGH)
        wiringpi.digitalWrite(OneB, HIGH)
        wiringpi.digitalWrite(OneG, HIGH)
        wiringpi.digitalWrite(OneY, HIGH)
        wiringpi.digitalWrite(OneR, HIGH)
        wiringpi.digitalWrite(TwoW, HIGH)
        wiringpi.digitalWrite(TwoB, HIGH)
        wiringpi.digitalWrite(TwoG, HIGH)
        wiringpi.digitalWrite(TwoY, HIGH)
        wiringpi.digitalWrite(TwoR, HIGH)
        sleep(1)
        count += 1


def sequence(repeat):
    count = 0
    while count <= repeat:
        for p in pins:
            wiringpi.digitalWrite(p, HIGH)
            sleep(count*.1)
            wiringpi.digitalWrite(p, LOW)
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
