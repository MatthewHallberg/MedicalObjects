import socket
UDP_IP = "10.215.39.108"
UDP_PORT = 1991
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.connect((UDP_IP, UDP_PORT))

def send_message(message):
	sock.send(message.encode())
	print(message)

def close_socket():
	sock.close()
	print('closing socket')