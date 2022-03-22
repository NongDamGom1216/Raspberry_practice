import socket
from threading import Thread
import os

def run_server(addr, thread_fn):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Address_family
    # 이미 열린 포트 충돌시 재사용 옵션 설정
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.settimeout(0.3)

    server_socket.bind(addr)
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
        t = Thread(target=thread_fn, args=(client_socket, addr))
        t.start()
    
    server_socket.close()

def file_read(file_path):
    with open(file_path, 'rb') as f:
        while True :
            data = f.read(1024)
            if not data :
                break
            yield data # 제너레이터

def send_file(addr, FILE_PATH):
    # with 문을 쓰면 자동으로 함수를 벗어날 때 자동으로 close
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try :
            s.connect(addr)
            fileSize = os.path.getsize(FILE_PATH)

            # 파일명, 파일 크기 전송
            file_name = FILE_PATH.split('/')[-1] # 파일명, 이런 생각 어떻게...?
            s.sendall(f'{file_name}/{fileSize}'.encode()) # 문자열로 변환시키고 인코딩

            # 준비 상태 수신
            isready = s.recv(1024).decode() 
            if isready == "ready":
                # 파일 전송
                for data in file_read(FILE_PATH):
                    s.sendall(data)
                
                print(file_name, "/", fileSize)
                print("전송완료")

        except Exception as e:
            print(e)

BASE = "/Users/hyunjinjeong/Documents/workspace/received/"

def receive_file(client_socket, addr):
    try :
        # 파일명, 파일 크기 수신
        data = client_socket.recv(1024)
        file_name, size = data.decode().split('/')
        size = int(size)

        print('file name: ', file_name)
        print("수신할 파일 크기:", size)

        # 준비상태 전송
        client_socket.send("ready".encode())

        # 파일 수신
        total_size = 0
        FILE_PATH = BASE + file_name
        with open(FILE_PATH, "wb") as f:
                while True:
                    data = client_socket.recv(1024)
                    f.write(data)
                    total_size += len(data)
                    if total_size >= size: break

                print(f"수신 완료: {file_name} / {total_size} bytes")
    except Exception as e:
        print(e)
    finally:
        client_socket.close()