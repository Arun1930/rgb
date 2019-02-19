import time
import RPi.GPIO as GPIO

from socketIO_client_nexus import SocketIO
socketIO = SocketIO("192.168.0.16",3000)

def on_connect():
    print("connect")

def on_disconnect():
    print("disconnect")

def on_light(*args):
    print("light",args)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.LOW)
    print('Hi')
    time.sleep(1)

    GPIO.output(21, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(21, GPIO.LOW)
    print('hello')
    time.sleep(1)

socketIO.on('connect',on_connect())
socketIO.on('disconnect',on_disconnect())
socketIO.on('reconnect',on_reconnect())

while True:
    socketIO.on('light',on_light())
    socketIO.wait(seconds=1)
    

