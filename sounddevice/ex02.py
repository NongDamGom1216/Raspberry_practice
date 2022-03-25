# 주로 쓰이는 방법!!!

import sounddevice as sd
import soundfile as sf
from io import BytesIO

fs = 44100 # Sample rate
seconds = 3 # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
# int(seconds * fs)의 크기 : 샘플링 갯수
# myrecording 은 결과가 담기는 numpy 배열
sd.wait() # Wait until recording is finished

# print(type(myrecording), myrecording.shape, myrecording.dtype)

mem_wav = BytesIO()
sf.write(mem_wav, myrecording, fs, format="wav")  # Save as WAV file

print(mem_wav.tell())
mem_wav.seek(0)

# mem_wav 전송