import socket
import random
HOST = "192.168.85.131"
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)

def whichbox(option):
    result = 0
    randinphase = random.randint(1, 3)
    if option == randinphase:
        result = 1
    return result

client, addr =  s.accept()
msg = "----K0$_M@ Challenge----\n"
client.send(msg.encode("utf8"))
try:
    while True:
        client.send("""Choose one? (type "1", "2", "3", "4")\n1. First Box.\n2. Second Box.\n3. Third Box.\n4. Quit Game.\n\n""".encode("utf8"))
        rev = client.recv(1024).decode("utf8")
        rev = rev.rstrip()
        rev = rev.replace("\n", "")
        if int(rev) <= 3 and int(rev) > 0:
            n = whichbox(int(rev))
            if n == 1:
                client.send("You won a cute Griseo.\nAgain?\n".encode("utf8"))
            else:
                client.send("Geez, nothing here. Try again.\n".encode("utf8"))
        elif int(rev) == 4:
            client.send("Cya ^^.".encode("utf8"))
            break
        else:
            client.send("No box like that :D. Choose again.\n".encode("utf8"))
except socket.error as error:
    print("Error occured : ", error)
finally:
    client.close()
s.close()