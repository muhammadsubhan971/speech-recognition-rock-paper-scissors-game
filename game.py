import pyttsx3 as pt
import speech_recognition as sr
import random as rd

a=["rock","paper","Caesar"]
option=["Rock","paper","scissor"]
cli=["i won The taste of victory is addictive","yes yes i won","oh wow i won","i won machine is better then you"]
ab=["oh no you just win so not be over","you win it's just my failure","oh I loss","oh you won"]
nb=["oh nobody win","oh it's just coincidence","seriously our thinking quiet similar","okay both think similar turn"]
mn=0
ai=0
voice=pt.init()
voice.runAndWait()
re=sr.Recognizer()
print("so let's ready for playing the game : ")
voice.say("so let's ready for playing the game")
voice.runAndWait()
for i in range(5):
    try:
        n=rd.randint(0,2)
        lu=rd.randint(0,3)
        with sr.Microphone() as mic:
            re.adjust_for_ambient_noise(mic,duration=0.4)
            awz=re.listen(mic)
            suno=re.recognize_google(awz)
        if suno.lower() == "rock":
            print("you said :",suno)
            print(option[n])
            voice.say(option[n])
            voice.runAndWait()
            if n == 0:
                print("nobody wins".capitalize())
                voice.say(nb[lu])
                voice.runAndWait()
                voice.runAndWait()
                # n=rd.randint(0,2)
            elif n == 2:
                print("you wins".capitalize())
                voice.say(ab[lu])
                voice.runAndWait()
                voice.runAndWait()
                mn=mn+1
                # n=rd.randint(0,2)
            elif n == 1:
                print("i won")
                voice.say(cli[lu])#rock,paoer,scissor
                voice.runAndWait()
                voice.runAndWait()
                ai=ai+1
                # n=rd.randint(0,2)
        elif suno.lower() == "paper":
            print("you said :",suno)
            print(option[n])
            voice.say(option[n])
            voice.runAndWait()
            if n == 2:
                print("i won")
                voice.say(cli[lu])
                voice.runAndWait()
                voice.runAndWait()
                ai=ai+1
                # n=rd.randint(0,2)
            elif n == 1:
                print("nobody win's")
                voice.say(nb[lu])
                voice.runAndWait()
                voice.runAndWait()
                # n=rd.randint(0,2)
            elif n == 0:
                print("you won")
                voice.say(ab[lu])
                voice.runAndWait()
                voice.runAndWait()
                mn=mn+1
                # n=rd.randint(0,2)
        elif suno.lower() == "caesar":
            print("you said :",suno)
            print(option[n])
            voice.say(option[n])
            voice.runAndWait()
            if n == 0:
                print("i won")
                voice.say(cli[lu])
                voice.runAndWait()
                voice.runAndWait()
                ai=ai+1
                # n=rd.randint(0,2)
            elif n == 1:
                print("you won")
                voice.say(ab[lu])
                voice.runAndWait()
                voice.runAndWait()
                mn=mn+1
                n=rd.randint(0,2)
            elif n == 2:
                print("nobody wins")
                voice.say(nb[lu])
                voice.runAndWait()
                voice.runAndWait()
                # n=rd.randint(0,2)
        else:
            voice.say("you say anything else")
            voice.runAndWait()
        if i != 4:
            voice.say("now ready for next turn")
            voice.runAndWait()
            print("\n speak:")
        # n=rd.randint(0,2)
        # # lu=rd.randint(0,3)
    except sr.UnknownValueError:
        print("sorry")
        continue

print(f"""Result
        Player:{mn}
        AI:{ai}""")
if ai > mn:
    print("Ai wins")
    voice.say("yes man I won the contest")
    voice.runAndWait()
elif ai < mn:
    print("You win")
    voice.say("congras man you are the winner")
    voice.runAndWait()
else:
    print("nobody won")
    voice.say("ok it's just nobody achieve it")
    voice.runAndWait()



