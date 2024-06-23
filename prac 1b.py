from gtts import gTTS
import os

f = open('file.txt')
x=f.read()
langauge='en'
audio=gTTS(text=x,lang=langauge)
audio.save("wishes.wav")
os.system("wishes.wav")
print("program executed succesfully.")
