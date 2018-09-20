import sys, socket, threading

class Client:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, HOST, PORT):
        self.server.connect((HOST, PORT))
        clientThread = threading.Thread(target = self.send_message)
        clientThread.daemon = True
        clientThread.start()
        while True:
            message = self.server.recv(1024)
            if not message:
                break
            print(message)

    def send_message(self):
        while True:
            self.server.send(bytes(input(''), 'UTF-8'))






if len(sys.argv) != 3:
    print ("Error: necesitas pasar: archivo, IP, puerto.")
    exit()
if(str(sys.argv[1] == 'localhost')):
    HOST = '127.0.0.1'
else:
    HOST = str(sys.argv[1])
PORT = int(sys.argv[2])
client = Client(HOST, PORT)