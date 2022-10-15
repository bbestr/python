import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("", 7890))
    dest_ip = input("輸入對方ip")
    dest_port = input("輸入對方port")
    while True:
        bshuju = input("输入你要发送的数据: ")

        udp_socket.sendto(bshuju.encode("utf-8"),(dest_ip,int(dest_port)))

        recv = udp_socket.recvfrom(1024)
        print("回復:%s" % recv[0].decode("utf-8"))


    udp_socket.close

if __name__ == "__main__":
    main()