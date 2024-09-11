from sequence import Sequence
from pattern import Pattern
from pydub import AudioSegment
# test = Sequence()
test = Pattern("test")
test2 = Sequence()
print(test2.BPM)
print(test.audio)

audio = AudioSegment.from_wav(f"./assets/matrix.wav")
audio2 = AudioSegment.from_wav(f"./assets/strawberry.wav")

audio3 = audio + audio2

audio3.export("audio3.mp3", format="mp3")
# this works :OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# lightwork audio work ig
