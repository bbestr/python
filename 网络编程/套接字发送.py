import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print(udp_socket)
    udp_socket.bind(('',7890))
    while True:
        bshuju = input("输入你要发送的数据: ")
        udp_socket.sendto(bshuju.encode("utf-8"),("192.168.56.1",8080))
        udp_socket.close

if __name__ == "__main__":
    main()