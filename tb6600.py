import RPi.GPIO as GPIO
import time

# Pin assignment
enable_pin = 11  # Pin enable
dir_pin = 13     # Pin direction
pulse_pin = 15   # Pin pulse

# Steps and delay
steps_per_revolution = 900  # Sesuaikan dengan motor Anda
delay_time = 0.0001         # Delay dalam detik (1000 microseconds)

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(pulse_pin, GPIO.OUT)

# Enable driver
GPIO.output(enable_pin, GPIO.LOW)  # Aktifkan driver

try:
    while True:
        # Gerakkan motor ke satu arah
        GPIO.output(dir_pin, GPIO.LOW)  # Arahkan motor

        
        GPIO.output(pulse_pin, GPIO.HIGH)
        time.sleep(delay_time)          # Waktu tinggi
        GPIO.output(pulse_pin, GPIO.LOW)
        time.sleep(delay_time)          # Waktu rendah
          # Delay setelah putaran kedua

except KeyboardInterrupt:
    print("Program dihentikan")

finally:
    GPIO.cleanup()  # Membersihkan GPIO
