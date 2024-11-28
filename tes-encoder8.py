from gpiozero import Button
from time import time, sleep
from threading import Timer

# Konfigurasi rotary encoder
ENCODER_A = 20  # Pin A pada encoder
ENCODER_B = 21  # Pin B pada encoder
RESOLUTION = 2000  # Resolusi encoder (pulsa per rotasi)

# Variabel global
pulse_count = 0  # Menghitung jumlah pulsa
last_time = time()  # Waktu terakhir diperbarui
rpm = 0  # Nilai RPM

# Fungsi untuk menghitung pulsa pada pin A
def encoder_callback_A():
    global pulse_count
    pulse_count += 1  # Tambahkan jumlah pulsa setiap kali ada perubahan pada pin A

# Fungsi untuk menghitung RPM
def calculate_rpm():
    global pulse_count, last_time, rpm

    current_time = time()  # Catat waktu sekarang
    elapsed_time = current_time - last_time  # Hitung waktu yang telah berlalu

    if elapsed_time > 0:  # Hindari pembagian dengan nol
        # Hitung Pulsa Per Detik (PPS)
        pps = pulse_count / elapsed_time

        # Konversi PPS ke RPM
        rpm = (pps * 60) / RESOLUTION

    # Reset variabel
    pulse_count = 0
    last_time = current_time

    # Cetak nilai RPM
    print(f"RPM: {rpm:.2f}")

    # Jalankan fungsi ini kembali setelah 1 detik
    Timer(1.0, calculate_rpm).start()

# Inisialisasi gpiozero Button untuk Pin A
pin_a = Button(ENCODER_A, pull_up=False)
pin_b = Button(ENCODER_B, pull_up=False)

# Pasang event handler pada pin A untuk menghitung pulsa
pin_a.when_pressed = encoder_callback_A

# Mulai penghitungan RPM
print("Program berjalan. Putar encoder untuk menghitung RPM.")
calculate_rpm()  # Mulai timer untuk menghitung RPM

# Program tetap berjalan sampai dihentikan
try:
    while True:
        sleep(0.1)  # Loop utama tetap berjalan
except KeyboardInterrupt:
    print("Program dihentikan.")
