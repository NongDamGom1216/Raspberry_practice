import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16 # 16비트(2바이트)
CHANNELS = 1
RATE = 48000 # 1초에 sampling

RECORD_SECONDS = 5 # 녹음 시간
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
stream = p.open(input_device_index = 1, # 자신에게 맞는 장치 번호 지정, 생략가능
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
            

print("Start to record the audio.")
frames = []

# 녹음 시간만큼 반복
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK, exception_on_overflow=False) # 녹음
    frames.append(data)

print("Recording is finished.")
stream.stop_stream()
stream.close()
p.terminate() # 녹음 데이터는 frames에 담겨 있음

# wav 파일 저장
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
