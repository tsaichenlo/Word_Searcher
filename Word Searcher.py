# Author: Phoebe Lo
# Email: tsaichenlo@umass.edu
# Spire ID: 33642075

import urllib.request
import string
import sys 
import re

def read_article_file(url):
    req = urllib.request.urlopen(url)
    text = req.read()
    text = text.decode('UTF-8')
    return text

def text_to_article_list(text):
    article_list = []
    tmp = re.split('<NEW ARTICLE>', str(text))
    for i in tmp:
        article_list.append(i)
    new_list = list(filter(lambda x: x != '', article_list))
    return new_list


def split_words(text):
    word_list = []
    line_list = text.splitlines()
    for i in line_list:
        word_list += i.split()
    return word_list


def scrub_word(text):
    t1 = text.strip(string.punctuation)
    t2 = t1.strip(' ')
    return t2


def scrub_words(text):
    lis = []
    for strin in text:
        words = strin.split()
        for i in words:
            x = i.lower()
            j = x.strip(string.punctuation)
            lis.append(j)
    new_lis = list(filter(lambda x: x != '', lis))
    print(new_lis)
    return new_lis