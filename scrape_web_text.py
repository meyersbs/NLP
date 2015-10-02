#!usr/bin/python
# @AUTHOR: Benjamin S. Meyers
# @DESCRIPTION: A simple function to copy an entire HTML file from a URL and then pull out all of the content text.

import requests, re, sys, nltk, random, numpy
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
