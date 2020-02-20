# CircuitPython_BMX160
CircuitPython driver for BMX160

For reference, see the datasheet for the device [here](https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMX160-DS000.pdf)

## Example setup and usage:

```python
import time
import board, busio
import bmx160

# set up BMX160 through I2C # note: also supports SPI communication through the BMX160_SPI class
i2c = busio.I2C(board.SCL1, board.SDA1) 
bmx = bmx160.BMX160_I2C(i2c)  

# conservative warm-up time
time.sleep(0.1) 

# Just call e.g. bmx.gyro to read the gyro value
print("gyroscope:", bmx.gyro)
print("accelerometer:", bmx.accel)
print("magnetometer:", bmx.mag)
```

## Sensors

A call to e.g. `bmx.gyro` returns a tuple: `(gyro_x, gyro_y, gyro_z)`.

#### Gyroscope
- getter: `bmx.gyro`
- units: °/sec
- default range: ±250 °/sec
- default data-rate: 25 Hz

#### Magnetometer
- getter: `bmx.mag`
- units: µT
- fixed range: ±1150µT (x/y) ±2500µT (z) (see Section 1.2 Table 4)
- default data-rate: 25 Hz
- default mode: low-power (see Section 2.2.1.2 and Table 11)

#### Accelerometer
- getter: `bmx.accel`
- units: m/s (note: this differs from the .c implementation, which returns in g)
- default range: ±2g
- default data-rate: 25 Hz

#### Temperature Sensor
- getter: `bmx.temp` / `bmx.temperature`
- units: °C

#### Timer
- resolution: 39µs
- resets every 654.311385s (see section 2.3.1 Table 12)

#### Other things
- Access error register: `bmx.error_status` returns a binary string following Section 2.11.2
- PMU (power management unit) mode fo each device with `bmx.status_acc_pmu`, `bmx.status_gyr_pmu`, `bmx.status_mag_pmu`
- Status register: `bmx.status` returns a binary string following Section 2.11.6, individual bits of which can also be gotten (as booleans) with getters named after the entries in that table. E.g. `bmx.drdy_acc`
- Note: Right now, encountering an *chip error* while e.g. changing settings, simply prints a warning.
