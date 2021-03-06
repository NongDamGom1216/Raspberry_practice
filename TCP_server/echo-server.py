import socket
from threading import Thread

HOST = '172.30.1.21'
PORT = 9999

# 주소 체계(address family): IPv4, 소켓 타입: TCP

# 동시 접속한 수만큼 스레드가 동작
def threaded(client_socket, addr):
       # 접속한 클라이언트의 주소 출력
    print('Connected by', addr)

    while True:
        # 메시지 수신 대기
        data = client_socket.recv(1024) # 최대 길이, 이 때 데이터는 바이트 배열
        if not data: # 연결이 끊겼을 때 None
            break

        # data(byte array), 바이트 배열을 문자열로 변환하여 출력
        print('Received from', addr, data.decode())
        # 받은 문자열을 다시 클라이언트로 전송(에코)
        client_socket.sendall(data) 
        # 수신할 때는 receive

    client_socket.close()



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Address_family
# 이미 열린 포트 충돌시 재사용 옵션 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.settimeout(0.3)

server_socket.bind((HOST, PORT))
server_socket.listen()


while True:

    try:
        # accept 함수에서 대기, 클라이언트 접속 시 새로운 소켓을 리턴
        client_socket, addr = server_socket.accept()
        # 실제 메시지를 주고받는 소켓은 클라이언트 소켓
        # 서버 소켓은 서버 연결
    except socket.timeout: # 예외 처리가 발생하면 socket 타임아웃이 호출
        continue
    
    # 스레드로 실행, 매개변수는 튜플이나 리스트로 전달
    t = Thread(target=threaded, args=(client_socket, addr))
    t.start()
 
server_socket.close()