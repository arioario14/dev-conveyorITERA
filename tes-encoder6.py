import RPi.GPIO as GPIO
import time

TEST_PIN = 20  # Ganti dengan salah satu pin encoder (A atau B)

GPIO.setmode(GPIO.BCM)
GPIO.setup(TEST_PIN, GPIO.IN)

def test_callback(channel):
    print(f"Edge detected on pin {channel}")

try:
    GPIO.add_event_detect(TEST_PIN, GPIO.BOTH, callback=test_callback, bouncetime=10)
    print("Menunggu edge detection...")
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Dihentikan.")
finally:
    GPIO.cleanup()
