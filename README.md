# bme280-micropython-example

This example outputs data from the BME280 sensor.  

## How to use  

In this example, we will be using the pi pico w.  

1. Connect the pins of the sensor in this order:  

| Sensor Pin | Pi Pin                |
|------------|-----------------------|
| Power      | 3v / 5v (36 / 40)     |
| GND        | GND (38)              |
| SDA        | SDA0 (pin 11 / gpio8) |
| SCL        | SCL0 (pin 12 / gpio9) |

Since we are using I2C, there may be some unused pins / cables. This is fine.  

2. Install MicroPython  

Download the micropython u2f file from [micropython.org](https://micropython.org/download/RPI_PICO_W/) ([Direct Link](https://micropython.org/resources/firmware/RPI_PICO_W-20260824-v1.29.0.uf2))  
  
Hold down the BOOT button and plug in your pi pico into your computer. It should appear as a USB drive. Copy the .u2f file on the newly appeared USB drive.  

3. Install the code  

Copy the code inside [bme280.py](bme280.py) and save it to the pi pico as `bme280.py` in the root directory.
Copy the code inside [main.py](./main.py) and save it to the pi pico as `main.py` in the root directory.  

4. Run the code  

Open your `main.py` program and run the code. If it is successful, it should output the values.  

## Common issues  

### OSError: [Errno 5] EIO  

`OSError: [Errno 5] EIO` means that your I2C device isn't being recognised.  
Either the wire connections aren't stable, your I2C device isn't recieving power, you connected it to the wrong I2C pins or your device has a different address.  
  
Connected to other pins?   
Adjust this line in main.py to match your pins   
`i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))`  
  
Still not working?   
Check for the address of your device by running [i2c-scan.py](./i2c-scan.py)  
Then change this line in [bme280.py](./bme280.py) to match your address:  
`BME280_I2CADDR = 0x76`  
  
If connecting power to 3v doesn't work, try connect it to 5v (ensure your sensor works with it)  
DO NOT SWAP POWER AND GROUND OR YOU WILL FRY YOUR SENSOR.
