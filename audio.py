from gtts import gTTS
import os

def audiobook(text_file, audio_file):
    with open(text_file, 'r',encoding='utf-8') as f:
        text=f.read()

    tts=gTTS(text=text, lang='en')
    
    tts.save(audio_file)
    print(f'audio_file save as {audio_file}')
text_file='poem.txt'
audio_file='poem.mp3'

audiobook(text_file,audio_file)
os.system(f'start{audio_file}')