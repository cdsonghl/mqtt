import random
import time

from paho.mqtt import client as mqtt_client

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id) #创建一个mqtt对象
    client.on_connect = on_connect
    client.connect(broker, port) #连接mqtt服务器
    return client

def publish(client,data):
    msg = f"messages: {data}"
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    data_need_pub = 0 #需要发送的数据
    while True:
        time.sleep(1)
        publish(client,data_need_pub)
        data_need_pub += 1

if __name__ == '__main__':
    broker = '43.139.231.248'
    port = 1883
    topic = "emqtt"
    # generate client ID with pub prefix randomly
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    run()