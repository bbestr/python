import socket
def main():
    #创建soket
    udpsocket1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #初始本地信息 bind  绑定
    addre = ('',7788)
    udpsocket1.bind(addre)

    #接受数据 是一个元祖(,) 第一个是 数据 ,第二个是发送方信息
    test_shuju = udpsocket1.recvfrom(1024)

    recv_data = test_shuju[0]
    recv_sender = test_shuju[1]

    print("%s 发送了 %s" %(recv_sender,recv_data.decode("utf-8")))

    udpsocket1.close
if __name__ == '__main__':
    main()