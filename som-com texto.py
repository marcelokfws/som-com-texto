from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(
    text = 'Meu primeiro som gerado com python',
    lang = language
)

sp.save(audio)
playsound(audio)