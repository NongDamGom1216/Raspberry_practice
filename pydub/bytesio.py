# wav -> mp3 BytesIO 활용하기

from pydub import AudioSegment
from pydub.playback import play
import io
import requests

with open('output.wav', 'rb') as f:
  wavMem = io.BytesIO(f.read()) # 초기 데이터

mp3Mem = io.BytesIO()
sound = AudioSegment.from_file(wavMem, format="wav")
sound.export(mp3Mem, format="mp3", codec="libmp3lame")

print(mp3Mem.tell()) # 파일 크기 출력
mp3Mem.seek(0) # seek() 읽기, 쓰기 위치를 옮길 때

song = AudioSegment.from_mp3(mp3Mem)
play(song)