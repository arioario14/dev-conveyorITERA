import smbus
import time

# Alamat I2C dari MPU6050
MPU6050_ADDR = 0x68

# Register untuk pengaturan dan membaca data
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

# Inisialisasi I2C bus
bus = smbus.SMBus(1)

# Fungsi untuk membaca data 2 byte
def read_word(reg):
    high = bus.read_byte_data(MPU6050_ADDR, reg)
    low = bus.read_byte_data(MPU6050_ADDR, reg + 1)
    value = (high << 8) + low
    if value >= 0x8000:
        value -= 0x10000
    return value

# Fungsi untuk membaca data akselerometer
def read_accel():
    ax = read_word(ACCEL_XOUT_H)
    ay = read_word(ACCEL_XOUT_H + 2)
    az = read_word(ACCEL_XOUT_H + 4)
    return ax, ay, az

# Fungsi untuk membaca data gyroscope
def read_gyro():
    gx = read_word(GYRO_XOUT_H)
    gy = read_word(GYRO_XOUT_H + 2)
    gz = read_word(GYRO_XOUT_H + 4)
    return gx, gy, gz

# Inisialisasi sensor MPU6050
bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

# Main program loop
try:
    while True:
        ax, ay, az = read_accel()
        gx, gy, gz = read_gyro()
        
        print(f"Accelerometer: X={ax}, Y={ay}, Z={az}")
        print(f"Gyroscope: X={gx}, Y={gy}, Z={gz}")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Program dihentikan")
