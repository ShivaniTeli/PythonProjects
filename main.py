import pyttsx3

print("Welcome to RoboSpeaker 1.1 Created by Shivani ")

# Initialize the engine once
engine = pyttsx3.init()

while True:
    x = input("Enter what you want me to speak: ")
    if x == "q":  # Quit if 'q' is entered (case-insensitive)
        engine.say("Bye bye Buddy")
        engine.runAndWait()
        break
    # Speak the input text
    engine.say(x)
    engine.runAndWait()

print("Goodbye!")
