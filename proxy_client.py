import socket
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024
payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connection(address):
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect(address)
        soc.sendall(payload.encode())
        soc.shutdown(socket.SHUT_WR)        
        
        data = soc.recv(BUFFER_SIZE)
        print(data)
    
    except Exception as e:
        print(e)
    finally:
        soc.close()
        
def main():
    connection((HOST, PORT))
    
if __name__ == "__main__":
    main()
