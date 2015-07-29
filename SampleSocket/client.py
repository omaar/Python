import socket

HOST = '10.16.50.39' #Se especifica la ip del servidor
PORT = 6030        #Puerto por el cual el cliente se va a comunicar

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Se crea una instancia del un socket
mysocket.connect((HOST, PORT))

data = raw_input("Escribe un saludo: ")
mysocket.send(data.encode("utf8"))
data = mysocket.recv(1024)

mysocket.close()

print ('Received', repr(data))