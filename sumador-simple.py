#!/usr/bin/python
# Christian Bermejo Guerrero
# Ejercicio 14.5 Sumador simple en dos fases

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1235))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

boolean = True;
try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        peticion = recvSocket.recv(2048).decode('utf-8')
        print (peticion)
        print ('Answering back...')

        rec = peticion.split()[1][1:]
        if (rec == "favicon.ico"):
            recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n" +
                            "<html><body>Not Found" +
                            "</body></html>" +
                            "\r\n",'utf-8'))
            recvSocket.close()
            continue
        if (boolean):
            if (str.isdigit(rec)):
                rec1 = rec
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>El sumando 1 es: " +
                                rec1 +
                                ". Introduce otro numero para obtener la suma" +
                                "</p>" +
                                "</body></html>" +
                                "\r\n",'utf-8'))
                recvSocket.close()
                boolean = False
            else :
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>No es un numero." +
                                "Vuelve a introducir otro numero" +
                                "</p>" +
                                "</body></html>" +
                                "\r\n",'utf-8'))
                recvSocket.close()
        else :
            if (str.isdigit(rec)):
                rec2 = rec
                suma = int(rec1) + int(rec2)
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>El sumando 2 es: " +
                                str(rec2) +
                                ". La suma de: " + str(rec1) +
                                " + " +
                                str(rec2) + " = " +
                                str(suma) +
                                "</p>" +
                                "</body></html>" +
                                "\r\n",'utf-8'))
                recvSocket.close()
                boolean = True
            else :
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>No es un numero." +
                                "Vuelve a introducir otro numero" +
                                "</p>" +
                                "</body></html>" +
                                "\r\n",'utf-8'))
                recvSocket.close()
except KeyboardInterrupt:
    print ("\nClosing binded socket")
    mySocket.close()
