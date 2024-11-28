import wiringpi as wp
import time

# Konfigurasi GPIO untuk pin encoder (menggunakan nomor BCM)
ENCODER_A = 20  # Pin A pada encoder
ENCODER_B = 21  # Pin B pada encoder

# Konstanta
RESOLUTION = 2000  # Resolusi encoder (2000 langkah per putaran)
MEASURE_INTERVAL = 1.0  # Interval pengukuran dalam detik (1 detik)

# Variabel global
pulse_count = 0  # Jumlah langkah yang terdeteksi
last_time = time.time()  # Waktu terakhir pengukuran

def encoder_callback(pin):
    """
    Callback untuk rotary encoder.
    Dipanggil setiap kali ada perubahan status pada pin.
    """
    global pulse_count
    a_state = wp.digitalRead(ENCODER_A)
    b_state = wp.digitalRead(ENCODER_B)

    # Tentukan arah putaran
    if a_state == b_state:
        pulse_count += 1  # Searah jarum jam (CW)
    else:
        pulse_count -= 1  # Berlawanan arah jarum jam (CCW)

def setup():
    """
    Konfigurasi WiringPi dan interrupt untuk rotary encoder.
    """
    wp.wiringPiSetupGpio()  # Gunakan nomor GPIO berdasarkan BCM

    # Setup pin sebagai input
    wp.pinMode(ENCODER_A, wp.INPUT)
    wp.pinMode(ENCODER_B, wp.INPUT)

    # Aktifkan pull-up resistor pada pin A dan B
    wp.pullUpDnControl(ENCODER_A, wp.PUD_UP)
    wp.pullUpDnControl(ENCODER_B, wp.PUD_UP)

    # Setup interrupt untuk mendeteksi perubahan pada pin A dan B
    wp.wiringPiISR(ENCODER_A, wp.INT_EDGE_BOTH, lambda: encoder_callback(ENCODER_A))
    wp.wiringPiISR(ENCODER_B, wp.INT_EDGE_BOTH, lambda: encoder_callback(ENCODER_B))

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
            calculate_rpm()  # Hitung RPM setiap interval
            time.sleep(0.1)   # Beri sedikit jeda untuk efisiensi CPU
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")

if __name__ == "__main__":
    setup()
    loop()
