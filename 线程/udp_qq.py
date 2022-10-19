import socket
import threading
def recv_msg(udp_socket):
    while True:
        data = udp_socket.recvfrom(1024)
        print(data)


def send_msg(udp_socket,dest_ip,dest_port):
    while True:
        send_data = input("输入要发送的数据:")
        udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))


def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    udp_socket.bind(("",7890))

    dest_ip = input("输入目标ip地址:")
    dest_port = int(input("输入目标端口号:"))

    t2 = threading.Thread(target=recv_msg, args=(udp_socket,))
    t1 = threading.Thread(target=send_msg,args=(udp_socket,dest_ip,dest_port))

    t2.start()
    t1.start()




if __name__ == '__main__':
    main()