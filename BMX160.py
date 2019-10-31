import time
try:
    import struct
except ImportError:
    import ustruct as struct

import adafruit_bus_device.i2c_device as i2c_device
import adafruit_bus_device.spi_device as spi_device
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
BMX160_AUX_DATA_ADDR       = const(0x04)
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
BMX160_AUX_ODR_ADDR        = const(0x44)
BMX160_FIFO_DOWN_ADDR      = const(0x45)
BMX160_FIFO_CONFIG_0_ADDR  = const(0x46)
BMX160_FIFO_CONFIG_1_ADDR  = const(0x47)
BMX160_AUX_IF_0_ADDR       = const(0x4B)
BMX160_AUX_IF_1_ADDR       = const(0x4C)
BMX160_AUX_IF_2_ADDR       = const(0x4D)
BMX160_AUX_IF_3_ADDR       = const(0x4E)
BMX160_AUX_IF_4_ADDR       = const(0x4F)
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

# I2C address
BMX160_I2C_ADDR            = const(0x68)
# Interface settings
BMX160_SPI_INTF            = const(1)
BMX160_I2C_INTF            = const(0)
BMX160_SPI_RD_MASK         = const(0x80)
BMX160_SPI_WR_MASK         = const(0x7F)

class BMX160:
    """Driver for the BMX160 accelerometer, magnetometer, gyroscope."""

    _BUFFER = bytearray(20)

    def __init__(self):
        # soft reset & reboot
        self._write_u8(BMX160_COMMAND_REG_ADDR, BMX160_SOFT_RESET_CMD)
        time.sleep(BMX160_SOFT_RESET_DELAY_MS)
        # Check ID registers.
        ID = self._read_u8(BMX160_CHIP_ID_ADDR)
        print('ID: %', ID)
        if ID != BMX160_CHIP_ID
            raise RuntimeError('Could not find BMX160, check wiring!')

        # Set default ranges for the various sensors
        # self._accel_mg_lsb = None
        # self._mag_mgauss_lsb = None
        # self._gyro_dps_digit = None
        # self.accel_range = ACCELRANGE_2G
        # self.mag_gain = MAGGAIN_4GAUSS
        # self.gyro_scale = GYROSCALE_245DPS



class BMX160_I2C(BMX160):
    """Driver for the BMX160 connect over I2C."""
    def __init__(self, i2c):
        self._device = i2c_device.I2CDevice(i2c, BMX160_I2C_ADDR)
        super().__init__()

    def _read_u8(self, address):
        with self._device as i2c:
            self._BUFFER[0] = address & 0xFF
            i2c.write_then_readinto(self._BUFFER, self._BUFFER, out_end=1, in_start=1, in_end=2)
        return self._BUFFER[1]

    def _read_bytes(self, address, count, buf):
        with self._device as i2c:
            buf[0] = address & 0xFF
            i2c.write_then_readinto(buf, buf, out_end=1, in_end=count)

    def _write_u8(self, address, val):
        with self._device as i2c:
            self._BUFFER[0] = address & 0xFF
            self._BUFFER[1] = val & 0xFF
            i2c.write(self._BUFFER, end=2)


class BMX160_SPI(BMX160):
    """Driver for the BMX160 connect over SPI."""
    def __init__(self, spi, cs):
        self._device = spi_device.SPIDevice(spi, cs)
        super().__init__()

    def _read_u8(self, address):
        with self._device as spi:
            self._BUFFER[0] = (address | 0x80) & 0xFF
            spi.write(self._BUFFER, end=1)
            spi.readinto(self._BUFFER, end=1)
        return self._BUFFER[0]

    def _read_bytes(self, address, count, buf):
        with self._device as spi:
            buf[0] = (address | 0x80) & 0xFF
            spi.write(buf, end=1)
            spi.readinto(buf, end=count)

    def _write_u8(self, address, val):
        with self._device as spi:
            self._BUFFER[0] = (address & 0x7F) & 0xFF
            self._BUFFER[1] = val & 0xFF
            spi.write(self._BUFFER, end=2)