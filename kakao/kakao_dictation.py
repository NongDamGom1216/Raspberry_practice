import requests
import json
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

# 샘플 다운로드 https://developers.kakao.com/docs/latest/ko/voice/rest-api

rest_api_key = '91993241356264156056f235e6563db3'
headers = {
    "Content-Type": "application/octet-stream",
    # 바이트 타입
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
    # KakaoAK 다음 띄어쓰기 포함
}

# 음성 파일의 데이터 값
with open('heykakao.wav', 'rb') as fp:
    audio = fp.read()
    # res = requests.post(kakao_speech_url, headers=headers, data=audio)


# 최종 추출 값 나타내기

# ------------------------------------------------
# 방법1
# 슬라이싱 res.text[:] 

# result_json_string = res.text[
#     res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1
#     # index 함수는 finalresult 값이 있으면 시작 인덱스를 리턴, 그러나 발음이라던가 오류로 인해 값이 없으면 예외 발생(errorcalled)
#     # -> 보완하기 위해 find 함수 사용
# ]
# result = json.loads(result_json_string)
# print(result)
# print(result['value'])

# ------------------------------------------------
# 방법 2

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

if is_success:
    print('인식 결과:', result['value'])
else:
    print('인식 실패: ', result['value'])