import RPi.GPIO as GPIO
import time

# Pin untuk Rotary Encoder
ENCODER_A = 20  # Pin A pada encoder
ENCODER_B = 21  # Pin B pada encoder

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENCODER_A, GPIO.IN)  # Gunakan pull-up eksternal
GPIO.setup(ENCODER_B, GPIO.IN)  # Gunakan pull-up eksternal

# Variabel global untuk posisi dan arah
position = 0
direction = None

# Fungsi callback untuk menangani perubahan status pada pin A
def encoder_callback_A(channel):
    global position, direction
    if GPIO.input(ENCODER_A) == GPIO.HIGH:  # Pin A naik
        if GPIO.input(ENCODER_B) == GPIO.LOW:
            position += 1
            direction = "CW"  # Clockwise
        else:
            position -= 1
            direction = "CCW"  # Counterclockwise
    print(f"Posisi: {position}, Arah: {direction}")

# Fungsi callback untuk menangani perubahan status pada pin B
def encoder_callback_B(channel):
    global position, direction
    if GPIO.input(ENCODER_B) == GPIO.HIGH:  # Pin B naik
        if GPIO.input(ENCODER_A) == GPIO.LOW:
            position -= 1
            direction = "CCW"  # Counterclockwise
        else:
            position += 1
            direction = "CW"  # Clockwise
    print(f"Posisi: {position}, Arah: {direction}")

# Pasang interrupt untuk mendeteksi perubahan status pada Pin A dan B
GPIO.add_event_detect(ENCODER_A, GPIO.BOTH, callback=encoder_callback_A, bouncetime=1)
GPIO.add_event_detect(ENCODER_B, GPIO.BOTH, callback=encoder_callback_B, bouncetime=1)

print("Program berjalan. Putar encoder untuk melihat posisi dan arah.")

try:
    while True:
        time.sleep(0.1)  # Loop utama tetap berjalan
except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    GPIO.cleanup()
