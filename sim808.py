import serial
import time,sys
import datetime

SERIAL_PORT = "/dev/ttyS0"
ser=serial.Serial(SERIAL_PORT, baudrate=9600)

def millis():
    milliSeconds=int(round(time.time()*1000))
    return milliSeconds

def sendTabData(command, timeout,debug):
    ser.write(command.encode())
    t = millis()
    i=0
    
    while (t+timeout)>millis():
        while ser.inWaiting():
            
            dat=""
            c=ser.readline()
            a=c.decode()
                
            x = "+CGNSINF:" in a
            if x:
                b=(a.split(","))
                state=b[1]
                latitude=b[3]
                longitude=b[4]
                
    return state,latitude,longitude
DEBUG=True
ser.write(("AT+CSMP=17,167,0,0\r\n").encode())
time.sleep(0.1)
ser.write(("AT+CMGF=1\r\n").encode())
time.sleep(0.4)
ser.write(("AT+CGNSPWR=1\r\n").encode())
time.sleep(0.05)
ser.write(("AT+CGNSSEQ=RMC\r\n").encode())
time.sleep(0.15)

while True:
    stat,lat,long=sendTabData("AT+CGNSINF\r\n",1000,DEBUG)
    if stat=="1":
        print(lat)
        print(long)
