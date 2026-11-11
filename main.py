#
# this script for the rp2040 port assumes the I2C connections at
# GPIO8 and 9. At the RPi Pico, these are the board pins 11 and 12
# Please check that pull-up resistors are in place at sda and scl.
#
import machine
import bme280_float as bme280

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
bme = bme280.BME280(i2c=i2c)

print(bme.values)
