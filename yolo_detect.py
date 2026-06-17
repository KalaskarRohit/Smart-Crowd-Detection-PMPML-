import cv2
import time
import sqlite3
from ultralytics import YOLO
from twilio.rest import Client
from datetime import datetime

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load bus video
cap = cv2.VideoCapture("bus_crowd.mp4")  # Replace with actual video path

# Twilio API Credentials (Get from Twilio dashboard)
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE = "your_twilio_phone_number"
ADMIN_PHONE = "controller_phone_number"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Threshold for full bus
PASSENGER_THRESHOLD = 40

# Database Setup
conn = sqlite3.connect("bus_data.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS bus_crowd (
        time TEXT,
        route TEXT,
        count INTEGER,
        status TEXT
    )
""")
conn.commit()


def update_db(route, count):
    status = "Full" if count >= PASSENGER_THRESHOLD else "Available"
    cursor.execute("INSERT INTO bus_crowd VALUES (?, ?, ?, ?)",
                   (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), route, count, status))
    conn.commit()


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    person_count = sum(1 for obj in results[0].boxes.data if int(obj[-1]) == 0)

    # Display results
    annotated_frame = results[0].plot()
    cv2.putText(annotated_frame, f"Passengers: {person_count}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Bus Crowd Detection", annotated_frame)

    # Store data in database
    update_db("Route 10", person_count)

    # Send alert if bus is full
    if person_count >= PASSENGER_THRESHOLD:
        message = client.messages.create(
            body=f"Bus is full with {person_count} passengers.",
            from_=TWILIO_PHONE,
            to=ADMIN_PHONE
        )
        print("🚨 Alert Sent:", message.sid)
        time.sleep(60)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
conn.close()
cv2.destroyAllWindows()
