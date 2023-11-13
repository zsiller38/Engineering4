#type: ignore
# Zachary Siller
# Morse Code Part 1 11/8/2023

import time
import board
import digitalio

led=digitalio.DigitalInOut(board.GP16) #Lines 7-10 led set up
led.direction=digitalio.Direction.OUTPUT

translatedtext = ""
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}
modifier = .25
dot = modifier
dash = 3*modifier
cseperator = modifier
space = 3*modifier
slash = 5*modifier

def translator (Itext):
    translatedtext = ""
    for letter in Itext:
        letterU = letter.upper()
        #print(MORSE_CODE[letterU])
        translatedtext = translatedtext + " " + MORSE_CODE[letterU]
    print(translatedtext)
    for character in translatedtext:
        if character = ".":
            led.value=True #Turns light on and off
            time.sleep(dot)
            led.value=False
            time.sleep(cseperator)
        elif character = "-":
            led.value=True #Turns light on and off
            time.sleep(dash)
            led.value=False
            time.sleep(cseperator)
        elif character = " ":
            led.value=True #Turns light on and off
            time.sleep(space)
            led.value=False
            time.sleep(cseperator)
        else:
            led.value=True #Turns light on and off
            time.sleep(slash)
            led.value=False
            time.sleep(cseperator)

while True:
    writeI = input('Write your message or press -q to exit: ')
    translatedtext = translator(writeI)
    if writeI == "-q":
        print("exit loop")
        break
    else:
        print(translatedtext)