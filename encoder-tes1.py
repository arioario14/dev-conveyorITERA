import RPi.GPIO as GPIO
import time

# Pin GPIO yang digunakan
PIN_A = 20  # Ganti dengan nomor pin untuk channel A
PIN_B = 21  # Ganti dengan nomor pin untuk channel B

# Variabel global untuk melacak arah dan posisi
position = 0
direction = None

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_A, GPIO.IN)  # Tanpa pull-up internal
GPIO.setup(PIN_B, GPIO.IN)  # Tanpa pull-up internal

# Callback untuk channel A
def callback_A(channel):
    global position, direction
    if GPIO.input(PIN_A) == GPIO.LOW:  # Jika ada falling edge di A
        if GPIO.input(PIN_B) == GPIO.HIGH:
            position += 1  # Arah searah jarum jam (CW)
            direction = "CW"
        else:
            position -= 1  # Arah berlawanan jarum jam (CCW)
            direction = "CCW"
        print(f"Falling Edge di A: Posisi={position}, Arah={direction}")

# Callback untuk channel B
def callback_B(channel):
    global position, direction
    if GPIO.input(PIN_B) == GPIO.LOW:  # Jika ada falling edge di B
        if GPIO.input(PIN_A) == GPIO.HIGH:
            position -= 1  # Arah berlawanan jarum jam (CCW)
            direction = "CCW"
        else:
            position += 1  # Arah searah jarum jam (CW)
            direction = "CW"
        print(f"Falling Edge di B: Posisi={position}, Arah={direction}")

# Tambahkan event detection untuk kedua pin
GPIO.add_event_detect(PIN_A, GPIO.FALLING, callback=callback_A, bouncetime=1)
GPIO.add_event_detect(PIN_B, GPIO.FALLING, callback=callback_B, bouncetime=1)

print("Menunggu input dari incremental encoder... (Tekan Ctrl+C untuk keluar)")

try:
    while True:
        time.sleep(0.1)  # Loop utama
except KeyboardInterrupt:
    print("\nProgram dihentikan.")
finally:
    GPIO.cleanup()  # Reset GPIO
