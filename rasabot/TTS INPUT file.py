#TTS INPUT file
#TTS Component
import pyttsx3
from typing import Any, Text, Dict, List
import os
engine = pyttsx3.init() # object creation
while True:

    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    #print (rate)                        #printing current voice rate
    engine.setProperty('rate', 120)     # setting up new voice rate


    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    #print (volume)                          #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    #Text="Hello, Welcome to Novagenie"
    Text=input()
    engine.say(Text)
    #engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()


    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file(Text, 'test.wav')
    engine.runAndWait()
    os.remove('test.wav')
    