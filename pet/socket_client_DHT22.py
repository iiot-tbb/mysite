import socket
import json
from time import sleep
import Adafruit_DHT as dht
import random
HOST = '169.254.89.195'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def get_data_json():
    humidity,temperature =dht.read_retry(dht.DHT22,4)
    health=random.uniform(7,10)
    speed=random.uniform(0,10)
    data = {
            'humidity' : humidity,
            'temperature': temperature,
            'health':health,
            'speed':speed
            }
    return json.dumps(data)


while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while True:
                s.sendall(get_data_json().encode('ascii'))
                sleep(1)
    except Exception as e:
        print(e)
        sleep(5)
#     data = s.recv(1024)

# print('Received', repr(data))
