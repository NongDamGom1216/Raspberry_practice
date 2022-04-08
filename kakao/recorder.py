import speech_recognition as sr
import requests
import io, sys
from pydub import AudioSegment
from pydub.playback import play
from gpiozero import Button
from signal import pause

button = Button(21, bounce_time=0.03)

WAVE_OUTPUT_FILENAME = "output.wav"

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK your API KEY"
}
DATA=""

def record_audio():
    recognizer = sr.Recognizer()

    # 마이크 설정
    microphone = sr.Microphone(sample_rate=16000)

    with microphone as source:
        print("Start to record the audio.")
        result = recognizer.listen(source)
        audio = result.get_wav_data()

    # 음성을 받아서 wav 파일로 저장
    print("Recording is finished.")
    with open(WAVE_OUTPUT_FILENAME, "wb") as f:
        f.write(audio)
    
    return audio

def recall(DATA):
    res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8'))
    if res.status_code != 200: # 에러를 확인하는 법
        print(res)
        print(res.text)
        sys.exit(0)

    sound = io.BytesIO(res.content)
    song = AudioSegment.from_mp3(sound)
    play(song)


# 버튼을 누른 경우 녹음 시작
button.when_pressed = record_audio

pause()