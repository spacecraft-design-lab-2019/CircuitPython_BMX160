import time
import board
import busio, bmx160

i2c = busio.I2C(board.SCL, board.SDA)

bmx = bmx160.BMX160_I2C(i2c)

print(hex(bmx.read_u8(bmx160.BMX160_CHIP_ID_ADDR)))

# for i in range(0x7E):
#     print(hex(i),hex(bmx.read_u8(i)))

print('PMU_STATUS:\t',hex(bmx.read_u8(0x03)))
bmx.write_u8(address=0x7E,val=0x11) # put accel into normal power
bmx.write_u8(address=0x7E,val=0x15) # put gyr into normal power
bmx.write_u8(address=0x7E,val=0x19) # put mag into normal power
bmx.write_u8(address=0x7E,val=0xA0) # writes NVM backed registers into NVM
bmx.write_u8(address=0x7E,val=0xB0) # clear FIFO
bmx.write_u8(address=0x7E,val=0xB1) # reset interrupts
print('PMU_STATUS:\t',hex(bmx.read_u8(0x03)))


bmx.read_all()
for b in bmx._BUFFER:
    print(b, end = ", ")

for i in range(10):
    print()
    print("gyro:", bmx.gyro())
    print("accel:", bmx.accel())
    print("mag:", bmx.mag())
    time.sleep(1)