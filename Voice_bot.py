import requests
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#sender=input("What is your name?\n")
bot_message=""
message=""
while bot_message != "الله يعاونك":
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything:")
        audio = r.listen(source)
        try:
            message=r.recognize_google(audio,language='ar-AR')
            print("You said : {}".format(message))
        except:
            print("Sorry could not recognize your voice")
        if len(message)==0:
            continue
        print("Sending message now...")

        r=requests.post('http://localhost:5002/webhooks/rest/webhook' , json={"message": message})

        print("Bot says, ",end='')
        for i in r.json():
            bot_message=i['text']
            print(f"{bot_message}")
        f=open('text.txt','a',encoding='utf-8')
        f.writelines(bot_message+'\n')
        obj=gTTS(text=bot_message,lang='ar',slow=False)
        obj.save('text.mp3')
        playsound('text.mp3')