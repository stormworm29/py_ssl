#!/usr/bin/python3
import socket,ssl,pprint
def interact(connstream):
	data = connstream.read()
	pprint.pprint(data.decode("ascii"))
	connstream.sendall(b"Okay that's cool")
def main():
	ip = ''
	port = 12345
	context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
	context.load_cert_chain(certfile="name.crt", keyfile="key.pem")
	bindsocket = socket.socket()
	bindsocket.bind((ip, port))
	bindsocket.listen(5)
	newsocket, fromaddr = bindsocket.accept()
	connstream = context.wrap_socket(newsocket, server_side=True)
	try:
    		interact(connstream)
	finally:
	       	connstream.shutdown(socket.SHUT_RDWR)
        	connstream.close()
if __name__ == '__main__':
	main()
