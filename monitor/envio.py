 
import socket
import sys
from subprocess import Popen, PIPE, STDOUT
import hashlib
# Se crea el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Obtener la direccion ip de la maquina
eventStatus = Popen('ip add | egrep -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/24"', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
outputStatus = eventStatus.communicate()
ip = outputStatus[0].decode('utf-8')
# ip y puerto a utilizar para la conexion
print(ip[:-4])

# se modifica para obtener la MAC
#ip add | grep -B 1 "172.16.44.129/24" | grep "ether" | awk '{print $2}'
eventStatus = Popen("ip add | grep -B 1 "+ip[:-4]+" | grep 'ether' | awk '{print $2}'", shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
outputStatus = eventStatus.communicate()
token = outputStatus[0].decode('utf-8')
token = (token.rstrip('\n')).encode()
m = hashlib.sha1(token)
m = m.hexdigest()

server_address = (ip[:-4], 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
# numero de sockets a escuchar
sock.listen(1)
while True:
    # esperamos la conexion
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('Conexiones desde: ',client_address)
        while True:
            data = connection.recv(45)
            mensaje = data.decode(encoding="ascii", errors="ignore")
            print(mensaje)
            if data:
                print('sending data back to the client {}'.format(client_address))
                connection.sendall(m.encode())
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
