from gtts import gTTS

import os

mytext = "namaku muhammad jeli almuta'ali"
bahasa = "en"

myobj = gTTS(text=mytext, lang=bahasa, slow=False)
myobj.save('perkenalan.mp3')

os.system("mpg321 perkenalan.mp3")
