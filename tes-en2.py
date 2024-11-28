import lgpio
import time

# Pin untuk Rotary Encoder
ENCODER_A = 20  # Pin A pada encoder (gunakan GPIO 20)
ENCODER_B = 21  # Pin B pada encoder (gunakan GPIO 21)

# Konstanta
RESOLUTION = 2000  # Resolusi encoder (2000 langkah per putaran)
MEASURE_INTERVAL = 1.0  # Interval pengukuran dalam detik (1 detik)

# Variabel global
pulse_count = 0  # Jumlah langkah yang terdeteksi
last_time = time.time()  # Waktu terakhir pengukuran

# Setup LGPIO
def setup():
    global gpio
    gpio = lgpio.gpiochip_open(0)  # Membuka GPIO chip 0 (GPIO 0-31)

    # Setup pin A dan B sebagai input dengan pull-up
    lgpio.gpio_claim_input(gpio, ENCODER_A)
    lgpio.gpio_claim_input(gpio, ENCODER_B)
    lgpio.gpio_set_pull_up_down(gpio, ENCODER_A, lgpio.PUD_UP)
    lgpio.gpio_set_pull_up_down(gpio, ENCODER_B, lgpio.PUD_UP)

    # Pasang callback untuk mendeteksi perubahan status
    lgpio.gpio_set_interrupt_func(gpio, ENCODER_A, lgpio.EITHER_EDGE, encoder_callback)
    lgpio.gpio_set_interrupt_func(gpio, ENCODER_B, lgpio.EITHER_EDGE, encoder_callback)

def encoder_callback(gpio, pin, level, tick):
    """
    Callback untuk perubahan status pin encoder.
    """
    global pulse_count
    a_state = lgpio.gpio_read(gpio, ENCODER_A)
    b_state = lgpio.gpio_read(gpio, ENCODER_B)

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
        lgpio.gpiochip_close(gpio)  # Menutup chip GPIO saat program berhenti

if __name__ == "__main__":
    setup()
    loop()
