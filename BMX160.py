import time
try:
    import struct
except ImportError:
    import ustruct as struct

from adafruit_bus_device.i2c_device import I2CDevice
from micropython import const

# Chip ID
BMX160_CHIP_ID = const(0xD8)

# Soft reset command
BMX160_SOFT_RESET_CMD      = const(0xb6)
BMX160_SOFT_RESET_DELAY_MS = 0.001

# Command
BMX160_COMMAND_REG_ADDR    = const(0x7E)

# BMX160 Register map
BMX160_CHIP_ID_ADDR        = const(0x00)
BMX160_ERROR_REG_ADDR      = const(0x02)
BMX160_PMU_STATUS_ADDR     = const(0x03)
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
BMX160_MAG_IF_0_ADDR       = const(0x4B)
BMX160_MAG_IF_1_ADDR       = const(0x4C)
BMX160_MAG_IF_2_ADDR       = const(0x4D)
BMX160_MAG_IF_3_ADDR       = const(0x4E)
BMX160_MAG_IF_4_ADDR       = const(0x4F)
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
BMX160_ACCEL_ODR_100HZ      = const(0x08)
BMX160_GYRO_ODR_100HZ       = const(0x08)
BMX160_ACCEL_RANGE_2G       = const(0x03)
BMX160_GYRO_RANGE_2000_DPS  = const(0x00)

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

# Delay in ms settings
BMX160_ACCEL_DELAY_MS                = const(5)
BMX160_GYRO_DELAY_MS                 = const(81)
BMX160_ONE_MS_DELAY                  = const(1)
BMX160_MAG_COM_DELAY                 = const(10)
BMX160_GYRO_SELF_TEST_DELAY          = const(20)
BMX160_ACCEL_SELF_TEST_DELAY         = const(50)

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

# Auxiliary sensor Output data rate
BMX160_AUX_ODR_RESERVED              = const(0x00)
BMX160_AUX_ODR_0_78HZ                = const(0x01)
BMX160_AUX_ODR_1_56HZ                = const(0x02)
BMX160_AUX_ODR_3_12HZ                = const(0x03)
BMX160_AUX_ODR_6_25HZ                = const(0x04)
BMX160_AUX_ODR_12_5HZ                = const(0x05)
BMX160_AUX_ODR_25HZ                  = const(0x06)
BMX160_AUX_ODR_50HZ                  = const(0x07)
BMX160_AUX_ODR_100HZ                 = const(0x08)
BMX160_AUX_ODR_200HZ                 = const(0x09)
BMX160_AUX_ODR_400HZ                 = const(0x0A)
BMX160_AUX_ODR_800HZ                 = const(0x0B)

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

    def __init__(self):
        # soft reset & reboot
        self.write_u8(BMX160_COMMAND_REG_ADDR, BMX160_SOFT_RESET_CMD)
        time.sleep(BMX160_SOFT_RESET_DELAY_MS)
        # Check ID registers.
        ID = self.read_u8(BMX160_CHIP_ID_ADDR)
        if ID != BMX160_CHIP_ID:
            raise RuntimeError('Could not find BMX160, check wiring!')

        # set the default settings
        self.settings = self.default_settings()
        self.apply_sensor_params()


    def read_all(self):
        self.read_bytes(BMX160_MAG_DATA_ADDR, 20, self._BUFFER)

    def gyro(self):
        self.read_bytes(BMX160_GYRO_DATA_ADDR, 6, self._smallbuf)
        return decode_sensor(self._smallbuf)

    def mag(self):
        self.read_bytes(BMX160_MAG_DATA_ADDR, 6, self._smallbuf)
        return decode_sensor(self._smallbuf)

    def accel(self):
        self.read_bytes(BMX160_ACCEL_DATA_ADDR, 6, self._smallbuf)
        return decode_sensor(self._smallbuf)

    def query_error(self):
        return self.read_u8(BMX160_ERROR_REG_ADDR)

    def clear_settings(self):
        self.setting.clear()

    def set_sensor_param(self, sensor, param, value):
        """
        Set any sensor configuration parameter. `sensor` and `param` should be strings
        like ("mag", "gyro", "accel"), and ("range", "config"). Case doesn't matter for these strings.
        """
        assert sensor.lower() in ("mag", "gyro", "accel")

        if param.lower() == "range":
            registername = "BMX160_" + sensor.upper() + "_RANGE_ADDR"
        else:
            registername = "BMX160_COMMAND_REG_ADDR"

        if registername in globals():
            register = globals()[registername]
            self.write_u8(register, value)
        else:
            print("WARNING: no register found corresponding to {}".format(registername))

    def apply_sensor_params(self, settings = None):
        if settings == None:
            settings = self.settings

        params = self.default_settings()
        params.update(settings)

        for key, val in params["accel"].items():
            self.set_sensor_param("accel", key, val)

        for key, val in params["gyro"].items():
            self.set_sensor_param("gyro", key, val)

        # for key, val in params["mag"]:
            # self.set_sensor_param("mag", key, val)

    def default_settings(self):
        """
        Basically copied from the C version.
        """
        accel_settings = {
                          "bw": BMX160_ACCEL_BW_NORMAL_AVG4,
                          "odr": BMX160_ACCEL_ODR_100HZ,
                          "power": BMX160_ACCEL_NORMAL_MODE,
                          # "range": BMX160_ACCEL_RANGE_2G
                          }
        gyro_settings = {
                         "bw": BMX160_GYRO_BW_NORMAL_MODE,
                         "odr": BMX160_GYRO_ODR_100HZ,
                         "power": BMX160_GYRO_NORMAL_MODE,
                         # "range": BMX160_GYRO_RANGE_2000_DPS
                         }

        mag_settings = {
                         "bw": BMX160_MAG_BW_NORMAL_MODE,
                         "odr": BMX160_MAG_ODR_100HZ,
                         "power": BMX160_MAG_NORMAL_MODE,
                         # "range": BMX160_GYRO_RANGE_2000_DPS
                         }

        return {"accel": accel_settings, "gyro": gyro_settings, "mag": mag_settings}




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
        return self._BUFFER[address]

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
        self.i2c_device = spi_device.SPIDevice(spi, cs)
        super().__init__()

    def read_u8(self, address):
        with self.i2c_device as spi:
            self._BUFFER[0] = (address | 0x80) & 0xFF
            spi.write(self._BUFFER, end=1)
            spi.readinto(self._BUFFER, end=1)
        return self._BUFFER[address]

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

## UTILS:

def bytestoint(lsb, msb): return (msb << 8) | lsb

def decode_sensor(arr):
    x = bytestoint(arr[0], arr[1])
    y = bytestoint(arr[2], arr[3])
    z = bytestoint(arr[4], arr[5])
    return (x, y, z)