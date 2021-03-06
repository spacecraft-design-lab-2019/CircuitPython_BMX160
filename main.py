import time
import sys
import storage
import board
import busio
import adafruit_sdcard
from digitalio import DigitalInOut
import BMX160 as bmx160

import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led[0] = [20, 255, 50]
led.brightness = 0.01

################### set up BMX160 through I2C ###################

i2c = busio.I2C(board.SCL1, board.SDA1)
bmx = bmx160.BMX160_I2C(i2c)

# print('PMU_STATUS:\t',hex(bmx.read_u8(0x03)))
# bmx.write_u8(address=0x7E,val=0xA0) # writes NVM backed registers into NVM
# bmx.write_u8(address=0x7E,val=0xB0) # clear FIFO
# bmx.write_u8(address=0x7E,val=0xB1) # reset interrupts
time.sleep(0.05)

# TEST BMX:
bmx.read_all()
for b in bmx._BUFFER:
    print(hex(b), end = ", ")
print('')
print("gyro:", bmx.gyro)
print("accel:", bmx.accel)
print("mag:", bmx.mag)

# ################### set up SD card through SPI  ###################

# spi = busio.SPI(board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# cs_sd = DigitalInOut(board.A2)
# sdcard = adafruit_sdcard.SDCard(spi, cs_sd)

# # Use the filesystem as normal. Files are under "/sd"
# vfs = storage.VfsFat(sdcard)
# storage.mount(vfs, "/sd")
# sys.path.append("/sd")

# #################### SET UP THE FILE (new one if one already exists) ####################

# filename = '/sd/sensordata1.csv'
# badname = True
# while badname:
#     try:
#         with open(filename) as f:
#             # Set a new filename, since this one already exists
#             fl = list(filename)
#             fl[-5] = str(int(fl[-5]) + 1)
#             filename = "".join(fl)
#     except Exception as e:
#         print(type(e))
#         badname = False

# print("Saving into {}".format(filename))
# # utility for writing a csv row
# def writerow(f, row):
#     for i in row[:-1]:
#         f.write(str(i) + ",")
#     f.write(str(row[-1]) + "\n")


# with open(filename, "a") as f:
#     header = ["magx", "magy", "magz", "gyrox", "gyroy", "gyroz", "accelx", "accely", "accelz", "sensortime"]
#     writerow(f, header)

# #################### Collect Data ####################

# rate = 1/10 # seconds
# # always with "a" for append
# with open(filename, "a") as f:
#     print("Begin Record")
#     # RECORD FOR 10 HOURS
#     t0 = time.time()
#     while (time.time() - t0) < 3600*10:

#         t1 = time.time()
#         led.brightness = 0.1
#         # Each returns a tuple, so adding them is the same as appending them to each other
#         data = bmx.mag + bmx.gyro + bmx.accel + (bmx.sensortime,)

#         writerow(f, data)

#         led.brightness = 0.01

#         if (time.time() - t0)%60 < 0.11:
#             print("Recorded for {} minutes".format((time.time() - t0)/60))

#         # Wait if necessary to keep rate consistent
#         dif = time.time() - t1
#         if dif < rate:
#             time.sleep(rate-dif)

# print("DONE")