import RPi.GPIO as GPIO
import time

# Pin untuk CW dan CCW
CW_pin = 26
CCW_pin = 19
AllWindingOff_pin = 13
CurrentCutback_pin = 6

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Menggunakan penomoran BCM untuk GPIO
GPIO.setup(CW_pin, GPIO.OUT)
GPIO.setup(CCW_pin, GPIO.OUT)
GPIO.setup(AllWindingOff_pin, GPIO.OUT)
GPIO.setup(CurrentCutback_pin, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(AllWindingOff_pin, GPIO.LOW)
GPIO.output(CurrentCutback_pin, GPIO.HIGH)
time.sleep(1)
GPIO.output(CCW_pin, GPIO.LOW)
GPIO.output(CW_pin, GPIO.LOW)
time.sleep(1)

def generate_pulse(num_pulses, delay):
    for _ in range(num_pulses):
#         GPIO.output(26, GPIO.HIGH)
#         GPIO.output(26, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)
        time.sleep(delay*0.8)
#         print("ON")
#         time.sleep(delay)
        GPIO.output(19, GPIO.LOW)
        time.sleep(delay)
#         GPIO.output(26, GPIO.HIGH)
#         GPIO.output(26, GPIO.HIGH)
#         GPIO.output(19, GPIO.HIGH)
#         time.sleep(delay)
#         print("OFF")

def rotate(direction, speed):
        
    if (direction == "CW"):
        GPIO.output(CCW_pin, GPIO.LOW)
        GPIO.output(CW_pin, GPIO.HIGH)
        time.sleep(speed)
        GPIO.output(CW_pin, GPIO.LOW)
#         GPIO.output(CW_pin, GPIO.LOW)
        time.sleep(speed)
    
    if (direction == "CCW"):
        GPIO.output(CW_pin, GPIO.LOW)
        GPIO.output(CCW_pin, GPIO.HIGH)
        time.sleep(speed)
        GPIO.output(CCW_pin, GPIO.LOW)
        time.sleep(speed)
    
    if (direction == "idle"):
        GPIO.output(CW_pin, GPIO.LOW)
        GPIO.output(CCW_pin, GPIO.LOW)   
        

try:    																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																			
        while True:
#         print("move cw")
#         GPIO.output(CCW_pin, GPIO.HIGH)
#         GPIO.output(19, GPIO.LOW)
            generate_pulse(10000, 0.00015)
            time.sleep(1)
#         GPIO.output(CW_pin, GPIO.HIGH)
#         time.sleep(1)
#     
#     print("move ccw")
#     GPIO.output(CW_pin, GPIO.LOW)
#     generate_pulse(CCW_pin, 1000, 0.00001)
#     time.sleep(2)
        
#         rotate("CW", 0.1)
        

except KeyboardInterrupt:
    print("Program dihentikan.")

finally:
    GPIO.cleanup()  # Membersihkan konfigurasi GPIO saat program dihentikan

