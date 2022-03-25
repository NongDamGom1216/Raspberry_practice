# pyaudio에서 했었던 음성이 바로 출력됐던 프로그램 -> playback

import sounddevice as sd

duration = 5.5 # seconds

# indata = 녹음된 numpy 배열
def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata
    # start, end가 생략 -> 기존에 가지고 있던 전체 데이터를 삭제하고 새로운 녹음 데이터를 넣는다
    # outdata = 출력할 numpy 배열

with sd.Stream(channels=1, callback=callback):
    sd.sleep(int(duration * 1000))