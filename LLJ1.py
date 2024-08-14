import sounddevice as sd
import wave

def gravar_audio(nome_arquivo,duracao_segundos,taxa_amostragem=44100):
    audio_data=sd.rec(int(duracao_segundos*taxa_amostragem))
    print("Comece a falar")
    sd.wait()

    with wave.open(nome_arquivo,'wb')as wf:
        wf.setnchannels(1)
        wf.setframerate(taxa_amostragem)
        wf.setsampwidth(4)
        wf.writeframes(audio_data.tobytes())
    print(f"audio gravado com sucesso em'{nome_arquivo}'")
def principal():
    nome_arquivo="gravacao_audio.wav"
    duracao_segundos=5
    gravar_audio(nome_arquivo,duracao_segundos)
principal()
