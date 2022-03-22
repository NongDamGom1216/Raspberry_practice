import os
import socket

HOST = "172.30.1.21"
PORT = 9999

FILE_PATH = "/Users/hyunjinjeong/Documents/workspace/test.jpg"

def file_read(file_path):
    with open(file_path, 'rb') as f:
        while True :
            data = f.read(1024)
            if not data :
                break
            yield data # 제너레이터

# with 문을 쓰면 자동으로 함수를 벗어날 때 자동으로 close

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try :
        s.connect((HOST, PORT))
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