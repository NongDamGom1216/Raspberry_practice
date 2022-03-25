import pyaudio
import wave
import sys

CHUNK = 1024
WAVE_FILENAME = "output.wav"

wf = wave.open(WAVE_FILENAME, 'rb')

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data: # 데이터를 다 읽을 때 까지 반복
    stream.write(data) # 사운드 출력
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()