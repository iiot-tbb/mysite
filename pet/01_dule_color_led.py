#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
colors1 = [0xFF00, 0x00FF, 0x0FF0, 0xF00F]
#colors1 = [0xFF00, 0x00FF]
colors2 = [0xFF00]
pins = {'pin_R':11, 'pin_G':12}  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in pins:
	GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
	GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
p_G = GPIO.PWM(pins['pin_G'], 2000)

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):   # For example : col = 0x112233
	R_val = (col & 0x1100) >> 8
	G_val = (col & 0x0011) >> 0
	
	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(G_val, 0, 255, 0, 100)
	
	p_R.ChangeDutyCycle(R_val)     # Change duty cycle
	p_G.ChangeDutyCycle(G_val)

def loop():
#	while True:
		for col in colors:
                        setColor(col)
                        time.sleep(0.5)

def destroy():
	p_R.stop()
	p_G.stop()
	for i in pins:
		GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds
	GPIO.cleanup()
def lightOnce():
    for col in colors1:
        setColor(col)
        time.sleep(0.1)

def darkOnce():
    for col in colors2:
        setColor(col)
        time.sleep(0.1)


if __name__ == "__main__":
#	try:
#		loop()
#	except KeyboardInterrupt:
#		destroy()
    import socket
    import json

    # HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    HOST = '169.254.233.190'  # Standard loopback interface address (localhost)
    PORT = 54321        # Port to listen on (non-privileged ports are > 1023)


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(4)
                print(data.decode("ascii"))
                if data.decode("ascii") == "feed":
                    lightOnce()
                    time.sleep(0.2)
                    darkOnce()
		# print(json.loads(data.decode('ascii')))import socket

    '''
    while True:
        i =input()
        if i=='1':
            lightOnce()
        else: pass
        '''
