import serial
import numpy as np
import pandas as pd
import random

# Change this to match your Arduino's Serial Port (Check in Arduino IDE: Tools -> Port)
SERIAL_PORT = "COM7"  # For Windows (Change if needed)
# SERIAL_PORT = "/dev/ttyUSB0"  # For Linux/Mac

BAUD_RATE = 115200
NUM_SAMPLES = 2000
data = []


# Open Serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
print("Waiting for data...")

while len(data) < NUM_SAMPLES:
    line = ser.readline().decode(errors="ignore").strip()
    if line.isdigit():  # Ensure it's a valid HR value
        hr_value = int(line)
        data.append(hr_value)
        print(f"Received: {hr_value}",len(data))

    elif line == "Done":
        break  # Stop when Arduino finishes sending data

# Close Serial connection
ser.close()
print("Data collection completed.")


# Convert to NumPy array for calculations
data = np.array(data)

# Compute Z-score normalization
mean = np.mean(data)
std_dev = np.std(data)
normalized_hr = (data - mean) / std_dev

# Save to CSV file
df = pd.DataFrame([normalized_hr], columns=range(2000))

# Save to CSV without index and header
csv_filename = "heart_rate_data.csv"
df.to_csv(csv_filename, index=False, header=True, sep=",")

print(f"CSV file saved: {csv_filename}")
