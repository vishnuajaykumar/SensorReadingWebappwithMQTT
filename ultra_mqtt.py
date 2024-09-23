import serial
import paho.mqtt.client as mqtt

# Serial configuration
ser = serial.Serial('/dev/ttyUSB0', 9600)

# MQTT broker details
MQTT_BROKER_HOST = "test.mosquitto.org"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = "vish/ultrasonic"  #replace it with your MQTT link

# Initialize MQTT client
client = mqtt.Client()

def read_and_publish():
    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            print(line)  
            
           
            client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)
            client.publish(MQTT_TOPIC, line)
            client.disconnect()

    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    read_and_publish()
