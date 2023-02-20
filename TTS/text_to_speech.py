import numpy as np
import os
from gtts import gTTS

# Global variables
PWD = os.getcwd()
TXT_INPUT_DIR = ''
TXT_ABS_PATH = ''

# Functions
def parseTxtFile(text_file_name, is_immediate_playback, audio_file_name=None):
    if audio_file_name == None and not is_immediate_playback:
        print("[ERROR] No file name was given. File name is needed for non-immediate playback option!")
        return -1

    elif audio_file_name == None and is_immediate_playback:
        audio_file_name = 'direct.mp3'
    
    text_contents = ''
    with open(text_file_name) as file_content: # type(file_content) -> _io.TextIOWrapper
        text_contents += file_content.read() # type(file_content.read()) -> str    

    if is_immediate_playback:
        directSpeechPlay(text_contents, audio_file_name)
    else:
        appendToFile(text_contents, audio_file_name)


def appendToFile(contents, file_name):
    speech = gTTS(contents, lang='en')
    speech_abs_path = os.path.abspath(file_name)
    val = speech.save(speech_abs_path) # for MSDOS-based systems
    print(f'Speech file location: {speech_abs_path}')

def directSpeechPlay(contents, file_name): 
    speech_abs_path = os.path.abspath(file_name)
    appendToFile(contents, speech_abs_path)
    os.system(f'start {speech_abs_path}') 
    print(f'Speech file location: {speech_abs_path}')

# Main
## VALUES ARE FOR TESTING ONLY 
text_fname = 'hello.txt' 
speech_fname = 'speak_non-immediate.mp3'
parseTxtFile(text_file_name=text_fname, is_immediate_playback=False, audio_file_name=speech_fname)