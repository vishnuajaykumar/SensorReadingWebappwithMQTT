import serial
import paho.mqtt.client as mqtt

# Serial configuration
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust the serial port accordingly

# MQTT broker details
MQTT_BROKER_HOST = "test.mosquitto.org"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = "vish/ultrasonic"  # Updated MQTT topic

# Initialize MQTT client
client = mqtt.Client()

def read_and_publish():
    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            print(line)  # Print the received data to the console
            
            # Publish the data to the MQTT topic "vish_ultrasonic"
            client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)
            client.publish(MQTT_TOPIC, line)
            client.disconnect()

    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    read_and_publish()
