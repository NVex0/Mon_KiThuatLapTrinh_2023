import socket

ip = "192.168.85.131"

portlist = [20, 21, 22, 23, 25, 53,80, 110, 119, 123, 143, 181, 194, 443]

try:
    for port in portlist:
        s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(port, ":" , "open")
        else:
            print(port, ":", "close")
except socket.error as error:
    print("Error occured: ", error)
finally:
    s.close()