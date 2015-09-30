#!usr/bin/python
# @AUTHOR: Benjamin S. Meyers
# @DESCRIPTION: A simple function to translate an English string into soundex. https://en.wikipedia.org/wiki/Soundex

import sys

soundex_dict = {'B': '1', 'F': '1', 'P': '1', 'V': '1', 'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2', 'D': '3', 'T': '3', 'L': '4', 'M': '5', 'N': '5', 'R': '6', 'A': '',  'E': '',  'I': '',  'O': '', 'U': '',  'H': '',  'W': '',  'Y': ''}

def translate_to_soundex(name_string):
    """ Translate a string of text to soundex. """
    global soundex_dict
    if len(name_string) == 0:
        return 'Found Empty String: No Translation Available.'
    soundex_string = name_string[1:]
         
    for key in sorted(soundex_dict.keys()):
        soundex_string = soundex_string.replace(key, soundex_dict[key])   

    length = len(soundex_string)    
    if length < 3:
        soundex_string += '0'*(3-length)
        
    return name_string[0] + soundex_string[:3]
                
def main():
    if len(sys.argv) == 2:
        print(translate_to_soundex(sys.argv[1].upper()))
    else:
        print 'You Must Provide A String To Be Translated.'

if __name__ == "__main__":
    main()
