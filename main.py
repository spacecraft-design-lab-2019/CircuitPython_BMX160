import time, board, busio
import BMX160
from BMX160 import BMX160_I2C
from BMX160 import BMX160_I2C_ADDR

import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led[0] = [255, 20, 50]
led.brightness = 0.01

def rainbow(led):
    col = led[0]
    col = [(125 - i)%255 for i in col]
    led[0] = col

i2c = busio.I2C(board.SCL, board.SDA)
sensor = BMX160_I2C(i2c)

# RESET:
sensor.write_u8(BMX160.BMX160_COMMAND_REG_ADDR, BMX160.BMX160_SOFT_RESET_CMD)
time.sleep(BMX160.BMX160_SOFT_RESET_DELAY_MS)

# attempt a self test (fails to write to...)
# sensor.write_u8(0x6D, 0b10000)
while True:
    # print(sensor._BUFFER)
    # sensor.read_all()
    # print(sensor.read_u8(BMX160.BMX160_CHIP_ID_ADDR))
    print("data registers")
    for i in range(4, 23):
        print(sensor.read_u8(i), end = " ")
    print("\n status register")
    print(bin(sensor.read_u8(BMX160.BMX160_STATUS_ADDR)))
    print("error register")
    print(sensor.query_error())

    print("all registers")
    for i in range(126, -1, -1):
        if i % 10 == 0:
            print()
        print("{i: >4}".format(i=hex(i)), end = "->")
        print("{i: >4}".format(i=hex(sensor.read_u8(i))), end = "  ")
    print()
    # sensor.write_u8(0x68, 1)

    time.sleep(2)
    rainbow(led)

# while not i2c.try_lock():
#     pass



# while True:
#     print("I2C addresses found:", [hex(device_address) for device_address in i2c.scan()])

#     # sensor = BMX160_I2C(i2c)
#     # print("bmx")
#     time.sleep(2)