from pydub import AudioSegment
from pydub.playback import play

# song = AudioSegment.from_file('test.mp3', format="mp3")

f = open('output.mp3', 'rb')
song = AudioSegment.from_mp3(f)
play(song)