#type: ignore
# Zachary Siller
# Morse Code Part 1 11/8/2023
translatedtext = ""
MORSE_CODE = { 'A':'.-', 'B':'-...',    #Dictionary containing translations
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

def translator (Itext): #Function that translates text letter by letter
    translatedtext = ""
    for letter in Itext: #Runs for each letter and turns them into capital letters because the dictionary uses capitals.
        letterU = letter.upper()
        #print(MORSE_CODE[letterU])
        translatedtext = translatedtext + " " + MORSE_CODE[letterU]
    print(translatedtext)
    
while True:
    writeI = input('Write your message or press -q to exit: ')
    translatedtext = translator(writeI)
    if writeI == "-q": #checks if -q is written and exits the code if so
        print("exit loop")
        break
    else:
        print(translatedtext)