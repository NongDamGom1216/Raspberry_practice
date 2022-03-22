# 전송하고자 하는 파일이 여러 개일 때

from net import send_file

ADDR = ('172.30.1.21', 9999)

files = [
    "/Users/hyunjinjeong/Documents/workspace/test.jpg",
    "/Users/hyunjinjeong/Documents/workspace/test2.jpg",
    "/Users/hyunjinjeong/Documents/workspace/test3.jpg"
]

# # 방법1
# for file in files:
#     send_file(ADDR, file)

# 방법2 (thread)
from threading import Thread
for file in files:
    t = Thread(target=send_file, args=(ADDR, file))
    t.start()