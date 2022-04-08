import recorder
import kakao

def main():
    audio = recorder.record_audio() # 버튼을 누르면 녹음 시작
    is_success, result = kakao.recognize(audio) # 음성 인식 실행

    if is_success:
        print('인식결과', result)
    
    else:
        # 음성 합성으로 오디오 출력
        recorder.recall("<speak>다시 말씀해주세요.</speak>")

main()