import socket

def main():
    #建立socket
    tcp_scoket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立连接
    tcp_scoket.connect(("192.168.56.1",8080))
    #姐发消息
    data = input("输入发送的消息:")
    tcp_scoket.send(data.encode("GBK"))

    recv_data = tcp_scoket.recv(1024)
    print("回复:%s" %(recv_data.decode("GBK")))
    #断开连接
    tcp_scoket.close()
if __name__ == '__main__':
    main()