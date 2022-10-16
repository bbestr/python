import socket

def main():
    #建立socket
    tcp_scoket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立连接

    tcp_scoket.connect(("192.168.31.241",7890))
    #姐发消息
    while True:
        data = input("输入发送的消息:")
        tcp_scoket.send(data.encode("utf-8"))

        recv_data = tcp_scoket.recv(4096)
        print("回复" ,recv_data.decode("utf-8"))

    #断开连接
    tcp_scoket.close()
if __name__ == '__main__':
    main()