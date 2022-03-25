# import 부분은 만들어보기
# 수행 평가

import a_util
import kakao

def main():
    audio = a_util.record_audio(5) # 5초 간 녹음
    is_success, result = kakao.recognize(audio) # 음성 인식 실행

    if is_success:
        print('인식결과', result)
    
    else:
        # 음성 합성으로 오디오 출력
        a_util.play_text_audio('다시 말씀해주세요.')

main()