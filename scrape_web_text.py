#!usr/bin/python
# @AUTHOR: Benjamin S. Meyers
# @DESCRIPTION: A simple function to copy an entire HTML file from a URL and then pull out all of the content text.

__copyright__= """
The MIT License (MIT)

Copyright (c) Benjamin S. Meyers <bsm9339@rit.edu>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests, re, sys
from bs4 import BeautifulSoup
from nltk.probability import FreqDist

def get_text_from_url(url):
    """ Grab the html from a webpage and collect all of the text into a string. """
    soup = BeautifulSoup(requests.get(url).text)
    clean_text = []
    for line in soup.stripped_strings:
        if (not re.search(r'.org', line) and not re.search(r'.com', line)
            and not re.search(r"\s'", line) and not re.search(r'[\{\}@=/\[\]]', line)):
            clean_line = re.sub(r'[.,!?:;\"\(\)#\\“”‘’©·\t]', "", line)
            clean_line = re.sub(r"[-—|]", " ", clean_line)
            if clean_line != '':
                clean_text.append(clean_line.strip('\n').lower())

    plain_text = ' '.join(clean_text)
    plain_text = re.sub('\n', '', plain_text)
    plain_text = re.sub(r'  ', ' ', plain_text)
    
    return plain_text
    
def main():
    url = sys.argv[1]
    text = get_text_from_url(url)
    print(text)
    
if __name__ == "__main__":
    main()
