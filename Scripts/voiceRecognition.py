import speech_recognition as voiceRecognition
s = voiceRecognition.Recognizer()

with voiceRecognition.Microphone() as source:
    print("Di algo...")
    audio = s.listen(source)
    
    try:
        text = s.recognize_google(audio, language='es-ES')
        print("Que es lo que dijiste: {}".format(text))
    except:
        print("Lo siento!, No pude entender!")