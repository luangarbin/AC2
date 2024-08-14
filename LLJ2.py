import sounddevice as sd
import wave
import speech_recognition as sr

def guardar_audio(nome_arquivo,duracao,taxa=44100):
    audio=sd.rec(int(duracao*taxa),samplerate=taxa,channels=1,dtype='int16')
    print("diga seu nome:")
    sd.wait()
    with wave.open(nome_arquivo,'wb') as wb:
        wb.setsampwidth(2)
        wb.setnchannels(1)
        wb.writeframes(audio.tobytes())

    print("gravado!")

guardar_audio("audio.wav",10)

def trancrever_audio():
    recognizer = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        print("Processando audio...")
        audio=recognizer.record(source)
        texto=recognizer.recognize_google(audio,language="pt-BR")
        print(texto)
transcrever_audio()
