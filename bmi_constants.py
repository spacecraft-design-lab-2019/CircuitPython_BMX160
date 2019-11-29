from micropython import const

# Mask definitions
BMI160_ACCEL_BW_MASK                 = const(0x70)
BMI160_ACCEL_ODR_MASK                = const(0x0F)
BMI160_ACCEL_UNDERSAMPLING_MASK      = const(0x80)
BMI160_ACCEL_RANGE_MASK              = const(0x0F)
BMI160_GYRO_BW_MASK                  = const(0x30)
BMI160_GYRO_ODR_MASK                 = const(0x0F)
BMI160_GYRO_RANGE_MSK                = const(0x07)

# Mask definitions for INT_EN registers
BMI160_ANY_MOTION_X_INT_EN_MASK      = const(0x01)
BMI160_HIGH_G_X_INT_EN_MASK          = const(0x01)
BMI160_NO_MOTION_X_INT_EN_MASK       = const(0x01)
BMI160_ANY_MOTION_Y_INT_EN_MASK      = const(0x02)
BMI160_HIGH_G_Y_INT_EN_MASK          = const(0x02)
BMI160_NO_MOTION_Y_INT_EN_MASK       = const(0x02)
BMI160_ANY_MOTION_Z_INT_EN_MASK      = const(0x04)
BMI160_HIGH_G_Z_INT_EN_MASK          = const(0x04)
BMI160_NO_MOTION_Z_INT_EN_MASK       = const(0x04)
BMI160_SIG_MOTION_INT_EN_MASK        = const(0x07)
BMI160_ANY_MOTION_ALL_INT_EN_MASK    = const(0x07)
BMI160_STEP_DETECT_INT_EN_MASK       = const(0x08)
BMI160_DOUBLE_TAP_INT_EN_MASK        = const(0x10)
BMI160_SINGLE_TAP_INT_EN_MASK        = const(0x20)
BMI160_FIFO_FULL_INT_EN_MASK         = const(0x20)
BMI160_ORIENT_INT_EN_MASK            = const(0x40)
BMI160_FIFO_WATERMARK_INT_EN_MASK    = const(0x40)
BMI160_LOW_G_INT_EN_MASK             = const(0x08)
BMI160_STEP_DETECT_EN_MASK           = const(0x08)
BMI160_FLAT_INT_EN_MASK              = const(0x80)
BMI160_DATA_RDY_INT_EN_MASK          = const(0x10)

# PMU status Macros
BMI160_AUX_PMU_SUSPEND               = const(0x00)
BMI160_AUX_PMU_NORMAL                = const(0x01)
BMI160_AUX_PMU_LOW_POWER             = const(0x02)

BMI160_GYRO_PMU_SUSPEND              = const(0x00)
BMI160_GYRO_PMU_NORMAL               = const(0x01)
BMI160_GYRO_PMU_FSU                  = const(0x03)

BMI160_ACCEL_PMU_SUSPEND             = const(0x00)
BMI160_ACCEL_PMU_NORMAL              = const(0x01)
BMI160_ACCEL_PMU_LOW_POWER           = const(0x02)

# Mask definitions for INT_OUT_CTRL register
BMI160_INT1_EDGE_CTRL_MASK           = const(0x01)
BMI160_INT1_OUTPUT_MODE_MASK         = const(0x04)
BMI160_INT1_OUTPUT_TYPE_MASK         = const(0x02)
BMI160_INT1_OUTPUT_EN_MASK           = const(0x08)
BMI160_INT2_EDGE_CTRL_MASK           = const(0x10)
BMI160_INT2_OUTPUT_MODE_MASK         = const(0x40)
BMI160_INT2_OUTPUT_TYPE_MASK         = const(0x20)
BMI160_INT2_OUTPUT_EN_MASK           = const(0x80)

# Mask definitions for INT_LATCH register
BMI160_INT1_INPUT_EN_MASK            = const(0x10)
BMI160_INT2_INPUT_EN_MASK            = const(0x20)
BMI160_INT_LATCH_MASK                = const(0x0F)

# Mask definitions for INT_MAP register
BMI160_INT1_LOW_G_MASK               = const(0x01)
BMI160_INT1_HIGH_G_MASK              = const(0x02)
BMI160_INT1_SLOPE_MASK               = const(0x04)
BMI160_INT1_NO_MOTION_MASK           = const(0x08)
BMI160_INT1_DOUBLE_TAP_MASK          = const(0x10)
BMI160_INT1_SINGLE_TAP_MASK          = const(0x20)
BMI160_INT1_FIFO_FULL_MASK           = const(0x20)
BMI160_INT1_FIFO_WM_MASK             = const(0x40)
BMI160_INT1_ORIENT_MASK              = const(0x40)
BMI160_INT1_FLAT_MASK                = const(0x80)
BMI160_INT1_DATA_READY_MASK          = const(0x80)
BMI160_INT2_LOW_G_MASK               = const(0x01)
BMI160_INT1_LOW_STEP_DETECT_MASK     = const(0x01)
BMI160_INT2_LOW_STEP_DETECT_MASK     = const(0x01)
BMI160_INT2_HIGH_G_MASK              = const(0x02)
BMI160_INT2_FIFO_FULL_MASK           = const(0x02)
BMI160_INT2_FIFO_WM_MASK             = const(0x04)
BMI160_INT2_SLOPE_MASK               = const(0x04)
BMI160_INT2_DATA_READY_MASK          = const(0x08)
BMI160_INT2_NO_MOTION_MASK           = const(0x08)
BMI160_INT2_DOUBLE_TAP_MASK          = const(0x10)
BMI160_INT2_SINGLE_TAP_MASK          = const(0x20)
BMI160_INT2_ORIENT_MASK              = const(0x40)
BMI160_INT2_FLAT_MASK                = const(0x80)

# Mask definitions for INT_DATA register
BMI160_TAP_SRC_INT_MASK              = const(0x08)
BMI160_LOW_HIGH_SRC_INT_MASK         = const(0x80)
BMI160_MOTION_SRC_INT_MASK           = const(0x80)

# Mask definitions for INT_MOTION register
BMI160_SLOPE_INT_DUR_MASK            = const(0x03)
BMI160_NO_MOTION_INT_DUR_MASK        = const(0xFC)
BMI160_NO_MOTION_SEL_BIT_MASK        = const(0x01)

# Mask definitions for INT_TAP register
BMI160_TAP_DUR_MASK                  = const(0x07)
BMI160_TAP_SHOCK_DUR_MASK            = const(0x40)
BMI160_TAP_QUIET_DUR_MASK            = const(0x80)
BMI160_TAP_THRES_MASK                = const(0x1F)

# Mask definitions for INT_FLAT register
BMI160_FLAT_THRES_MASK               = const(0x3F)
BMI160_FLAT_HOLD_TIME_MASK           = const(0x30)
BMI160_FLAT_HYST_MASK                = const(0x07)

# Mask definitions for INT_LOWHIGH register
BMI160_LOW_G_HYST_MASK               = const(0x03)
BMI160_LOW_G_LOW_MODE_MASK           = const(0x04)
BMI160_HIGH_G_HYST_MASK              = const(0xC0)

# Mask definitions for INT_SIG_MOTION register
BMI160_SIG_MOTION_SEL_MASK           = const(0x02)
BMI160_SIG_MOTION_SKIP_MASK          = const(0x0C)
BMI160_SIG_MOTION_PROOF_MASK         = const(0x30)

# Mask definitions for INT_ORIENT register
BMI160_ORIENT_MODE_MASK              = const(0x03)
BMI160_ORIENT_BLOCK_MASK             = const(0x0C)
BMI160_ORIENT_HYST_MASK              = const(0xF0)
BMI160_ORIENT_THETA_MASK             = const(0x3F)
BMI160_ORIENT_UD_ENABLE              = const(0x40)
BMI160_AXES_EN_MASK                  = const(0x80)

# Mask definitions for FIFO_CONFIG register
BMI160_FIFO_GYRO                     = const(0x80)
BMI160_FIFO_ACCEL                    = const(0x40)
BMI160_FIFO_AUX                      = const(0x20)
BMI160_FIFO_TAG_INT1                 = const(0x08)
BMI160_FIFO_TAG_INT2                 = const(0x04)
BMI160_FIFO_TIME                     = const(0x02)
BMI160_FIFO_HEADER                   = const(0x10)
BMI160_FIFO_CONFIG_1_MASK            = const(0xFE)

# Mask definitions for STEP_CONF register
BMI160_STEP_COUNT_EN_BIT_MASK        = const(0x08)
BMI160_STEP_DETECT_MIN_THRES_MASK    = const(0x18)
BMI160_STEP_DETECT_STEPTIME_MIN_MASK = const(0x07)
BMI160_STEP_MIN_BUF_MASK             = const(0x07)

# Mask definition for FIFO Header Data Tag
BMI160_FIFO_TAG_INTR_MASK            = const(0xFC)

# Fifo byte counter mask definitions
BMI160_FIFO_BYTE_COUNTER_MASK        = const(0x07)

# Enable/disable bit value
BMI160_ENABLE                        = const(0x01)
BMI160_DISABLE                       = const(0x00)

# Latch Duration
BMI160_LATCH_DUR_NONE                = const(0x00)
BMI160_LATCH_DUR_312_5_MICRO_SEC     = const(0x01)
BMI160_LATCH_DUR_625_MICRO_SEC       = const(0x02)
BMI160_LATCH_DUR_1_25_MILLI_SEC      = const(0x03)
BMI160_LATCH_DUR_2_5_MILLI_SEC       = const(0x04)
BMI160_LATCH_DUR_5_MILLI_SEC         = const(0x05)
BMI160_LATCH_DUR_10_MILLI_SEC        = const(0x06)
BMI160_LATCH_DUR_20_MILLI_SEC        = const(0x07)
BMI160_LATCH_DUR_40_MILLI_SEC        = const(0x08)
BMI160_LATCH_DUR_80_MILLI_SEC        = const(0x09)
BMI160_LATCH_DUR_160_MILLI_SEC       = const(0x0A)
BMI160_LATCH_DUR_320_MILLI_SEC       = const(0x0B)
BMI160_LATCH_DUR_640_MILLI_SEC       = const(0x0C)
BMI160_LATCH_DUR_1_28_SEC            = const(0x0D)
BMI160_LATCH_DUR_2_56_SEC            = const(0x0E)
BMI160_LATCHED                       = const(0x0F)

# BMI160 Register map
BMI160_CHIP_ID_ADDR                  = const(0x00)
BMI160_ERROR_REG_ADDR                = const(0x02)
BMI160_PMU_STATUS_ADDR               = const(0x03)
BMI160_AUX_DATA_ADDR                 = const(0x04)
BMI160_GYRO_DATA_ADDR                = const(0x0C)
BMI160_ACCEL_DATA_ADDR               = const(0x12)
BMI160_STATUS_ADDR                   = const(0x1B)
BMI160_INT_STATUS_ADDR               = const(0x1C)
BMI160_FIFO_LENGTH_ADDR              = const(0x22)
BMI160_FIFO_DATA_ADDR                = const(0x24)
BMI160_ACCEL_CONFIG_ADDR             = const(0x40)
BMI160_ACCEL_RANGE_ADDR              = const(0x41)
BMI160_GYRO_CONFIG_ADDR              = const(0x42)
BMI160_GYRO_RANGE_ADDR               = const(0x43)
BMI160_AUX_ODR_ADDR                  = const(0x44)
BMI160_FIFO_DOWN_ADDR                = const(0x45)
BMI160_FIFO_CONFIG_0_ADDR            = const(0x46)
BMI160_FIFO_CONFIG_1_ADDR            = const(0x47)
BMI160_AUX_IF_0_ADDR                 = const(0x4B)
BMI160_AUX_IF_1_ADDR                 = const(0x4C)
BMI160_AUX_IF_2_ADDR                 = const(0x4D)
BMI160_AUX_IF_3_ADDR                 = const(0x4E)
BMI160_AUX_IF_4_ADDR                 = const(0x4F)
BMI160_INT_ENABLE_0_ADDR             = const(0x50)
BMI160_INT_ENABLE_1_ADDR             = const(0x51)
BMI160_INT_ENABLE_2_ADDR             = const(0x52)
BMI160_INT_OUT_CTRL_ADDR             = const(0x53)
BMI160_INT_LATCH_ADDR                = const(0x54)
BMI160_INT_MAP_0_ADDR                = const(0x55)
BMI160_INT_MAP_1_ADDR                = const(0x56)
BMI160_INT_MAP_2_ADDR                = const(0x57)
BMI160_INT_DATA_0_ADDR               = const(0x58)
BMI160_INT_DATA_1_ADDR               = const(0x59)
BMI160_INT_LOWHIGH_0_ADDR            = const(0x5A)
BMI160_INT_LOWHIGH_1_ADDR            = const(0x5B)
BMI160_INT_LOWHIGH_2_ADDR            = const(0x5C)
BMI160_INT_LOWHIGH_3_ADDR            = const(0x5D)
BMI160_INT_LOWHIGH_4_ADDR            = const(0x5E)
BMI160_INT_MOTION_0_ADDR             = const(0x5F)
BMI160_INT_MOTION_1_ADDR             = const(0x60)
BMI160_INT_MOTION_2_ADDR             = const(0x61)
BMI160_INT_MOTION_3_ADDR             = const(0x62)
BMI160_INT_TAP_0_ADDR                = const(0x63)
BMI160_INT_TAP_1_ADDR                = const(0x64)
BMI160_INT_ORIENT_0_ADDR             = const(0x65)
BMI160_INT_ORIENT_1_ADDR             = const(0x66)
BMI160_INT_FLAT_0_ADDR               = const(0x67)
BMI160_INT_FLAT_1_ADDR               = const(0x68)
BMI160_FOC_CONF_ADDR                 = const(0x69)
BMI160_CONF_ADDR                     = const(0x6A)

BMI160_IF_CONF_ADDR                  = const(0x6B)
BMI160_SELF_TEST_ADDR                = const(0x6D)
BMI160_OFFSET_ADDR                   = const(0x71)
BMI160_OFFSET_CONF_ADDR              = const(0x77)
BMI160_INT_STEP_CNT_0_ADDR           = const(0x78)
BMI160_INT_STEP_CONFIG_0_ADDR        = const(0x7A)
BMI160_INT_STEP_CONFIG_1_ADDR        = const(0x7B)
BMI160_COMMAND_REG_ADDR              = const(0x7E)
BMI160_SPI_COMM_TEST_ADDR            = const(0x7F)
BMI160_INTL_PULLUP_CONF_ADDR         = const(0x85)

# Error code definitions
BMI160_OK                            = const(0)
BMI160_E_NULL_PTR                    = const(-1)
BMI160_E_COM_FAIL                    = const(-2)
BMI160_E_DEV_NOT_FOUND               = const(-3)
BMI160_E_OUT_OF_RANGE                = const(-4)
BMI160_E_INVALID_INPUT               = const(-5)
BMI160_E_ACCEL_ODR_BW_INVALID        = const(-6)
BMI160_E_GYRO_ODR_BW_INVALID         = const(-7)
BMI160_E_LWP_PRE_FLTR_INT_INVALID    = const(-8)
BMI160_E_LWP_PRE_FLTR_INVALID        = const(-9)
BMI160_E_AUX_NOT_FOUND               = const(-10)
BMI160_FOC_FAILURE                   = const(-11)

#\name API warning codes
BMI160_W_GYRO_SELF_TEST_FAIL         = const(1)
BMI160_W_ACCEl_SELF_TEST_FAIL        = const(2)

# BMI160 unique chip identifier
BMI160_CHIP_ID                       = const(0xD8)

# Soft reset command
BMI160_SOFT_RESET_CMD                = const(0xb6)
BMI160_SOFT_RESET_DELAY_MS           = const(1)

# Start FOC command
BMI160_START_FOC_CMD                 = const(0x03)

# NVM backup enabling command
BMI160_NVM_BACKUP_EN                 = const(0xA0)

# Delay in ms settings
BMI160_ACCEL_DELAY_MS                = const(5)
BMI160_GYRO_DELAY_MS                 = const(81)
BMI160_ONE_MS_DELAY                  = const(1)
BMI160_AUX_COM_DELAY                 = const(10)
BMI160_GYRO_SELF_TEST_DELAY          = const(20)
BMI160_ACCEL_SELF_TEST_DELAY         = const(50)

# Self test configurations
BMI160_ACCEL_SELF_TEST_CONFIG        = const(0x2C)
BMI160_ACCEL_SELF_TEST_POSITIVE_EN   = const(0x0D)
BMI160_ACCEL_SELF_TEST_NEGATIVE_EN   = const(0x09)
BMI160_ACCEL_SELF_TEST_LIMIT         = const(8192)

# Power mode settings
# Accel power mode
BMI160_ACCEL_NORMAL_MODE             = const(0x11)
BMI160_ACCEL_LOWPOWER_MODE           = const(0x12)
BMI160_ACCEL_SUSPEND_MODE            = const(0x10)

# Gyro power mode
BMI160_GYRO_SUSPEND_MODE             = const(0x14)
BMI160_GYRO_NORMAL_MODE              = const(0x15)
BMI160_GYRO_FASTSTARTUP_MODE         = const(0x17)

# Aux power mode
BMI160_AUX_SUSPEND_MODE              = const(0x18)
BMI160_AUX_NORMAL_MODE               = const(0x19)
BMI160_AUX_LOWPOWER_MODE             = const(0x1A)

# Range settings
# Accel Range
BMI160_ACCEL_RANGE_2G                = const(0x03)
BMI160_ACCEL_RANGE_4G                = const(0x05)
BMI160_ACCEL_RANGE_8G                = const(0x08)
BMI160_ACCEL_RANGE_16G               = const(0x0C)

# Gyro Range
BMI160_GYRO_RANGE_2000_DPS           = const(0x00)
BMI160_GYRO_RANGE_1000_DPS           = const(0x01)
BMI160_GYRO_RANGE_500_DPS            = const(0x02)
BMI160_GYRO_RANGE_250_DPS            = const(0x03)
BMI160_GYRO_RANGE_125_DPS            = const(0x04)

# Bandwidth settings
# Accel Bandwidth
BMI160_ACCEL_BW_OSR4_AVG1            = const(0x00)
BMI160_ACCEL_BW_OSR2_AVG2            = const(0x01)
BMI160_ACCEL_BW_NORMAL_AVG4          = const(0x02)
BMI160_ACCEL_BW_RES_AVG8             = const(0x03)
BMI160_ACCEL_BW_RES_AVG16            = const(0x04)
BMI160_ACCEL_BW_RES_AVG32            = const(0x05)
BMI160_ACCEL_BW_RES_AVG64            = const(0x06)
BMI160_ACCEL_BW_RES_AVG128           = const(0x07)

BMI160_GYRO_BW_OSR4_MODE             = const(0x00)
BMI160_GYRO_BW_OSR2_MODE             = const(0x01)
BMI160_GYRO_BW_NORMAL_MODE           = const(0x02)

# Output Data Rate settings
# Accel Output data rate
BMI160_ACCEL_ODR_RESERVED            = const(0x00)
BMI160_ACCEL_ODR_0_78HZ              = const(0x01)
BMI160_ACCEL_ODR_1_56HZ              = const(0x02)
BMI160_ACCEL_ODR_3_12HZ              = const(0x03)
BMI160_ACCEL_ODR_6_25HZ              = const(0x04)
BMI160_ACCEL_ODR_12_5HZ              = const(0x05)
BMI160_ACCEL_ODR_25HZ                = const(0x06)
BMI160_ACCEL_ODR_50HZ                = const(0x07)
BMI160_ACCEL_ODR_100HZ               = const(0x08)
BMI160_ACCEL_ODR_200HZ               = const(0x09)
BMI160_ACCEL_ODR_400HZ               = const(0x0A)
BMI160_ACCEL_ODR_800HZ               = const(0x0B)
BMI160_ACCEL_ODR_1600HZ              = const(0x0C)
BMI160_ACCEL_ODR_RESERVED0           = const(0x0D)
BMI160_ACCEL_ODR_RESERVED1           = const(0x0E)
BMI160_ACCEL_ODR_RESERVED2           = const(0x0F)

# Gyro Output data rate
BMI160_GYRO_ODR_RESERVED             = const(0x00)
BMI160_GYRO_ODR_25HZ                 = const(0x06)
BMI160_GYRO_ODR_50HZ                 = const(0x07)
BMI160_GYRO_ODR_100HZ                = const(0x08)
BMI160_GYRO_ODR_200HZ                = const(0x09)
BMI160_GYRO_ODR_400HZ                = const(0x0A)
BMI160_GYRO_ODR_800HZ                = const(0x0B)
BMI160_GYRO_ODR_1600HZ               = const(0x0C)
BMI160_GYRO_ODR_3200HZ               = const(0x0D)

# Auxiliary sensor Output data rate
BMI160_AUX_ODR_RESERVED              = const(0x00)
BMI160_AUX_ODR_0_78HZ                = const(0x01)
BMI160_AUX_ODR_1_56HZ                = const(0x02)
BMI160_AUX_ODR_3_12HZ                = const(0x03)
BMI160_AUX_ODR_6_25HZ                = const(0x04)
BMI160_AUX_ODR_12_5HZ                = const(0x05)
BMI160_AUX_ODR_25HZ                  = const(0x06)
BMI160_AUX_ODR_50HZ                  = const(0x07)
BMI160_AUX_ODR_100HZ                 = const(0x08)
BMI160_AUX_ODR_200HZ                 = const(0x09)
BMI160_AUX_ODR_400HZ                 = const(0x0A)
BMI160_AUX_ODR_800HZ                 = const(0x0B)

# Maximum limits definition
BMI160_ACCEL_ODR_MAX                 = const(15)
BMI160_ACCEL_BW_MAX                  = const(2)
BMI160_ACCEL_RANGE_MAX               = const(12)
BMI160_GYRO_ODR_MAX                  = const(13)
BMI160_GYRO_BW_MAX                   = const(2)
BMI160_GYRO_RANGE_MAX                = const(4)

# FIFO_CONFIG Definitions
BMI160_FIFO_TIME_ENABLE              = const(0x02)
BMI160_FIFO_TAG_INT2_ENABLE          = const(0x04)
BMI160_FIFO_TAG_INT1_ENABLE          = const(0x08)
BMI160_FIFO_HEAD_ENABLE              = const(0x10)
BMI160_FIFO_M_ENABLE                 = const(0x20)
BMI160_FIFO_A_ENABLE                 = const(0x40)
BMI160_FIFO_M_A_ENABLE               = const(0x60)
BMI160_FIFO_G_ENABLE                 = const(0x80)
BMI160_FIFO_M_G_ENABLE               = const(0xA0)
BMI160_FIFO_G_A_ENABLE               = const(0xC0)
BMI160_FIFO_M_G_A_ENABLE             = const(0xE0)

# Macro to specify the number of bytes over-read from the FIFO in order to get the sensor time at the end of FIFO
BMI160_FIFO_BYTES_OVERREAD           = const(25)

# Accel, gyro and aux. sensor length and also their combined length definitions in FIFO
BMI160_FIFO_G_LENGTH                 = const(6)
BMI160_FIFO_A_LENGTH                 = const(6)
BMI160_FIFO_M_LENGTH                 = const(8)
BMI160_FIFO_GA_LENGTH                = const(12)
BMI160_FIFO_MA_LENGTH                = const(14)
BMI160_FIFO_MG_LENGTH                = const(14)
BMI160_FIFO_MGA_LENGTH               = const(20)

# FIFO Header Data definitions
BMI160_FIFO_HEAD_SKIP_FRAME          = const(0x40)
BMI160_FIFO_HEAD_SENSOR_TIME         = const(0x44)
BMI160_FIFO_HEAD_INPUT_CONFIG        = const(0x48)
BMI160_FIFO_HEAD_OVER_READ           = const(0x80)
BMI160_FIFO_HEAD_A                   = const(0x84)
BMI160_FIFO_HEAD_G                   = const(0x88)
BMI160_FIFO_HEAD_G_A                 = const(0x8C)
BMI160_FIFO_HEAD_M                   = const(0x90)
BMI160_FIFO_HEAD_M_A                 = const(0x94)
BMI160_FIFO_HEAD_M_G                 = const(0x98)
BMI160_FIFO_HEAD_M_G_A               = const(0x9C)

# FIFO sensor time length definitions
BMI160_SENSOR_TIME_LENGTH            = const(3)

# FIFO DOWN selection
# Accel fifo down-sampling values
BMI160_ACCEL_FIFO_DOWN_ZERO         = const(0x00)
BMI160_ACCEL_FIFO_DOWN_ONE          = const(0x10)
BMI160_ACCEL_FIFO_DOWN_TWO          = const(0x20)
BMI160_ACCEL_FIFO_DOWN_THREE        = const(0x30)
BMI160_ACCEL_FIFO_DOWN_FOUR         = const(0x40)
BMI160_ACCEL_FIFO_DOWN_FIVE         = const(0x50)
BMI160_ACCEL_FIFO_DOWN_SIX          = const(0x60)
BMI160_ACCEL_FIFO_DOWN_SEVEN        = const(0x70)

# Gyro fifo down-smapling values
BMI160_GYRO_FIFO_DOWN_ZERO          = const(0x00)
BMI160_GYRO_FIFO_DOWN_ONE           = const(0x01)
BMI160_GYRO_FIFO_DOWN_TWO           = const(0x02)
BMI160_GYRO_FIFO_DOWN_THREE         = const(0x03)
BMI160_GYRO_FIFO_DOWN_FOUR          = const(0x04)
BMI160_GYRO_FIFO_DOWN_FIVE          = const(0x05)
BMI160_GYRO_FIFO_DOWN_SIX           = const(0x06)
BMI160_GYRO_FIFO_DOWN_SEVEN         = const(0x07)

# Accel Fifo filter enable
BMI160_ACCEL_FIFO_FILT_EN           = const(0x80)

# Gyro Fifo filter enable
BMI160_GYRO_FIFO_FILT_EN            = const(0x08)

# Definitions to check validity of FIFO frames
FIFO_CONFIG_MSB_CHECK                = const(0x80)
FIFO_CONFIG_LSB_CHECK                = const(0x00)

#! BMI160 accel FOC configurations
BMI160_FOC_ACCEL_DISABLED            = const(0x00)
BMI160_FOC_ACCEL_POSITIVE_G          = const(0x01)
BMI160_FOC_ACCEL_NEGATIVE_G          = const(0x02)
BMI160_FOC_ACCEL_0G                  = const(0x03)

# Array Parameter DefinItions
BMI160_SENSOR_TIME_LSB_BYTE          = const(0)
BMI160_SENSOR_TIME_XLSB_BYTE         = const(1)
BMI160_SENSOR_TIME_MSB_BYTE          = const(2)

# Interface settings
BMI160_SPI_INTF                      = const(1)
BMI160_I2C_INTF                      = const(0)
BMI160_SPI_RD_MASK                   = const(0x80)
BMI160_SPI_WR_MASK                   = const(0x7F)

# Sensor & time select definition
BMI160_ACCEL_SEL                     = const(0x01)
BMI160_GYRO_SEL                      = const(0x02)
BMI160_TIME_SEL                      = const(0x04)

# Sensor select mask
BMI160_SEN_SEL_MASK                  = const(0x07)

# Error code mask
BMI160_ERR_REG_MASK                  = const(0x0F)

# BMI160 I2C address
BMI160_I2C_ADDR                      = const(0x68)

# BMI160 secondary IF address
BMI160_AUX_BMM150_I2C_ADDR           = const(0x10)

# BMI160 Length definitions
BMI160_ONE                           = const(1)
BMI160_TWO                           = const(2)
BMI160_THREE                         = const(3)
BMI160_FOUR                          = const(4)
BMI160_FIVE                          = const(5)

# BMI160 fifo level Margin
BMI160_FIFO_LEVEL_MARGIN             = const(16)

# BMI160 fifo flush Command
BMI160_FIFO_FLUSH_VALUE              = const(0xB0)

# BMI160 offset values for xyz axes of accel
BMI160_ACCEL_MIN_OFFSET              = const(-128)
BMI160_ACCEL_MAX_OFFSET              = const(127)

# BMI160 offset values for xyz axes of gyro
BMI160_GYRO_MIN_OFFSET               = const(-512)
BMI160_GYRO_MAX_OFFSET               = const(511)

# BMI160 fifo full interrupt position and mask
BMI160_FIFO_FULL_INT_POS             = const(5)
BMI160_FIFO_FULL_INT_MSK             = const(0x20)
BMI160_FIFO_WTM_INT_POS              = const(6)
BMI160_FIFO_WTM_INT_MSK              = const(0x40)

BMI160_FIFO_FULL_INT_PIN1_POS        = const(5)
BMI160_FIFO_FULL_INT_PIN1_MSK        = const(0x20)
BMI160_FIFO_FULL_INT_PIN2_POS        = const(1)
BMI160_FIFO_FULL_INT_PIN2_MSK        = const(0x02)

BMI160_FIFO_WTM_INT_PIN1_POS         = const(6)
BMI160_FIFO_WTM_INT_PIN1_MSK         = const(0x40)
BMI160_FIFO_WTM_INT_PIN2_POS         = const(2)
BMI160_FIFO_WTM_INT_PIN2_MSK         = const(0x04)

BMI160_MANUAL_MODE_EN_POS            = const(7)
BMI160_MANUAL_MODE_EN_MSK            = const(0x80)
BMI160_AUX_READ_BURST_POS            = const(0)
BMI160_AUX_READ_BURST_MSK            = const(0x03)

BMI160_GYRO_SELF_TEST_POS            = const(4)
BMI160_GYRO_SELF_TEST_MSK            = const(0x10)
BMI160_GYRO_SELF_TEST_STATUS_POS     = const(1)
BMI160_GYRO_SELF_TEST_STATUS_MSK     = const(0x02)

BMI160_GYRO_FOC_EN_POS               = const(6)
BMI160_GYRO_FOC_EN_MSK               = const(0x40)

BMI160_ACCEL_FOC_X_CONF_POS          = const(4)
BMI160_ACCEL_FOC_X_CONF_MSK          = const(0x30)

BMI160_ACCEL_FOC_Y_CONF_POS          = const(2)
BMI160_ACCEL_FOC_Y_CONF_MSK          = const(0x0C)

BMI160_ACCEL_FOC_Z_CONF_MSK          = const(0x03)

BMI160_FOC_STATUS_POS                = const(3)
BMI160_FOC_STATUS_MSK                = const(0x08)

BMI160_GYRO_OFFSET_X_MSK             = const(0x03)

BMI160_GYRO_OFFSET_Y_POS             = const(2)
BMI160_GYRO_OFFSET_Y_MSK             = const(0x0C)

BMI160_GYRO_OFFSET_Z_POS             = const(4)
BMI160_GYRO_OFFSET_Z_MSK             = const(0x30)

BMI160_GYRO_OFFSET_EN_POS            = const(7)
BMI160_GYRO_OFFSET_EN_MSK            = const(0x80)

BMI160_ACCEL_OFFSET_EN_POS           = const(6)
BMI160_ACCEL_OFFSET_EN_MSK           = const(0x40)

BMI160_GYRO_OFFSET_POS               = const(8)
BMI160_GYRO_OFFSET_MSK               = const(0x0300)

BMI160_NVM_UPDATE_POS                = const(1)
BMI160_NVM_UPDATE_MSK                = const(0x02)

BMI160_NVM_STATUS_POS                = const(4)
BMI160_NVM_STATUS_MSK                = const(0x10)

BMI160_MAG_POWER_MODE_MSK            = const(0x03)

BMI160_ACCEL_POWER_MODE_MSK          = const(0x30)
BMI160_ACCEL_POWER_MODE_POS          = const(4)

BMI160_GYRO_POWER_MODE_MSK           = const(0x0C)
BMI160_GYRO_POWER_MODE_POS           = const(2)