import pyttsx3
import time
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--voice", required=False, default=16, help="Defines the voice")
ap.add_argument("-r", "--rate", required=False, default=125, help="Defines the speaking rate")
ap.add_argument("-l", "--volume", required=False, default=1.0, help="Defines the volume level")
ap.add_argument("-m", "--msg", required=False, default="Hello", help="Defines the message to speak")
ap.add_argument("-n", "--name", required=False, default="Jason", help="Defines your name")
args = vars(ap.parse_args())

name = "JARVIS"

engine = pyttsx3.init()
voices = engine.getProperty('voices')


def get_voice():
    try:
        cur_voice = pyttsx3.voice.Voice
        return cur_voice.name
    except Exception as e:
        print(e)
        return engine.getProperty('voice')


def set_voice(value):
    engine.setProperty('voice', voices[value].id)
    engine.runAndWait()


def get_rate():
    return engine.getProperty('rate')


def set_rate(value):
    engine.setProperty('rate', value)
    engine.runAndWait()


def get_volume():
    return engine.getProperty('volume')


def set_volume(value):
    engine.setProperty('volume', value)
    engine.runAndWait()


if __name__ == "__main__":
    my_name = args["name"]
    set_rate(int(args["rate"]))
    set_volume(float(args["volume"]))
    set_voice(int(args["voice"]))

    msg = f"Hello {my_name}, my name is {name}. The current volumn level is {get_volume()}. My speaking rate is {get_rate()}. I'm currently using a {get_voice()} voice."
    print(f"{name} -> {msg}")
    engine.say(msg, name)
    engine.runAndWait()
    time.sleep(1.0)