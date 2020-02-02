import time
try:
    import struct
except ImportError:
    import ustruct as struct

from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_bus_device.spi_device import SPIDevice
from micropython import const

# Chip ID
BMX160_CHIP_ID = const(0xD8)

# Soft reset command
BMX160_SOFT_RESET_CMD      = const(0xb6)
BMX160_SOFT_RESET_DELAY    = const(0.001)

# Command
BMX160_COMMAND_REG_ADDR    = const(0x7E)

# BMX160 Register map
BMX160_CHIP_ID_ADDR        = const(0x00)
BMX160_ERROR_REG_ADDR      = const(0x02)
BMX160_PMU_STATUS_ADDR     = const(0x03)
BMX160_SENSOR_TIME_ADDR    = const(0x18)
BMX160_MAG_DATA_ADDR       = const(0x04)
BMX160_GYRO_DATA_ADDR      = const(0x0C)
BMX160_ACCEL_DATA_ADDR     = const(0x12)
BMX160_STATUS_ADDR         = const(0x1B)
BMX160_INT_STATUS_ADDR     = const(0x1C)
BMX160_FIFO_LENGTH_ADDR    = const(0x22)
BMX160_FIFO_DATA_ADDR      = const(0x24)
BMX160_ACCEL_CONFIG_ADDR   = const(0x40)
BMX160_ACCEL_RANGE_ADDR    = const(0x41)
BMX160_GYRO_CONFIG_ADDR    = const(0x42)
BMX160_GYRO_RANGE_ADDR     = const(0x43)
BMX160_MAG_ODR_ADDR        = const(0x44)
BMX160_FIFO_DOWN_ADDR      = const(0x45)
BMX160_FIFO_CONFIG_0_ADDR  = const(0x46)
BMX160_FIFO_CONFIG_1_ADDR  = const(0x47)
# BMX160_MAG_IF_0_ADDR       = const(0x4B)
BMX160_MAG_IF_0_ADDR       = const(0x4C)
BMX160_MAG_IF_1_ADDR       = const(0x4D)
BMX160_MAG_IF_2_ADDR       = const(0x4E)
BMX160_MAG_IF_3_ADDR       = const(0x4F)
BMX160_INT_ENABLE_0_ADDR   = const(0x50)
BMX160_INT_ENABLE_1_ADDR   = const(0x51)
BMX160_INT_ENABLE_2_ADDR   = const(0x52)
BMX160_INT_OUT_CTRL_ADDR   = const(0x53)
BMX160_INT_LATCH_ADDR      = const(0x54)
BMX160_INT_MAP_0_ADDR      = const(0x55)
BMX160_INT_MAP_1_ADDR      = const(0x56)
BMX160_INT_MAP_2_ADDR      = const(0x57)
BMX160_INT_DATA_0_ADDR     = const(0x58)
BMX160_INT_DATA_1_ADDR     = const(0x59)
BMX160_INT_LOWHIGH_0_ADDR  = const(0x5A)
BMX160_INT_LOWHIGH_1_ADDR  = const(0x5B)
BMX160_INT_LOWHIGH_2_ADDR  = const(0x5C)
BMX160_INT_LOWHIGH_3_ADDR  = const(0x5D)
BMX160_INT_LOWHIGH_4_ADDR  = const(0x5E)
BMX160_INT_MOTION_0_ADDR   = const(0x5F)
BMX160_INT_MOTION_1_ADDR   = const(0x60)
BMX160_INT_MOTION_2_ADDR   = const(0x61)
BMX160_INT_MOTION_3_ADDR   = const(0x62)
BMX160_INT_TAP_0_ADDR      = const(0x63)
BMX160_INT_TAP_1_ADDR      = const(0x64)
BMX160_INT_ORIENT_0_ADDR   = const(0x65)
BMX160_INT_ORIENT_1_ADDR   = const(0x66)
BMX160_INT_FLAT_0_ADDR     = const(0x67)
BMX160_INT_FLAT_1_ADDR     = const(0x68)
BMX160_FOC_CONF_ADDR       = const(0x69)
BMX160_CONF_ADDR           = const(0x6A)

BMX160_ACCEL_BW_NORMAL_AVG4 = const(0x02)
BMX160_GYRO_BW_NORMAL_MODE  = const(0x02)

BMX160_SELF_TEST_ADDR                = const(0x6D)
# Self test configurations
BMX160_ACCEL_SELF_TEST_CONFIG        = const(0x2C)
BMX160_ACCEL_SELF_TEST_POSITIVE_EN   = const(0x0D)
BMX160_ACCEL_SELF_TEST_NEGATIVE_EN   = const(0x09)
BMX160_ACCEL_SELF_TEST_LIMIT         = const(8192)

# Power mode settings
# Accel power mode
BMX160_ACCEL_NORMAL_MODE             = const(0x11)
BMX160_ACCEL_LOWPOWER_MODE           = const(0x12)
BMX160_ACCEL_SUSPEND_MODE            = const(0x10)

# Gyro power mode
BMX160_GYRO_SUSPEND_MODE             = const(0x14)
BMX160_GYRO_NORMAL_MODE              = const(0x15)
BMX160_GYRO_FASTSTARTUP_MODE         = const(0x17)

# Mag power mode
BMX160_MAG_SUSPEND_MODE              = const(0x18)
BMX160_MAG_NORMAL_MODE               = const(0x19)
BMX160_MAG_LOWPOWER_MODE             = const(0x1A)

# Accel Range
BMX160_ACCEL_RANGE_2G                = const(0x03)
BMX160_ACCEL_RANGE_4G                = const(0x05)
BMX160_ACCEL_RANGE_8G                = const(0x08)
BMX160_ACCEL_RANGE_16G               = const(0x0C)

BMX160_ACCEL_RANGE_CONSTANTS = [BMX160_ACCEL_RANGE_16G,
                                BMX160_ACCEL_RANGE_8G,
                                BMX160_ACCEL_RANGE_4G,
                                BMX160_ACCEL_RANGE_2G]
BMX160_ACCEL_RANGE_VALUES = [16, 8, 4, 2]


# Gyro Range
BMX160_GYRO_RANGE_2000_DPS           = const(0x00)
BMX160_GYRO_RANGE_1000_DPS           = const(0x01)
BMX160_GYRO_RANGE_500_DPS            = const(0x02)
BMX160_GYRO_RANGE_250_DPS            = const(0x03)
BMX160_GYRO_RANGE_125_DPS            = const(0x04)

BMX160_GYRO_RANGE_CONSTANTS = [BMX160_GYRO_RANGE_2000_DPS,
                               BMX160_GYRO_RANGE_1000_DPS,
                               BMX160_GYRO_RANGE_500_DPS,
                               BMX160_GYRO_RANGE_250_DPS,
                               BMX160_GYRO_RANGE_125_DPS]
BMX160_GYRO_RANGE_VALUES = [2000, 1000, 500, 250, 125]

# Delay in ms settings
BMX160_ACCEL_DELAY                   = const(0.005)
BMX160_GYRO_DELAY                    = const(0.0081)
BMX160_ONE_MS_DELAY                  = const(0.001)
BMX160_MAG_COM_DELAY                 = const(0.001)
BMX160_GYRO_SELF_TEST_DELAY          = const(0.002)
BMX160_ACCEL_SELF_TEST_DELAY         = const(0.005)

# Output Data Rate settings
# Accel Output data rate
BMX160_ACCEL_ODR_RESERVED            = const(0x00)
BMX160_ACCEL_ODR_0_78HZ              = const(0x01)
BMX160_ACCEL_ODR_1_56HZ              = const(0x02)
BMX160_ACCEL_ODR_3_12HZ              = const(0x03)
BMX160_ACCEL_ODR_6_25HZ              = const(0x04)
BMX160_ACCEL_ODR_12_5HZ              = const(0x05)
BMX160_ACCEL_ODR_25HZ                = const(0x06)
BMX160_ACCEL_ODR_50HZ                = const(0x07)
BMX160_ACCEL_ODR_100HZ               = const(0x08)
BMX160_ACCEL_ODR_200HZ               = const(0x09)
BMX160_ACCEL_ODR_400HZ               = const(0x0A)
BMX160_ACCEL_ODR_800HZ               = const(0x0B)
BMX160_ACCEL_ODR_1600HZ              = const(0x0C)
BMX160_ACCEL_ODR_RESERVED0           = const(0x0D)
BMX160_ACCEL_ODR_RESERVED1           = const(0x0E)
BMX160_ACCEL_ODR_RESERVED2           = const(0x0F)

BMX160_ACCEL_ODR_CONSTANTS = [BMX160_ACCEL_ODR_1600HZ,
                              BMX160_ACCEL_ODR_800HZ,
                              BMX160_ACCEL_ODR_400HZ,
                              BMX160_ACCEL_ODR_200HZ,
                              BMX160_ACCEL_ODR_100HZ,
                              BMX160_ACCEL_ODR_50HZ,
                              BMX160_ACCEL_ODR_25HZ,
                              BMX160_ACCEL_ODR_12_5HZ,
                              BMX160_ACCEL_ODR_6_25HZ,
                              BMX160_ACCEL_ODR_3_12HZ,
                              BMX160_ACCEL_ODR_1_56HZ,
                              BMX160_ACCEL_ODR_0_78HZ]
BMX160_ACCEL_ODR_VALUES = [1600, 800, 400, 200, 100, 50, 25, 12.5, 6.25, 3.12, 1.56, 0.78]

# Gyro Output data rate
BMX160_GYRO_ODR_RESERVED             = const(0x00)
BMX160_GYRO_ODR_25HZ                 = const(0x06)
BMX160_GYRO_ODR_50HZ                 = const(0x07)
BMX160_GYRO_ODR_100HZ                = const(0x08)
BMX160_GYRO_ODR_200HZ                = const(0x09)
BMX160_GYRO_ODR_400HZ                = const(0x0A)
BMX160_GYRO_ODR_800HZ                = const(0x0B)
BMX160_GYRO_ODR_1600HZ               = const(0x0C)
BMX160_GYRO_ODR_3200HZ               = const(0x0D)

BMX160_GYRO_ODR_CONSTANTS = [BMX160_GYRO_ODR_3200HZ,
                             BMX160_GYRO_ODR_1600HZ,
                             BMX160_GYRO_ODR_800HZ,
                             BMX160_GYRO_ODR_400HZ,
                             BMX160_GYRO_ODR_200HZ,
                             BMX160_GYRO_ODR_100HZ,
                             BMX160_GYRO_ODR_50HZ]
BMX160_GYRO_ODR_VALUES = [3200, 1600, 800, 400, 200, 100, 50]

# Auxiliary sensor Output data rate
BMX160_MAG_ODR_RESERVED              = const(0x00)
BMX160_MAG_ODR_0_78HZ                = const(0x01)
BMX160_MAG_ODR_1_56HZ                = const(0x02)
BMX160_MAG_ODR_3_12HZ                = const(0x03)
BMX160_MAG_ODR_6_25HZ                = const(0x04)
BMX160_MAG_ODR_12_5HZ                = const(0x05)
BMX160_MAG_ODR_25HZ                  = const(0x06)
BMX160_MAG_ODR_50HZ                  = const(0x07)
BMX160_MAG_ODR_100HZ                 = const(0x08)
BMX160_MAG_ODR_200HZ                 = const(0x09)
BMX160_MAG_ODR_400HZ                 = const(0x0A)
BMX160_MAG_ODR_800HZ                 = const(0x0B)

# Accel, gyro and aux. sensor length and also their combined length definitions in FIFO
BMX160_FIFO_G_LENGTH                 = const(6)
BMX160_FIFO_A_LENGTH                 = const(6)
BMX160_FIFO_M_LENGTH                 = const(8)
BMX160_FIFO_GA_LENGTH                = const(12)
BMX160_FIFO_MA_LENGTH                = const(14)
BMX160_FIFO_MG_LENGTH                = const(14)
BMX160_FIFO_MGA_LENGTH               = const(20)

# I2C address
BMX160_I2C_ADDR            = const(0x68)
BMX160_I2C_ALT_ADDR        = const(0x69)  # alternate address
# Interface settings
BMX160_SPI_INTF            = const(1)
BMX160_I2C_INTF            = const(0)
BMX160_SPI_RD_MASK         = const(0x80)
BMX160_SPI_WR_MASK         = const(0x7F)

# Error related
BMX160_OK                  = const(0)

class BMX160:
    """
    Driver for the BMX160 accelerometer, magnetometer, gyroscope.

    In the buffer, bytes are allocated as follows:
        - mag 0-5
        - rhall 6-7 (not relevant?)
        - gyro 8-13
        - accel 14-19
        - sensor time 20-22
    """

    _BUFFER = bytearray(40)
    _smallbuf = bytearray(6)

    _gyro_bandwidth = NORMAL
    _gyro_powermode = NORMAL
    _gyro_odr = 25    # Hz
    _gyro_range = 250 # deg/sec

    _accel_bandwidth = NORMAL
    _accel_powermode = NORMAL
    _accel_odr = 25  # Hz
    _accel_range = 2 # g

    _mag_bandwidth = NORMAL
    _mag_powermode = NORMAL
    _mag_odr = 25    # Hz
    _mag_range = 250 # deg/sec


    def __init__(self):
        # soft reset & reboot
        self.write_u8(BMX160_COMMAND_REG_ADDR, BMX160_SOFT_RESET_CMD)
        time.sleep(BMX160_SOFT_RESET_DELAY)
        # Check ID registers.
        ID = self.read_u8(BMX160_CHIP_ID_ADDR)
        if ID != BMX160_CHIP_ID:
            raise RuntimeError('Could not find BMX160, check wiring!')

        # set the default settings
        self.init_gyro()
        self.init_accel()
        self.init_mag()
        self.apply_sensor_params()


    ######################## SENSOR API ########################

    def read_all(self): return self.read_bytes(BMX160_MAG_DATA_ADDR, 20, self._BUFFER)

    def query_error(self): return self.read_u8(BMX160_ERROR_REG_ADDR)

    ### ACTUAL API
    @property
    def gyro(self):  return decode_sensor(self.gyro_raw(), self._gyro_range)

    @property
    def accel(self): return decode_sensor(self.accel_raw(), self._accel_range)

    @property
    def mag(self):   return decode_sensor(self.mag_raw(), self._mag_range)

    @property
    def sensortime(self):
        tbuf = self.sensortime_raw()
        t0, t1, t2 = tbuf[:3]
        t = (t2 << 16) | (t1 << 8) | t0
        t *= 0.000039 # the time resolution is 39 microseconds
        return t


    # NOTE, these share a buffer! Can't call two in a row! Either make a wrapper for a buffer slice
    # to allow partial passing or copy the buffer to return or completely hide this API
    def gyro_raw(self):  return self.read_bytes(BMX160_GYRO_DATA_ADDR, 6, self._smallbuf)
    def accel_raw(self): return self.read_bytes(BMX160_ACCEL_DATA_ADDR, 6, self._smallbuf)
    def mag_raw(self):   return self.read_bytes(BMX160_MAG_DATA_ADDR, 6, self._smallbuf)
    def sensortime_raw(self):  return self.read_bytes(BMX160_SENSOR_TIME_ADDR, 3, self._smallbuf)

    ######################## SETTINGS RELATED ########################

    ############## GYROSCOPE SETTINGS  ##############
    # NOTE still missing BW / OSR config, but those are more complicated

    def init_gyro(self):
        # BW doesn't have an interface yet
        self.write_u8(BMX160_GYRO_CONFIG_ADDR, BMX160_GYRO_BW_NORMAL_MODE)
        # the rest do
        self._gyro_bwmode = BMX160_GYRO_BW_NORMAL_MODE
        self.gyro_range = 500
        self.gyro_odr = 25
        self.gyro_powermode = BMX160_GYRO_NORMAL_MODE

    @property
    def gyro_range(self):
        return self._gyro_range

    @gyro_range.setter
    def gyro_range(self, range):
        """
        Set the range of the gyroscope. The possible ranges are
        2000, 1000, 500, 250, and 125 degree/second. Note, setting a value between the possible ranges
        will round *downwards*. A value of e.g. 250 means the sensor can measure +/-250 deg/sec
        """
        res = self.generic_setter(range, BMX160_GYRO_RANGE_VALUES,
                                  BMX160_GYRO_RANGE_CONSTANTS,
                                  BMX160_GYRO_RANGE_ADDR,
                                  "gyroscope range")
        if res != None:
            self._gyro_range = res

    @property
    def gyro_odr(self):
        return self._gyro_odr

    @gyro_odr.setter
    def gyro_odr(self, odr):
        """
        Set the output data rate of the gyroscope. The possible ODRs are 1600, 800, 400, 200, 100,
        50, 25, 12.5, 6.25, 3.12, 1.56, and 0.78 Hz. Note, setting a value between the listed ones
        will round *downwards*.
        """
        res = self.generic_setter(odr, BMX160_GYRO_ODR_VALUES,
                                  BMX160_GYRO_ODR_CONSTANTS,
                                  BMX160_GYRO_CONFIG_ADDR,
                                  "gyroscope odr")
        if res != None:
            self._gyro_odr = res

    @property
    def gyro_powermode(self):
        return self._gyro_powermode

    @gyro_powermode.setter
    def gyro_powermode(self, powermode):
        """
        Set the power mode of the gyroscope. Unlike other setters, this one has to directly take the
        BMX160-const associated with the power mode. The possible modes are:
        `BMX160_GYRO_SUSPEND_MODE`
        `BMX160_GYRO_NORMAL_MODE`
        `BMX160_GYRO_FASTSTARTUP_MODE`
        """
        if powermode not in BMX160_GYRO_MODES:
            warn("Unknown gyroscope powermode: " + str(powermode))
            return

        self.write_u8(BMX160_COMMAND_REG_ADDR, powermode)
        if self.query_error() == 0:
            self._gyro_powermode = powermode
        else:
            settingswarning("gyroscope power mode")

        # NOTE: this delay is a worst case. If we need repeated switching
        # we can choose the delay on a case-by-case basis.
        time.sleep(BMX160_GYRO_DELAY)


    ############## ACCELEROMETER SETTINGS  ##############

    def init_accel(self):
        # BW doesn't have an interface yet
        self.write_u8(BMX160_ACCEL_CONFIG_ADDR, BMX160_ACCEL_BW_NORMAL_AVG4)
        # the rest do
        self._accel_bwmode = BMX160_ACCEL_BW_NORMAL_AVG4
        self.accel_range = 2
        self.accel_odr = 25
        self.accel_powermode = BMX160_ACCEL_NORMAL_MODE

    @property
    def accel_range(self):
        return self._accel_range

    @accel_range.setter
    def accel_range(self, range):
         """
        Set the range of the accelerometer. The possible ranges are 16, 8, 4, and 2 Gs.
        Note, setting a value between the possible ranges will round *downwards* unless it is below 2.
        A value of e.g. 2 means the sensor can measure +/-2 G
        """
        res = self.generic_setter(range, BMX160_ACCEL_RANGE_VALUES,
                                  BMX160_ACCEL_RANGE_CONSTANTS,
                                  BMX160_ACCEL_RANGE_ADDR,
                                  "accelerometer range")
        if res != None:
            self._accel_range = res

    @property
    def accel_odr(self):
        return self._accel_odr

    @accel_odr.setter
    def accel_odr(self, odr):
        res = self.generic_setter(odr, BMX160_ACCEL_ODR_VALUES,
                                  BMX160_ACCEL_ODR_CONSTANTS,
                                  BMX160_ACCEL_CONFIG_ADDR,
                                  "accelerometer odr")
        if res != None:
            self._accel_odr = res

    @property
    def accel_powermode(self):
        return self._accel_powermode

    @accel_powermode.setter
    def accel_powermode(self, powermode):
        """
        Set the power mode of the accelerometer. Unlike other setters, this one has to directly take the
        BMX160-const associated with the power mode. The possible modes are:
        `BMI160_ACCEL_NORMAL_MODE`
        `BMI160_ACCEL_LOWPOWER_MODE`
        `BMI160_ACCEL_SUSPEND_MODE`
        """
        if powermode not in BMX160_ACCEL_MODES:
            warn("Unknown accelerometer powermode: " + str(powermode))
            return

        self.write_u8(BMX160_COMMAND_REG_ADDR, powermode)
        if self.query_error() == 0:
            self._accel_powermode = powermode
        else:
            settingswarning("accelerometer power mode")

        # NOTE: this delay is a worst case. If we need repeated switching
        # we can choose the delay on a case-by-case basis.
        time.sleep(BMX160_ACCEL_DELAY)

    ############## MAGENTOMETER SETTINGS  ##############

    def init_mag(self):
        # see pg 25 of: https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMX160-DS000.pdf
        self.write_u8(BMX160_COMMAND_REG_ADDR, BMX160_MAG_NORMAL_MODE)
        time.sleep(0.00065) # datasheet says wait for 650microsec
        self.write_u8(BMX160_MAG_IF_0_ADDR, 0x80)
        # put mag into sleep mode
        self.write_u8(BMX160_MAG_IF_3_ADDR, 0x01)
        self.write_u8(BMX160_MAG_IF_2_ADDR, 0x4B)
        # set x-y to regular power preset
        self.write_u8(BMX160_MAG_IF_3_ADDR, 0x04)
        self.write_u8(BMX160_MAG_IF_2_ADDR, 0x51)
        # set z to regular preset
        self.write_u8(BMX160_MAG_IF_3_ADDR, 0x0E)
        self.write_u8(BMX160_MAG_IF_2_ADDR, 0x52)
        # prepare MAG_IF[1-3] for mag_if data mode
        self.write_u8(BMX160_MAG_IF_3_ADDR, 0x02)
        self.write_u8(BMX160_MAG_IF_2_ADDR, 0x4C)
        self.write_u8(BMX160_MAG_IF_1_ADDR, 0x42)
        # Set ODR to 25 Hz
        self.write_u8(BMX160_MAG_ODR_ADDR, BMX160_MAG_ODR_25HZ)
        self.write_u8(BMX160_MAG_IF_0_ADDR, 0x00)
        # put in low power mode.
        self.write_u8(BMX160_COMMAND_REG_ADDR, BMX160_MAG_LOWPOWER_MODE)
        time.sleep(0.1) # takes this long to warm up (empirically)


    ## UTILS:
    def decode_sensor(arr, range):
        x = (arr[1] << 8) | arr[0]
        y = (arr[3] << 8) | arr[2]
        z = (arr[5] << 8) | arr[4]

        # divide by typemax(Int16) and multiply by range
        x *= range / 32768.0
        y *= range / 32768.0
        z *= range / 32768.0
        # NOTE: This may be the wrong conversion! It might need to be something like (x + typemin(Int16)) / typemin(Int16)

        return (x, y, z)

    def find_nearest_valid(self, desired, possible_values, bmx_values):
        # This line finds the first value less than or equal to the desired value (and its index).
        # res = None if the desired value is smaller than all elements of the list.
        res = next(filter(lambda x: (desired >= x[1]), enumerate(possible_values)), None)
        if res == None:
            val = possible_values[-1]
            bmxconst = bmx_values[-1]
        else:
            val = possible_values[res[0]]
            bmxconst = bmx_values[res[0]]

        return val, bmxconst

    def generic_setter(self, desired, possible_values, bmx_constants, config_addr, warning_interp = ""):
        rounded, bmxconst = self.find_nearest_valid(desired, possible_values, bmx_constants)
        self.write_u8(config_addr, bmxconst)
        if self.query_error() == BMX160_OK:
            return rounded
        else:
            settingswarning(warning_interp)

    def settingswarning("interp"):
        if interp == "":
                interp += " "
        warn("BMX160 error occurred during " + interp +
             "setting change. Setting not successfully changed and BMX160 may be in error state.")


class BMX160_I2C(BMX160):
    """Driver for the BMX160 connect over I2C."""

    def __init__(self, i2c):

        try:
            self.i2c_device = I2CDevice(i2c, BMX160_I2C_ADDR)
        except:
            self.i2c_device = I2CDevice(i2c, BMX160_I2C_ALT_ADDR)

        super().__init__()

    def read_u8(self, address):
        with self.i2c_device as i2c:
            self._BUFFER[0] = address & 0xFF
            i2c.write_then_readinto(self._BUFFER, self._BUFFER, out_end=1, in_start=1, in_end=2)
        return self._BUFFER[1]

    def read_bytes(self, address, count, buf):
        with self.i2c_device as i2c:
            buf[0] = address & 0xFF
            i2c.write_then_readinto(buf, buf, out_end=1, in_end=count)
        return buf

    def write_u8(self, address, val):
        with self.i2c_device as i2c:
            self._BUFFER[0] = address & 0xFF
            self._BUFFER[1] = val & 0xFF
            i2c.write(self._BUFFER, end=2, stop=True)


class BMX160_SPI(BMX160):
    """Driver for the BMX160 connect over SPI."""
    def __init__(self, spi, cs):
        self.i2c_device = SPIDevice(spi, cs)
        super().__init__()

    def read_u8(self, address):
        with self.i2c_device as spi:
            self._BUFFER[0] = (address | 0x80) & 0xFF
            spi.write(self._BUFFER, end=1)
            spi.readinto(self._BUFFER, end=1)
        return self._BUFFER[0]

    def read_bytes(self, address, count, buf):
        with self.i2c_device as spi:
            buf[0] = (address | 0x80) & 0xFF
            spi.write(buf, end=1)
            spi.readinto(buf, end=count)
        return buf

    def write_u8(self, address, val):
        with self.i2c_device as spi:
            self._BUFFER[0] = (address & 0x7F) & 0xFF
            self._BUFFER[1] = val & 0xFF
            spi.write(self._BUFFER, end=2)

