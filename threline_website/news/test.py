import socket

HOST = '127.0.0.1'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with server:
	server.bind((HOST, PORT))
	server.listen(5)

	conn, addr = server.accept()

	with conn:
		print('You are connected to', addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break 
			conn.sendall(data)


