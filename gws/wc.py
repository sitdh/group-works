# -*- coding: utf-8 -*-

import json
import collections

import os.path
import glob

import codecs

import sys

def open_json(file_name):

    json_content = None

    if os.path.isfile(file_name):

        with open(file_name, 'r') as json_handler:
            json_content = json.load(json_handler)
            json_handler.close()

    return json_content

def word_list():
    word_content = []
    words = codecs.open('word-list.csv', encoding='utf-8')
    word_content = words.read()
    words.close()
    word_content = word_content.split("\r\n")

    return [word.strip() for word in word_content]

def open_json(file_location):
    file_content = open(file_location, 'r')
    message_content = json.load(file_content)
    file_content.close()

    return message_content

def get_datasource():
    return glob.glob("../datasource/*/*.txt")

if '__main__' == __name__:

    words = word_list()
    file_content = open_json('../datasource.json')
    
    for key, comment_content_location in file_content.iteritems():

        comment_location_handler = codecs.open("../%s" % comment_content_location, encoding='utf-8')
        comment_message = comment_location_handler.read()
        comment_location_handler.close()

        word_count = codecs.open('results/%s-count.csv' % key, encoding='utf-8', mode='w+')
        word_collection = dict()
        for word in words:
            word_found = comment_message.count("%s" % word)
            word_collection.update({word:word_found})

        cnt = collections.Counter(word_collection).most_common()
        for (word_index,word_found) in cnt:
            word_count.write("%s,%i\n" % (word_index, word_found))

        word_count.close()
