# import pyttsx3

# engine = pyttsx3.init()

# print("🤖 Robo Speaker Ready!")
# text = input("What should I say? ")

# engine.say(text)
# engine.runAndWait()
import os

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1 Created by Harry")

    while True:
        x = input("Enter what you want me to pronounce (q to quit): ")

        if x.lower() == "q":
            print("Goodbye 👋")
            break

        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'

        os.system(command)