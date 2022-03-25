# wav -> mp3

from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file('output.wav', format="wav")
sound.export('output.mp3', format="mp3", codec="libmp3lame")


# # mp3 -> wav
# from pydub import AudioSegment
# from pydub.playback import play
# sound = AudioSegment.from_file('test.mp3', format="mp3")
# sound.export('converted.wav', format="wav")