from vosk import Model, KaldiRecognizer
import os
import json, pyaudio


model = Model(r"F:/Vol_Playng/Vol_Praving/vosk-model-small-ru-0.22") # полный путь к модели
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, 
    channels=1, 
    rate=16000, 
    input=True, 
    frames_per_buffer=8000
)
stream.start_stream()

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']

for text in listen():

    if 'ваш текст' in text:     #пиши с маленькой буквы а иначе могут быть ошибки
        print('А это будет ответ')
        
   