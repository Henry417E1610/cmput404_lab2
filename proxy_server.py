import socket, time, sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_ip(host):
    print(f'Getting IP for {host}')
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Unresolvable host')
        sys.exit()
    
    print(f'IP address for {host} is {ip}')
    return ip

def main():
    ext_host = 'www.google.com'
    port = 80
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start:
        print('Starting proxy server')
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        start.bind((HOST, PORT))
        start.listen(1)
        while True:
            conn, addr = start.accept()
            print("Connecting by", addr)  
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as end:
                print('Connecting to Google')
                ip = get_ip(ext_host)
                end.connect((ip,port))
                send_data = conn.recv(BUFFER_SIZE)
                #print(f"Sending data {send_data} to google")
                end.sendall((send_data))
                end.shutdown(socket.SHUT_WR)
                data = end.recv(BUFFER_SIZE)
                print(f"Sending received data {data} to client")
                conn.send(data)
            conn.close()
                
if __name__ == "__main__":
    main()                