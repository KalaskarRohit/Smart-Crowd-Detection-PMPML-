# 🚍 TransitVision AI: Real-Time Crowd Detection & Passenger Analytics Using YOLOv8

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object_Detection-green)
![Computer Vision](https://img.shields.io/badge/Computer_Vision-OpenCV-orange)
![Edge AI](https://img.shields.io/badge/Edge_AI-Raspberry_Pi-red)
![Industry Sponsored](https://img.shields.io/badge/Industry_Sponsored-PMPML-purple)

## 📌 Overview

TransitVision AI is an industry-sponsored Artificial Intelligence and Computer Vision project developed to address crowd management challenges in public transportation systems.

The project leverages **YOLOv8**, **OpenCV**, and **Edge AI** technologies to perform real-time passenger detection, crowd density estimation, and occupancy analytics inside public buses. By combining Deep Learning with intelligent transportation monitoring, the system enables safer, smarter, and more efficient public transit operations.

This project demonstrates the practical application of AI/ML in Smart City infrastructure and real-world transportation systems.

---

## 🏢 Industry Sponsorship

This project was developed under a sponsored initiative supported by **Pune Mahanagar Parivahan Mahamandal Ltd. (PMPML)**.

The objective was to explore how Artificial Intelligence, Computer Vision, and Edge Computing can be used to improve:

* Passenger safety
* Occupancy monitoring
* Crowd management
* Public transport analytics
* Operational decision-making

---

# 🎯 Problem Statement

Urban transportation systems frequently face challenges such as:

* Overcrowded buses
* Passenger discomfort
* Safety concerns
* Inefficient resource allocation
* Lack of real-time occupancy information
* Difficulty in monitoring passenger flow

Traditional monitoring methods rely heavily on manual observation and provide limited actionable insights.

TransitVision AI addresses these issues through automated crowd detection and real-time passenger analytics powered by Deep Learning.

---

# 🧠 AI/ML Concepts Used

### Computer Vision

Real-time video stream analysis and passenger detection.

### Deep Learning

YOLOv8 neural network for object detection and localization.

### Object Detection

Identification of passengers and objects using bounding boxes.

### Crowd Analytics

Real-time crowd density estimation and occupancy tracking.

### Edge AI

Deployment of AI models on Raspberry Pi for on-device inference.

### Real-Time Monitoring

Continuous analysis of live video streams for intelligent transportation monitoring.

---

# ✨ Key Features

✅ Real-Time Passenger Detection

✅ Crowd Density Estimation

✅ Occupancy Monitoring

✅ YOLOv8-Based Object Detection

✅ Edge AI Deployment

✅ Automated Alert Generation

✅ Passenger Analytics

✅ Smart Transportation Monitoring

✅ Lightweight and Cost-Effective Architecture

✅ Public Transport Safety Enhancement

---

# 🏗 System Architecture

```text
Camera Feed
     │
     ▼
Video Frame Acquisition
     │
     ▼
YOLOv8 Object Detection
     │
     ▼
Passenger Detection & Counting
     │
     ▼
Crowd Density Analysis
     │
     ▼
Occupancy Estimation
     │
     ▼
Alert Generation
     │
     ▼
Analytics Dashboard / Cloud Storage
```

---

# 🛠 Technology Stack

## Artificial Intelligence

* YOLOv8
* Deep Learning
* Computer Vision
* Object Detection

## Programming Language

* Python

## Libraries

* Ultralytics
* OpenCV
* NumPy
* Picamera2

## Edge Computing

* Raspberry Pi 4

## Notification System

* Twilio API

## Development Tools

* Raspberry Pi OS
* PuTTY
* Git
* GitHub

---

# 📊 Methodology

## 1. Data Acquisition

Video frames are continuously captured using the IMX219 camera module installed within the bus environment.

---

## 2. Object Detection

Each frame is processed by the YOLOv8 model.

The model:

* Detects passengers
* Detects bags
* Detects onboard objects
* Generates bounding boxes
* Produces confidence scores

---

## 3. Passenger Counting

Detected passengers are counted in real time.

Passenger occupancy is estimated dynamically through continuous frame analysis.

---

## 4. Crowd Density Analysis

The system monitors passenger density and occupancy levels.

When crowd levels exceed predefined thresholds, the system identifies potential overcrowding conditions.

---

## 5. Alert Generation

Twilio API integration enables automated SMS notifications whenever abnormal crowd situations are detected.

A cooldown mechanism prevents repeated notifications.

---

# 📷 Detection Pipeline

```text
Video Input
     │
     ▼
Frame Capture
     │
     ▼
YOLOv8 Inference
     │
     ▼
Person Detection
     │
     ▼
Passenger Count Calculation
     │
     ▼
Crowd Density Estimation
     │
     ▼
Occupancy Monitoring
     │
     ▼
Alert Generation
```

---

# 📈 Results

## Real-Time Object Detection

The YOLOv8 model successfully detected:

* Passengers
* Bags
* Onboard Objects

under varying environmental conditions.

---

## Crowd Monitoring

The system effectively monitored passenger density and occupancy levels in real time.

This allowed continuous crowd analytics within public transportation environments.

---

## Edge AI Deployment

The system was successfully deployed on Raspberry Pi hardware, demonstrating the feasibility of running lightweight AI models on low-cost edge devices.

### Deployment Specifications

* Resolution: 640 × 480
* Frame Rate: 30 FPS
* Device: Raspberry Pi 4
* Camera: IMX219 Camera Module

---

## Alert System Performance

Twilio SMS notifications were successfully delivered in real time whenever crowd thresholds were exceeded.

This improved situational awareness and response capabilities.

---

# 🚀 Applications

### Smart Cities

AI-driven transportation monitoring and analytics.

### Public Transportation

Passenger counting and occupancy estimation.

### Crowd Intelligence

Real-time crowd density monitoring.

### Urban Mobility

Transportation optimization through AI insights.

### Safety Monitoring

Overcrowding detection and passenger safety enhancement.

### Edge AI Systems

Deployment of lightweight AI models on embedded hardware.

---

# 📁 Repository Structure

```text
TransitVision-AI/
│
├── images/
│   ├── system_architecture.png
│   ├── hardware_setup.png
│   ├── object_detection_1.png
│   ├── object_detection_2.png
│   ├── twilio_alert.png
│
├── models/
│   └── yolov8n.pt
│
├── src/
│   ├── detection.py
│   ├── counting.py
│   ├── alerts.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🔮 Future Scope

* Multi-Camera Passenger Tracking
* Cloud-Based Analytics Dashboard
* Passenger Flow Prediction
* AI-Based Demand Forecasting
* Occupancy Heatmaps
* Real-Time Route Optimization
* Smart City Integration
* Advanced YOLO Models
* Predictive Transportation Analytics

---

# 🏆 Key Achievements

* Developed an AI-powered crowd analytics solution for public transportation.
* Applied YOLOv8 for real-time passenger detection and monitoring.
* Successfully demonstrated Edge AI deployment on Raspberry Pi.
* Integrated automated alert mechanisms using Twilio.
* Built a practical Computer Vision solution addressing real-world transportation challenges.
* Completed under an industry-sponsored initiative supported by PMPML.

---

# 👨‍💻 Author

## Rohit Kalaskar

B.Tech Student
Vishwakarma Institute of Technology, Pune

Interests:

* Artificial Intelligence
* Machine Learning
* Computer Vision
* Deep Learning
* Edge AI
* Full Stack Development

LinkedIn: [www.linkedin.com/in/rohitkalaskar](http://www.linkedin.com/in/rohitkalaskar)

---

# 📄 License

This project is licensed under the Apache 2.0 License.

---

## ⭐ If you found this project interesting, consider giving it a star!
