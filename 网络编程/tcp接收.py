import socket

def main():
    #建立套接字
    #bind
    #listen  监听  (等待 tcp 客户端 连接)
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket.bind(("",7890))
    tcp_socket.listen(124)

    while True:
        #等待接收 accept(返回值一个元祖) = (新建的套接字,数据包)
        print("----------等待连接--------")
        #accept_group是新建立的套接字(1对1 的连接)  accept_addr接收的客户端 (ip,端口)信息
        accept_group,accept_addr = tcp_socket.accept()
        print("-----------连接成功--------")


        #核心业务
        #获取数据  并回复
        recv_data = accept_group.recv(1024)
        print("回复:", recv_data.decode("utf-8"))
        if recv_data:
            accept_group.send("收到收到".encode("utf-8"))
        else:
            break

        #关闭套接字
        accept_group.close()
        print("一次接发结束!\n")


    tcp_socket.close()

if __name__ == '__main__':
    main()