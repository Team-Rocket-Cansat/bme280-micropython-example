import machine
import time

# Initialize I2C bus 0 with pins 8 (SDA) and 9 (SCL)
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))

print("Scanning I2C bus...")
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C devices found.")
else:
    print(f"Found {len(devices)} I2C device(s):")
    for device in devices:
        print(f"  - Decimal address: {device} | Hex address: 0x{device:02X}")