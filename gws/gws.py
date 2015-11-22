# -*- coding: utf-8 -*-

import urllib2
import json
import time

import sys

reload(sys)
sys.setdefaultencoding('utf8')

graph_url = "https://graph.facebook.com/v2.5/"

def json_message():

    json_setting = ''

    with open('../setting.json', 'r') as json_file:
        json_setting = json.load(json_file)

    return json_setting if json_setting == "" else json_setting['credential']['facebook']

def format_url(page_id = "", query = ""):
    credential = json_message()
    return "%s%s%s&access_token=%s" % (graph_url, page_id, query, credential['access_token'])

def get_object(q=""):
    pass


if '__main__' == __name__:
    pages = ['BulgeHd', 'Lickourdisplay', 'trasherbangkok', 'haruehun.airry', 'Toodsdiary', 'NeeNongNa', 'overtheeyebrow', 'cutegaystory', 'gaythaigointer', 'koorakgay', 'iamgaytherabbit', 'SingleGay.th', 'GthaiMovie', 'gaybottom']

    for page in pages:
        p_url = format_url(page_id = page, query = '?fields=feed{message,link,comments}') 
        page_request = urllib2.urlopen(p_url)
        page_content_text = page_request.read()
        page_content = json.loads(page_content_text)

        for message in page_content['feed']['data']:
            with open('message.txt', 'aw') as m:
                if 'message' in message:
                    m.write("%s\n" % message['message'])

                m.close()

        time.sleep(30)
