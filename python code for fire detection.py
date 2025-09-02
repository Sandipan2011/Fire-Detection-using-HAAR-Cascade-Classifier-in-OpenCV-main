import numpy as np
import cv2
import serial
import time
import winsound  # For system speaker beep (Windows only)

# Load fire detection cascade
fire_cascade = cv2.CascadeClassifier('cascade.xml')

# Connect to Arduino
ser1 = serial.Serial('COM4', 9600)  # Change COM port if needed

# Start video capture
cap = cv2.VideoCapture(0)
count = 0

# Alpha = contrast, Beta = brightness
alpha = 0.5 # Increase contrast (>1), decrease (<1)
beta = 0.4    # Increase brightness (>0), decrease (<0)

while cap.isOpened():
    ret, img = cap.read()  # Capture frame
    if not ret:
        break

    # Adjust brightness & contrast
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    gray = cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Fire detection
    fire = fire_cascade.detectMultiScale(adjusted, 2, 20)  
    detected = False

    for (x, y, w, h) in fire:
        # Thicker bounding box (Red)
        cv2.rectangle(adjusted, (x, y), (x + w, y + h), (0, 0, 255), 4)

        print('🔥 Fire is detected..! ' + str(count))
        count += 1

        # Send signal to Arduino
        ser1.write(b'p')

        # Play system buzzer sound
        winsound.Beep(1000, 500)  # 1000 Hz for 0.5 seconds

        detected = True
        time.sleep(0.2)  # Small delay

    if not detected:
        ser1.write(b's')  # No fire signal

    cv2.imshow('Fire Detection', adjusted)

    k = cv2.waitKey(100) & 0xff
    if k == 27:  # ESC key to exit
        break

# Cleanup
ser1.close()
cap.release()
cv2.destroyAllWindows()
