import serial
import sys

x = 0

Port = input("What Is The Port (Blank for /dev/ttyUSB0): ")
Room = input("Room NR (Rxxx): ")
Network = input("Network Name (Blank for Student): ")


output = open("CSV/Data.csv", "a")

if Network == "":
    Network = "Student"

if Port == "":
    Port = "/dev/ttyUSB0"

ESP = serial.Serial(Port, 115200)

while True:
    if (x < 32):
        Input = ESP.readline().decode()
        File = Input.split("-")
        output.write(Room+","+File[0]+","+File[1])
        print("RSSI Writing " + str(x))
        if File[0] == Network:
            x = x + 1
        else:
            continue
    else:
        output.close()
        sys.exit("Done")