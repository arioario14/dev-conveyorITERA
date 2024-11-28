import RPi.GPIO as GPIO
import time

# Pin untuk CW dan CCW
CW_pin = 26
CCW_pin = 19
AllWindingOff_pin = 13
CurrentCutback_pin = 6


Speed = 0.005   # 5 - 500 microseconds, 0.005 detik = 5000 mikrodetik

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Menggunakan penomoran BCM untuk GPIO
GPIO.setup(CW_pin, GPIO.OUT)
GPIO.setup(CCW_pin, GPIO.OUT)
GPIO.setup(AllWindingOff_pin, GPIO.OUT)
GPIO.setup(CurrentCutback_pin, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(AllWindingOff_pin, GPIO.HIGH)
GPIO.output(CurrentCutback_pin, GPIO.HIGH)

GPIO.output(CCW_pin, GPIO.LOW)
GPIO.output(CW_pin, GPIO.LOW)



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
        rotate("CW", 0.000001)
        # Arah searah jarum jam (CW)
        
#         GPIO.output(CW_pin, GPIO.LOW) # io untuk pin cw 
#         GPIO.output(CCW_pin, GPIO.HIGH) # io untuk pin ccw
        # delay dalam detik (microseconds diubah ke detik)
#         time.sleep(Speed)
        # Arah berlawanan jarum jam (CCW)
#         GPIO.output(CCW_pin, GPIO.LOW) # io untuk pin ccw
#         GPIO.output(AllWindingOff_pin, GPIO.LOW)
#         GPIO.output(CurrentCutback_pin, GPIO.LOW) 
#         GPIO.output(CCW_pin, GPIO.LOW)
        
        

except KeyboardInterrupt:
    print("Program dihentikan.")

finally:
    GPIO.cleanup()  # Membersihkan konfigurasi GPIO saat program dihentikan
