import requests
import json
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

# 샘플 다운로드 https://developers.kakao.com/docs/latest/ko/voice/rest-api

rest_api_key = 'rest_api_key'
headers = {
    "Content-Type": "application/octet-stream",
    # 바이트 타입
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
    # KakaoAK 다음 띄어쓰기 포함
}
def recognize(audio):
    # 음성 파일의 데이터 값
    with open('output.wav', 'rb') as fp:
        audio = fp.read()
        # res = requests.post(kakao_speech_url, headers=headers, data=audio)

    res = requests.post(kakao_speech_url, headers=headers, data=audio)

    is_success = True
    start = res.text.find('{"type":"finalResult"')
    end = res.text.rindex('}')+1

    if start == -1:
        start = res.text.find('{"type":"errorCalled"')
        is_success = False

    # res.text[:] 슬라이싱
    result_json_string = res.text[start:end]
    result = json.loads(result_json_string)

    return is_success, result