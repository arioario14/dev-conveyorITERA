import os
import time

# Path direktori 1-Wire
BASE_DIR = '/sys/bus/w1/devices/'
DEVICE_FOLDER = [d for d in os.listdir(BASE_DIR) if d.startswith('28-')][0]
DEVICE_FILE = f'{BASE_DIR}/{DEVICE_FOLDER}/w1_slave'

def read_temp_raw():
    """Membaca data mentah dari sensor."""
    with open(DEVICE_FILE, 'r') as file:
        lines = file.readlines()
    return lines

def read_temp():
    """Mengonversi data mentah menjadi suhu dalam Celcius."""
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

try:
    while True:
        print(f"Suhu: {read_temp():.2f}°C")
        time.sleep(1)
except IndexError as e:
    print("Sensor tidak terdeteksi")

