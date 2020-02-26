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
led[0] = [255, 255, 50]
led.brightness = 0.01

################### set up BMX160 through I2C ###################

i2c = busio.I2C(board.SCL1, board.SDA1)
bmx = bmx160.BMX160_I2C(i2c)
time.sleep(0.05)

################### set up SD card through SPI  ###################

spi = busio.SPI(board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs_sd = DigitalInOut(board.CS_SD)
sdcard = adafruit_sdcard.SDCard(spi, cs_sd)

# Use the filesystem as normal. Files are under "/sd"
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
sys.path.append("/sd")

#################### SET UP THE FILE (new one if one already exists) ####################

filename = '/sd/sensordata1.csv'
badname = True
while badname:
    try:
        with open(filename) as f:
            # Set a new filename, since this one already exists
            fl = list(filename)
            fl[-5] = str(int(fl[-5]) + 1)
            filename = "".join(fl)
    except Exception as e:
        print(type(e))
        badname = False

print("Saving into {}".format(filename))
# utility for writing a csv row
def writerow(f, row):
    for i in row[:-1]:
        f.write(str(i) + ",")
    f.write(str(row[-1]) + "\n")


with open(filename, "a") as f:
    header = ["magx", "magy", "magz", "gyrox", "gyroy", "gyroz", "accelx", "accely", "accelz", "sensortime", "dt"]
    writerow(f, header)

#################### Collect Data ####################

rate = 1/20 # seconds
# always with "a" for append
with open(filename, "a") as f:
    print("Begin Record")
    led[0] = [20, 255, 50]
    # RECORD FOR 12 HOURS
    t0 = time.monotonic()
    while (time.monotonic() - t0) < 3600*12:

        t1 = time.monotonic()
        led[0] = [20, 255, 50]
        # Each returns a tuple, so adding them is the same as appending them to each other
        data = bmx.mag + bmx.gyro + bmx.accel + (bmx.sensortime,) + (t1-t0,)

        writerow(f, data)

        led[0] = [255, 255, 50]


        if (t1 - t0)%60 < (1.05*rate):
            print("Recorded for {} minutes".format((t1 - t0)/60))

        # Wait if necessary to keep rate consistent
        dif = time.monotonic() - t1
        if dif < rate:
            time.sleep(rate-dif)

led[0] = [20, 20, 255]
print("DONE")