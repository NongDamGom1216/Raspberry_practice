from os import path
from sys import stderr

file_path = '/home/pi/my_video.h264'

# 디렉토리 경로 얻기
dir_path = path.dirname(file_path)
print('디렉토리 경로:', dir_path)

# 파일명 얻기
file_name = path.basename(file_path)
print('파일명:', file_name)

# 경로와 파일명
result = path.split(file_path)
print('경로와 파일명:', result)

# 확장자와 나머지 분리
result = path.splitext(file_path)
print('확장자 분리:', result)

# 확장명 변경
dest_path = result[0] + '.mp4'
print('변환된 파일명:', dest_path)

# MP4Box -add <src> <dst>
cmd = f"MP4BOX -add '{file_path}' '{dest_path}'"
print(cmd)

# 확장명 변경 함수
import subprocess

def convert_to_mp4(src):
    dst = path.splitext(src)[0] + '.mp4'
    cmd = f"MP4Box -add '{src}' '{dst}'"
    # 대소문자 구분
    # subprocess.run(cmd, shell = True, stderr=subprocess.DEVNULL) # 코드 간편화
    result = subprocess.run(cmd, shell = True)
    # subprocess는 정의한 명령어를 운영체제한테 명령하도록 한다
    return not result.returncode, dst
    # 첫 번째 요소는 성공 여부에 대한 true, false

result, dst = convert_to_mp4('my_video.h264')
if result:
    print('변환 파일:', dst)
else:
    print('변환 실패')