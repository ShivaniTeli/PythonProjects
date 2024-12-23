import requests
import json
import pyttsx3

engine = pyttsx3.init()

while(True):
    engine.say("Enter City")
    engine.runAndWait()
    city = input("Enter City:\t")

    if city == "None" or city == "null":
        engine.say("Thank you for using WeatherApp! Bye Bye!")
        print("Thank you for using WeatherApp! Bye Bye!")
        engine.runAndWait()
        break
    url = f"http://api.weatherapi.com/v1/current.json?key=7f275a7a0ada4c7b89680459241812&q=bulk={city}"
    r = requests.get(url)
    # print(r.text)
    wdic = json.loads(r.text)
    w = (wdic["current"]["temp_c"])
    print(w)

    engine.say(f"'The current weather in {city} is {w} degrees'")
    print(f"The current weather in {city} is {w} degrees")
    engine.runAndWait()
