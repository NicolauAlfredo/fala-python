import gtts
from playsound import playsound

with open('frase.txt', 'r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='Pt-br')
        
        # Guardar o arquivo em mp3
        frase.save('frase.mp3')
        
        # Tocar o arquivo mp3
        playsound('frase.mp3')