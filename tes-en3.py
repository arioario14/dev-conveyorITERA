import RPi.GPIO as GPIO
import time

# Pin untuk Rotary Encoder
ENCODER_A = 20  # Pin A pada encoder
ENCODER_B = 21  # Pin B pada encoder

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENCODER_A, GPIO.IN)  # Gunakan pull-up internal
GPIO.setup(ENCODER_B, GPIO.IN)  # Gunakan pull-up internal

# Fungsi untuk menangani perubahan status
def encoder_callback(channel):
    state_A = GPIO.input(ENCODER_A)
    state_B = GPIO.input(ENCODER_B)
    print(f"Pin A: {state_A}, Pin B: {state_B}")

# Pasang interrupt untuk mendeteksi perubahan status pada Pin A dan B


print("Program berjalan. Putar encoder untuk melihat perubahan status pin.")

try:
    while True:
       
        encoder_callback(ENCODER_A)
        time.sleep(1)
        
         # time.sleep(0.1)  # Program terus berjalan, hanya mencetak status pin
except KeyboardInterrupt:
    print("Program dihentikan.")

finally:
    GPIO.cleanup()

