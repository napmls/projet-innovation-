import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything:")
    audio = r.listen(source)
    try:
        t=r.recognize_google(audio,language='ar-AR')
        print(t)
        f=open('text.txt','a',encoding='utf-8')
        f.writelines(t+'\n')
        f.close()
        

    except:
        print("Sorry could not recognize your voice")
    