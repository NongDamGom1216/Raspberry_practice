from _thread import *
import net
import socket

BASE = "/Users/hyunjinjeong/Documents/workspace/received/"
def receive_thread(client_socket, addr):
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

ADDR = ('172.30.1.21', 9999) # 튜플
net.run_server(ADDR, receive_thread)