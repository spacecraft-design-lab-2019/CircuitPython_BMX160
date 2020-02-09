from pycubed import cubesat

from time import sleep
import struct
import BMX160
from micropython import const

bmx = BMX160.BMX160_I2C(cubesat.i2c)

sleep(1)

bbuf = bytearray(6)
abuf = bytearray(2)

S2G=const(16384) # accelerometer sensitivity. See Section 1.2, Table 2
SCALAR = S2G*0.101971621 # 1 m/s^2 = 0.101971621 g
SCALAR_TEMP = 0.5**9
while True:
    sleep(0.5)
    bmx.read_bytes(0x12,6,bbuf)

    # using struct.unpack
    x=struct.unpack('<h',bbuf[0:2])[0]/SCALAR
    y=struct.unpack('<h',bbuf[2:4])[0]/SCALAR
    z=struct.unpack('<h',bbuf[4:6])[0]/SCALAR

    # or you could do it the way you were doing it
    # z=(bbuf[4] | (bbuf[5]<<8))/SCALAR

    # temperature is different (also make sure gyro is in normal power mode)
    bmx.read_bytes(0x20,2,abuf)
    t=(struct.unpack('<h',abuf)[0]*SCALAR_TEMP)+23

    # print everything for manual method
    print('x:{:.2f}\ty:{:.2f}\tz:{:.2f}\tt:{:.2f}'.format(x,y,z,t))

    # or do it the fancy-library way... :)
    print('xyz{}, t:{}'.format(bmx.acceleration, bmx.temperature))
