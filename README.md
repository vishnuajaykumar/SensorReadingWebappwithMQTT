# Ultrasonic Sensor Real-Time Display with MQTT

## Overview
This project uses an ultrasonic sensor connected to an Arduino, which publishes sensor readings via MQTT. These readings are then displayed in real time on a web interface. The server-side logic is managed with Python, while the client-side interaction, including visual feedback and real-time updates, is handled by JavaScript (Socket.IO).

---

## Components
- **Arduino with Ultrasonic Sensor**: The hardware that reads distance measurements.
- **MQTT Explorer**: A tool to monitor and debug MQTT messages.
- **Server Script (`server_mqtt.py`)**: A Python script that subscribes to the sensor's MQTT topic and broadcasts updates to connected clients.
- **Web Interface (`index.html`)**: The front-end interface where the sensor data is displayed.
- **Client Script (`client.js`)**: JavaScript responsible for real-time updates and visual feedback on the web page.
- **Socket.IO**: Enables real-time communication between the server and client.
  
---

## Setup

### Hardware Requirements
- Arduino board
- Ultrasonic sensor
- Any computer as a server

### Software Requirements
- Arduino IDE for sketch upload
- Python with libraries: `paho-mqtt`, `flask`, `flask_socketio`
- MQTT Explorer to monitor the data flow
- A modern web browser to display the interface

### Installation
1. **Arduino Setup**:
   - Connect the ultrasonic sensor to the Arduino as per the provided `sketch_oct24a.ino`.
   - Upload the Arduino sketch to the board.

2. **Server Setup**:
   - Install Python and the required libraries (`pip install paho-mqtt flask flask_socketio`).
   - Run `server_mqtt.py` to start listening for sensor data and broadcasting it over the web.

3. **Web Interface**:
   - Open `index.html` in any modern web browser to view the live sensor data.

4. **MQTT Explorer**:
   - Use MQTT Explorer to connect to your MQTT broker and subscribe to the topic your Arduino publishes to. This lets you view the raw data as it comes from the sensor.

---

## Usage
Once everything is set up:
- The Arduino reads distances and sends them to the MQTT broker.
- The server subscribes to the MQTT broker, receives these distances, and relays them to the web interface using Socket.IO.
- The web interface dynamically updates the displayed distance and changes the text color based on sensor values.

---

## Files Explained

### Arduino Sketch (`arduino.ino`)
- This sketch runs on the Arduino and reads data from the ultrasonic sensor. It sends the sensor readings to the MQTT broker.

### Server Script (`server_mqtt.py`)
- The Python script that acts as the server. It subscribes to the MQTT broker, receives ultrasonic sensor readings, and broadcasts the data to clients using Socket.IO.

### Web Interface Files:
1. **`index.html`**: The front-end web page that shows the real-time sensor data.
2. **`client.js`**:
   - This JavaScript file listens for incoming data from the server (using Socket.IO).
   - It parses the MQTT message payload and displays the sensor value in real time on the web page.
   - It includes a **color mapping function** to indicate the range of the sensor value visually. For example:
     - Low values appear **green**.
     - Medium values appear **yellow**.
     - High values appear **red**, providing a quick visual alert if necessary.
  
3. **`socket.io.js`**: The Socket.IO client-side library is responsible for real-time communication with the server.

---

## Color Mapping Logic
The `client.js` file uses a function that maps sensor values to colors for easy interpretation:

- **White**: Value < 25
- **Green**: 25 ≤ Value < 50
- **Yellow**: 50 ≤ Value < 75
- **Orange**: 75 ≤ Value < 100
- **Red**: Value ≥ 100

This allows users to quickly see if the sensor readings are in a safe or concerning range.

---

## Future Enhancements
- Add more sensors for multi-dimensional data collection.
- Implement data logging on the server for historical analysis.
- Enhance the web interface with charts and graphs for better data visualization.

---

## Conclusion
This project is a practical example of real-time data monitoring using an ultrasonic sensor and MQTT. The combination of Socket.IO for live updates and MQTT for communication makes this a versatile setup for Internet of Things (IoT) applications.



```bash
Computer
  │
  │ USB Cable
  │
  ▼
Adafruit Metro Mini
  ┌────────────────────────────┐
  │                            │
  │   ┌──────────────┐          │
  │   │  Trig Pin 9  │──────────┼──> Trig Pin on Ultrasonic Sensor
  │   └──────────────┘          │
  │                            │
  │   ┌──────────────┐          │
  │   │ Echo Pin 10  │──────────┼──> Echo Pin on Ultrasonic Sensor
  │   └──────────────┘          │
  │                            │
  │   ┌──────────────┐          │
  │   │    GND       │──────────┼──> Ground for Ultrasonic Sensor
  │   └──────────────┘          │
  │                            │
  │   ┌──────────────┐          │
  │   │   5V (USB)   │──────────┼──> Power for Ultrasonic Sensor
  │   └──────────────┘          │
  └────────────────────────────┘

Ultrasonic Sensor (HC-SR04)
  ┌────────────────────────────┐
  │  │                         │
  │  │ Trig Pin (from Pin 9) ───> Send trigger signal
  │  │                         │
  │  │ Echo Pin (to Pin 10) ────> Receive echo signal
  │  │                         │
  │  │ Power (from 5V)          ──> Power the sensor
  │  │                         │
  │  │ Ground (shared GND)      ──> Connect to GND
  └────────────────────────────┘
```
