import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print('Conectado!!\n')

namefile = str(input('Arquivo>'))
namefile = 'C:\\lucas\\Downloads\\' + namefile

client.send(namefile.encode())

with open(namefile, 'rb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{namefile} recebido!\n')