# 녹음한 파일을 바로 재생

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16 # 16비트(2바이트)
CHANNELS = 1
RATE = 48000 # 1초에 sampling

RECORD_SECONDS = 5 # 녹음 시간
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

in_stream = p.open(input_device_index = 1,
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

out_stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True)

print("Start to record the audio")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = in_stream.read(CHUNK, exception_on_overflow=False) # 녹음
    out_stream.write(data)
    frames.append(data)

print("Recording is finished")

out_stream.stop_stream()
out_stream.close()
p.terminate()