import RPi.GPIO as GPIO

ENCODER_A = 20
ENCODER_B = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENCODER_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ENCODER_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        print(f"Encoder A: {GPIO.input(ENCODER_A)}, Encoder B: {GPIO.input(ENCODER_B)}")
except KeyboardInterrupt:
    GPIO.cleanup()
