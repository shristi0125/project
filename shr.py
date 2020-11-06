import webbrowser
import os
import pyttsx3
import speech_recognition as sr
import pyscreenshot as imagegrab

os.system("figlet DAZZLERS")
print("----------------WELCOME----------------------------\n")
print("\n")

print("Features:-")
os.system("espeak -s 125 -v en+f4 'hello welcome everyone ' ")
os.system("espeak -s 100 -v en+f4 'welcome to magic world' ")
print("features provided are listed as follow")
os.system('zenity --info --text "Want To See Your Fortune\n\nWant To Run Train\n\nWant To Run Calendar\n\nWant To Listen A Story\n\nWant To see Animal"') 

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("start saying..")
        audio=r.listen(source)
        print("speech done")
        p = r.recognize_google(audio)
        print(p)
        
    
    if (("show" in p) or ("tell" in p) or ("open" in p)) and (("fortune" in p) or ("lucky" in p)):
        os.system("fortune")
        
    elif (("show" in p) or ("start" in p)) and ("train" in p):
        os.system("sl")
    elif (("start" in p) or ("show" in p)) and ("calendar" in p):
        os.system("zenity --calendar")

    elif (("show" in p) or ("start" in p)) and ("train" in p):
        os.system("sl")
    elif (("show" in p) or ("tell" in p)) and ("story" in p):
        os.system("telnet towel.blinkenlights.nl")
    elif (("show" in p) or ("tell" in p)) and ("animal" in p):
        os.system("cowsay I LIKE CODING")
    elif ("exit" in p) or ("stop" in p) or ("quit" in p):
        print("dont support ask again")
        os.system("zenity --warning")
    else:
        os.system("zenity --error")



