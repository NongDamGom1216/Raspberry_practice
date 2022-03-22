from net import send_file

ADDR = ('172.30.1.21', 9999)
FILE_PATH = "/Users/hyunjinjeong/Documents/workspace/test.jpg"

send_file(ADDR, FILE_PATH)