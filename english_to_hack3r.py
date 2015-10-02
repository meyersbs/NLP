# @AUTHOR: Benjamin Meyers
# @DESCRIPTION: Try to write code to convert text into hAck3r, using regular
#               expressions and substitution, where e → 3, i → 1, o → 0,
#               l → |, s → 5, . → 5w33t!, ate → 8. Normalize the text to
#               lowercase before converting it. Add more substitutions of your
#               own. Now try to map s to two different values: $ for
#               word-initial s, and 5 for word-internal s.

import re, sys

def file_to_hacker(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            temp_line = line.lower().strip('.,:;!?')
            temp_line = re.sub(r'\ss', ' $', temp_line)
            temp_line = re.sub(r'ate', '8', temp_line)
            temp_line = re.sub(r'for', '4', temp_line)
            temp_line = re.sub(r'too', '2', temp_line)
            temp_line = re.sub(r'to', '2', temp_line)
            temp_line = re.sub(r'e', '3', temp_line)
            temp_line = re.sub(r'i', '1', temp_line)
            temp_line = re.sub(r'o', '0', temp_line)
            temp_line = re.sub(r'l', '|', temp_line)
            temp_line = re.sub(r's', '5', temp_line)
            temp_line = re.sub(r'\.', '5w33t!', temp_line)
            print(temp_line)
    
    
def text_to_hacker(input_text):
    for line in input_text.split('\n'):
        temp_line = line.lower().strip('.,:;!?')
        temp_line = re.sub(r'\ss', ' $', temp_line)
        temp_line = re.sub(r'ate', '8', temp_line)
        temp_line = re.sub(r'for', '4', temp_line)
        temp_line = re.sub(r'too', '2', temp_line)
        temp_line = re.sub(r'to', '2', temp_line)
        temp_line = re.sub(r'e', '3', temp_line)
        temp_line = re.sub(r'i', '1', temp_line)
        temp_line = re.sub(r'o', '0', temp_line)
        temp_line = re.sub(r'l', '|', temp_line)
        temp_line = re.sub(r's', '5', temp_line)
        temp_line = re.sub(r'\.', '5w33t!', temp_line)
        print(temp_line)


def main():
    if sys.argv[1] == '-f':
        file_to_hacker(sys.argv[2])
    elif sys.argv[1] == '-t':
        text_to_hacker(sys.argv[2])
    else:
        sys.exit("Invalid command.")
        
if __name__ == "__main__":
    main()
