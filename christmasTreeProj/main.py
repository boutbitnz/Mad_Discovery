# lightcontroller (Christmas tree) voice controller for Build Madison 2015
# Works with python 3.4

# Newest version of my code. 
# The API key is in this file, 
# don't post that directly to Github.
    # Jack Willis (The yung man that joined the group.)
    # My Github username is jackwillis. 
    # I'll add everyone to the wit.ai project later, 
    # but the key is below:
    # MGJX5IAV3TME26J7P7QG2UO2Y2FYISYF
    

import time
import pprint
import sys

import wave
import pyaudio
import threading

import speech_recognition as sr

import lightcontroller

def phrase_callback(r, audio, controller):
    print("Captured a phrase")

    try:
        start = time.time()
        wit_response = r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)
        end = time.time()

        print("Wit.ai responded in", end - start, "seconds")

        intent, value = parse_wit_response(wit_response)

        if intent == "quit":
            sys.exit("Bye!")
        else:
            lc_response = controller.command(intent, value)
            print("lightcontroller response:", lc_response)

    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai; {0}".format(e))
    except IndexError as e:
        print(e)


def get_single_value_from_entities(entities, name):
    value = ""

    value_entity = entities.get(name)

    print("value_entity:", value_entity)

    if value_entity:
        value = value_entity[0].get("value")

    return value


def parse_wit_response(response):
    outcomes = response["outcomes"]
    pprint.pprint(outcomes, indent=3)

    if len(outcomes) == 0:
        raise IndexError("No outcomes given in Wit response")

    outcome = sorted(outcomes, key=lambda outcome: outcome["confidence"])[-1]

    confidence = outcome["confidence"]
    intent = outcome["intent"]
    entities = outcome["entities"]

    if confidence < 0.5 or intent == "UNKNOWN":
        print("I don't understand")

        return "", ""
    else:
        print("Success recognizing an intent!")

    if intent in ("change_color", "blink"):
        value = get_single_value_from_entities(entities, "color")
    elif intent == "rainbow":
        value = str(get_single_value_from_entities(entities, "number"))
    else:
        value = ""

    print("intent, value:", intent, ",", value)

    replies = {
        "turn_on": "Turning it on.",
        "turn_off": "Turning it off.",
        "change_color": "Changing the color to " + value,
        "rainbow": "Rainbow-ing " + value + " times",
        "test": "Running the test",
        "blink": "Blinking " + value,
    }

    reply = replies.get(intent, "")

    print(reply)

    return intent, value


if __name__ == "__main__":
    controller = lightcontroller.Controller()

    r = sr.Recognizer()
    r.pause_threshold = 0.5

    mic = sr.Microphone(sample_rate=8000)

    with mic as source:
        r.adjust_for_ambient_noise(source)

    print("Say something!")

    stop_listening = r.listen_in_background(mic, lambda r, audio: phrase_callback(r, audio, controller))

    while True: time.sleep(0.1)









