import socket
import threading
sk=socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen()

while True:
    con,adrr=sk.accept()
    data=con.recv(2048).decode('utf-8')
    url=data.split()[1]
    print(url)


    con.send(b'''HTTP/1.1 200 OK\r\n\r\n<h1>ok</h1>''')
    con.close()

