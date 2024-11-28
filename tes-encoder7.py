from gpiozero import Button
from signal import pause

# Pin untuk Rotary Encoder
ENCODER_A = 20  # Pin A pada encoder
ENCODER_B = 21  # Pin B pada encoder

# Variabel global untuk posisi dan arah
position = 0
direction = None

# Fungsi untuk menangani perubahan status pada Pin A
def encoder_callback_A():
    global position, direction
    if pin_b.is_pressed:  # Pin B HIGH
        position += 1
        direction = "CW"  # Clockwise
    else:  # Pin B LOW
        position -= 1
        direction = "CCW"  # Counterclockwise
    print(f"Posisi: {position}, Arah: {direction}")

# Fungsi untuk menangani perubahan status pada Pin B
def encoder_callback_B():
    global position, direction
    if pin_a.is_pressed:  # Pin A HIGH
        position -= 1
        direction = "CCW"  # Counterclockwise
    else:  # Pin A LOW
        position += 1
        direction = "CW"  # Clockwise
    print(f"Posisi: {position}, Arah: {direction}")

# Inisialisasi gpiozero Button untuk Pin A dan B
pin_a = Button(ENCODER_A, pull_up=False)  # pull_up=False karena menggunakan pull-up eksternal
pin_b = Button(ENCODER_B, pull_up=False)

# Pasang event handler untuk mendeteksi perubahan status
pin_a.when_pressed = encoder_callback_A
pin_b.when_pressed = encoder_callback_B

print("Program berjalan. Putar encoder untuk melihat posisi dan arah.")

# Program tetap berjalan sampai dihentikan
pause()
