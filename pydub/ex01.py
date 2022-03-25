from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file('output.wav', format="wav")
# song = AudioSegment.from_wav('test.wav')
play(song)

# 명령어에 아래와 같이 추가하면 터미널이 깔끔해짐
# 2> /dev/null