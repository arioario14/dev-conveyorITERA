import RPi.GPIO as GPIO
import time

# Pin untuk Rotary Encoder
ENCODER_A = 7  # Pin A pada encoder (gunakan GPIO 20)
ENCODER_B = 1  # Pin B pada encoder (gunakan GPIO 21)

# Konstanta
RESOLUTION = 2000  # Resolusi encoder (2000 langkah per putaran)
MEASURE_INTERVAL = 1.0  # Interval pengukuran dalam detik (1 detik)

# Variabel global
pulse_count = 0  # Jumlah langkah yang terdeteksi
last_time = time.time()  # Waktu terakhir pengukuran

def setup():
    # Setup GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENCODER_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ENCODER_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Setup interrupt untuk mendeteksi perubahan sinyal encoder
    GPIO.add_event_detect(ENCODER_A, GPIO.BOTH, callback=encoder_callback, bouncetime=200)
    GPIO.add_event_detect(ENCODER_B, GPIO.BOTH, callback=encoder_callback, bouncetime=200)

def encoder_callback(channel):
    """
    ISR (Interrupt Service Routine) untuk Rotary Encoder.
    Dipanggil setiap kali ada perubahan pada pin A atau B.
    """
    global pulse_count
    a_state = GPIO.input(ENCODER_A)
    b_state = GPIO.input(ENCODER_B)

    # Tentukan arah putaran
    if a_state == b_state:
        pulse_count += 1  # Searah jarum jam (CW)
    else:
        pulse_count -= 1  # Berlawanan arah jarum jam (CCW)

def calculate_rpm():
    """
    Hitung RPM berdasarkan jumlah langkah yang terdeteksi dalam interval waktu tertentu.
    """
    global pulse_count, last_time

    # Hitung waktu yang telah berlalu
    current_time = time.time()
    elapsed_time = current_time - last_time

    if elapsed_time >= MEASURE_INTERVAL:
        # Hitung RPM
        revolutions = pulse_count / RESOLUTION  # Jumlah putaran
        rpm = revolutions * (60 / MEASURE_INTERVAL)  # RPM = putaran/detik * 60

        # Reset penghitung langkah dan waktu
        pulse_count = 0
        last_time = current_time

        # Tampilkan hasil
        print(f"RPM: {rpm:.2f}")

def loop():
    """
    Loop utama untuk membaca dan menghitung RPM.
    """
    try:
        while True:
            calculate_rpm()
            time.sleep(0.1)  # Beri sedikit jeda untuk efisiensi CPU
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    setup()
    loop()
