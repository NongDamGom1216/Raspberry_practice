# 무한 루프를 돌면서
# 사용자로부터 텍스트 입력을 받음
# 입력 받은 문자열을 음성 합성으로 재생

import requests
import io, sys
from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK 91993241356264156056f235e6563db3"
}
while True:
    data = input("문장을 입력하세요 : ")

    DATA = f""" <speak>
    <voice name="WOMAN_DIALOG_BRIGHT">{data}</voice>
    </speak>"""

    res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8'))
    if res.status_code != 200: # 에러를 확인하는 법
        print(res)
        print(res.text)
        sys.exit(0)


    sound = io.BytesIO(res.content)
    song = AudioSegment.from_mp3(sound)
    play(song)