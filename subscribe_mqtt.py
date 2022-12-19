import random
from paho.mqtt import client as mqtt_client
import threading


broker = '43.139.231.248'
port = 1883
topic = "emqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# 连接到Borker
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id) #创建一个mqtt对象
    client.on_connect = on_connect
    client.connect(broker, port) #连接mqtt服务器
    return client

# 订阅函数，设定要订阅的Topic，以及设定接受信息后的回调函数
def subscribe(client: mqtt_client):
    global myGlobalMessage
    global myGlobaltopic
    def on_message(client, userdata, msg):
        # 接收消息后的处理函数
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        myGlobalMessage = msg.payload.decode()
        myGlobaltopic = msg.topic
        print(myGlobalMessage)
        print(myGlobaltopic)
    client.subscribe(topic)
    client.on_message = on_message
    # return a

def run():
    client = connect_mqtt()
    subscribe(client)
    # 网络阻塞，不断接受并调用回调函数处理结果，意味着代码会一直卡在这里接受，所以可以使用多线程来使用
    client.loop_forever()

if __name__ == '__main__':
    payloads = []
    run()