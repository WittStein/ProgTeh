import socket
import threading

TARGET_HOST = '127.0.0.1'


def scan_tcp_port(host, port):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.settimeout(1)
    result = tcp_socket.connect_ex((host, port))
    tcp_socket.close()
    if result == 0:
        print(f'TCP Port {port} is OPEN')
    else:
        print(f'TCP Port {port} is CLOSED')


def scan_udp_port(host, port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(1)
    try:
        udp_socket.sendto(b'', (host, port))
        udp_socket.recvfrom(1024)
        print(f'UDP Port {port} is OPEN')
    except socket.timeout:
        print(f'UDP Port {port} is CLOSED')
    except Exception as e:
        print(f'Error scanning UDP Port {port}: {e}')
    finally:
        udp_socket.close()


def scan_ports(host, start_port, end_port, protocol):
    for port in range(start_port, end_port + 1):
        if protocol == 'tcp':
            thread = threading.Thread(target=scan_tcp_port, args=(host, port))
        elif protocol == 'udp':
            thread = threading.Thread(target=scan_udp_port, args=(host, port))

        thread.start()
        thread.join()


if __name__ == '__main__':
    try:
        start_port = int(input("Введите начальный порт: "))
        end_port = int(input("Введите конечный порт: "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print(
                "Пожалуйста, введите корректные значения портов (1-65535) и убедитесь, что начальный порт меньше конечного.")
            exit()

        protocol = input("Выберите протокол (tcp/udp): ").strip().lower()
        if protocol not in ['tcp', 'udp']:
            print("Пожалуйста, выберите корректный протокол: tcp или udp.")
            exit()

        print(f'Scanning {TARGET_HOST} for {protocol.upper()} ports from {start_port} to {end_port}...')
        scan_ports(TARGET_HOST, start_port, end_port, protocol)
    except ValueError:
        print("Пожалуйста, введите числовые значения для портов.")
