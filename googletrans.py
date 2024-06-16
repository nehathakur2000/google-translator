import gtts
from playsound import playsound
import googletrans

print(googletrans.LANGUAGES)
a = gtts.gTTS("hlo everyone",lang="hi")

a.save("myfile.mp3")
playsound("myfile.mp3")


