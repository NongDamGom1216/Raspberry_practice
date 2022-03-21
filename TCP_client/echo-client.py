import socket
HOST = '172.30.1.21' # 서버의 IP주소(PC)
PORT = 9999
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버와 연결(튜플)
client_socket.connect((HOST, PORT))
# 성공하면 연결, 실패하면 예외

# 메시지 전송
client_socket.sendall('안녕'.encode())

# 메시지 수신
data = client_socket.recv(1024)
print('Received', repr(data.decode()))

client_socket.close()