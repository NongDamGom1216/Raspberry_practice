# net.py의 함수를 활용한 TCP 연결

import net
import socket

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

ADDR = ('172.30.1.21', 9999) # 튜플
net.run_server(ADDR, threaded)

