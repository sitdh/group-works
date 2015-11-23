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

if '__main__' == __name__:
    pages = ['BulgeHd', 'Lickourdisplay', 'trasherbangkok', 'haruehun.airry', 'Toodsdiary', 'NeeNongNa', 'overtheeyebrow', 'cutegaystory', 'gaythaigointer', 'koorakgay', 'iamgaytherabbit', 'SingleGay.th', 'GthaiMovie', 'gaybottom']

    for page in pages:
        print "Page @%s" % page

        p_url = format_url(page_id = page, query = '?fields=feed{comments{message,comment_count,comments{message}}}') 

        first_page = True

        for i in [1..10]:

            page_request = urllib2.urlopen(p_url)
            page_content_text = page_request.read()
            page_content = json.loads(page_content_text)

            for message in page_content['feed']['data']:

                if 'comments' in message:

                    with open('%s-comments.txt' % page, 'aw') as message_content:
                        for msg in message['comments']['data']:
                            message_content.write("%s\n" % msg['message'])

                            if msg['comment_count'] > 0:

                                for reply_comment in msg['comments']['data']:
                                    message_content.write("%s\n" % reply_comment['message'])

                        message_content.close()

                p_url = page_content['paging']['next']

                time.sleep(30)

        time.sleep(30)
         
