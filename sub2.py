# subscriber
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('192.168.0.106', 1883)

def on_connect(client, userdata, flags, rc):
    print("Connected to a broker!")
    client.subscribe("LINTANGtopic/test")

def on_message(client, userdata, message):
    print(message.payload.decode())
     # Receive data and decode it
    print("topic:", message.topic)
    print("Message received: " + message.payload.decode('utf-8'))
    data = json.loads(message.payload.decode('utf-8'))
    print(data)


    if message.topic == "/start":
        print("i am in start topic" , data)
        print("start command received")
        
        print(data)

    if message.topic == "/stop":
        print("i am stop topic" , data)
        print("stop command received")
        
        print(data)


while True:
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
