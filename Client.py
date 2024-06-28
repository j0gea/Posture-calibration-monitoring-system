import smbus
import time
import math
import socket

bus = smbus.SMBus(1)

address = 0x53
x_adr= 0x32
y_adr= 0x34
z_adr= 0x36

HOST = '0.0.0.0'
PORT = 1234

def init_ADXL345():
    bus.write_byte_data(address, 0x2D, 0x08)

def measure_acc(adr):
    acc0 = bus.read_byte_data(address, adr)
    acc1 = bus.read_byte_data(address, adr+ 1)
    acc= (acc1 << 8) + acc0

    if acc > 0x1FF:
        acc= (65536 -acc) * -1
    acc= acc* 3.9 / 1000
    return acc

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

try:
    init_ADXL345()

    while True:
        x_acc= measure_acc(x_adr)
        y_acc= measure_acc(y_adr)
        z_acc= measure_acc(z_adr)
        
        ax = x_acc
        ay = y_acc
        az = z_acc
        
        try:
            yAngle = math.atan( ay / (math.sqrt(pow(ax, 2) + pow(az, 2))))

            yAngle *= 180.00
            yAngle /= 3.141592
            
        except:
            yAngle = 80

        print(yAngle)

        if (yAngle < 75):
            s.send(str(yAngle).encode())

        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass
