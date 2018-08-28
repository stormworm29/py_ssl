#!/usr/bin/python3
import socket,ssl,pprint
def interact(connstream):
	connstream.sendall(b"Hello this is a message")
	data = connstream.recv(1024)
	pprint.pprint(data.decode("ascii"))
def main():
	ip = '<server_ip'
	port = 12345
	context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
	context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	context.verify_mode = ssl.CERT_REQUIRED
	context.load_verify_locations("name.crt")
	connstream = context.wrap_socket(socket.socket(socket.AF_INET)) 
	connstream.connect((ip,port))
	try:
		interact(connstream)
	finally:
		connstream.shutdown(socket.SHUT_RDWR)
		connstream.close()
if __name__ == '__main__':
	main()
