import socket

HOST = "192.168.85.131"
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

try:
    while True:
        receive = s.recv(1024).decode("utf8")
        print(receive)
        msg = input()
        s.send(msg.encode("utf8"))
        msg = msg.rstrip()
        if msg == "4":
            print(s.recv(1024).decode("utf8"))
            break
except socket.error as error:
    print("Error occured: ", error)
finally:
    s.close()