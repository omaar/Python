import socket

HOST = '10.16.50.10'
PORT = 6030

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind((HOST, PORT))
mysocket.listen(2)
connection, address = mysocket.accept()

print("Cliente: ", address)

while 1:
    data = connection.recv(1024)
    if not data:
    	break
    print(data.decode("utf-8"))
    connection.send("Puto en el que lo lea!!".encode("utf-8"))
connection.close()