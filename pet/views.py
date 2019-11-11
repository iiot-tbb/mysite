from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import socket
import json
import re
# Create your views here.
app_name='pet'#zeng
def index(request):
    return render(request, 'index.html')
def index2(request):
    return render(request, 'index2.html')
def index3(request):
    return render(request, 'index3.html')
def index4(request):
    return render(request, 'index4.html')
def index5(request):
    return render(request, 'index5.html')
def index6(request):
    return render(request, 'index6.html')
def location(request):
    return HttpResponse("this is the location")
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# get sensor data from socket

# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
HOST = '169.254.89.195'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)




import threading
data = {
    "temperature": 0,
    "humidity": 0,
    "health" : 0,
    "speed": 0
} 
speed_history= []
time_window = 0xFFFF
def get_socket_data():
    global data
    global speed_history
    global time_window
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("running thread")
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data_raw = conn.recv(1024)
                    if not data_raw:
                        break
                    data = json.loads(data_raw.decode('ascii'))
                    #xinjiade
                    if len(speed_history) >= time_window:
                        speed_history.pop(0)
                    speed_history.append(data['speed'])


threading.Thread(target=get_socket_data).start()


def get_sensor_data(request):
    return JsonResponse(data)


def feed(request):
    import json
    HOST = '169.254.233.190'  # The server's hostname or IP address
    PORT = 54321        # The port used by the server
    
    print("feed")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall("feed".encode('ascii'))
    
    return JsonResponse({"status":"ok"})
    
#请求speed历史数据
def get_speed_history(request):
    return JsonResponse({"speed_history": speed_history})