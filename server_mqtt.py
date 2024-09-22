from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO, emit
import time
from threading import Thread

# Flask Webserver
app = Flask(__name__)

# socket to send data to web client on
socketio = SocketIO(app)

app.config['SECRET_KEY'] = 'secret!'
app.config['MQTT_BROKER_URL'] = 'test.mosquitto.org'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
app.config['MQTT_TLS_ENABLED'] = False  # If your server supports TLS, set it True

# MQTT topic to subscribe to
mqtt_topic = 'vish/ultrasonic'

# Initialize Flask-MQTT and SocketIO
socketio = SocketIO(app)
mqtt = Mqtt(app)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt.subscribe(mqtt_topic)  # subscribe to the MQTT topic
    else:
        print('Bad connection. Code:', rc)

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)  # Emit MQTT data to the web client

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('Client connected')
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
