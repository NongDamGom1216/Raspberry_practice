import requests
import io, sys
from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK rest_api_key"
}

DATA = """
<speak>
    그는 그렇게 말했습니다.
    <voice name="WOMAN_DIALOG_BRIGHT">잘 지냈어? 나도 잘 지냈어.</voice>
    <voice name="WOMAN_DIALOG_BRIGHT" speechStyle="SS_ALT_FAST_1">금요일이 좋아요.</voice>
</speak>
"""

res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8'))
if res.status_code != 200: # 에러를 확인하는 법
    print(res)
    print(res.text)
    sys.exit(0)

# 음성 합성 결과를 파일로 저장하기

# with open("result.mp3", "wb") as f:
# f.write(res.content)
#
# 파일에서 재생하기
# song = AudioSegment.from_mp3("./result.mp3")

sound = io.BytesIO(res.content)
song = AudioSegment.from_mp3(sound)
play(song)