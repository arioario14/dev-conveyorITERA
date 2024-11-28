import RPi.GPIO as GPIO
import time

# Pin GPIO Raspberry Pi
pin_a = 20  # GPIO pin untuk Encoder_A
pin_b = 21  # GPIO pin untuk Encoder_B

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Gunakan penomoran BCM
GPIO.setup(pin_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variabel global
encoder_value = 0

# Callback fungsi encoder
def encoder_callback(channel):
    global encoder_value
    A = GPIO.input(pin_a)
    B = GPIO.input(pin_b)

    # Deteksi arah rotasi
    if A == GPIO.HIGH and B == GPIO.LOW:
        encoder_value += 1
    elif A == GPIO.LOW and B == GPIO.HIGH:
        encoder_value -= 1

# Tambahkan event detect
try:
    GPIO.add_event_detect(pin_a, GPIO.BOTH, callback=encoder_callback)
    GPIO.add_event_detect(pin_b, GPIO.BOTH, callback=encoder_callback)

    print("Program dimulai. Tekan Ctrl+C untuk berhenti.")
    while True:
        print(f"Encoder Value: {encoder_value}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    GPIO.cleanup()

