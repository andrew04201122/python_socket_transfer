import socket

IP = '192.168.0.193'
PORT = 8501
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    """ Connecting to the server. """
    client.connect(ADDR)

    """ Opening and reading the file data. """
    ##################################

    print('start send image')
    imgFile = open("test.png", "rb")
    while True:
        imgData = imgFile.readline(512)
        if not imgData:
            break  
        client.send(imgData)
    imgFile.close()
    print('transmit end')
    ##################################

    client.close()  
    print('client close')


if __name__ == "__main__":
    main()
