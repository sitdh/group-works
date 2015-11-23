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

def get_page_content(page_url, is_first_page=True):
    page_request = urllib2.urlopen(age_url)
    page_content_text = page_request.read()
    page_content = json.loads(page_content_text)

    return page_content['feed']['data'] if is_first_page else page['data']


def get_comemnts(comments, datastore):

    for comment in comments:
        datastore.write("%s\n" % comment)

        if comment['comment_count'] > 0:
            get_comments(comment['comments']['data'], datastore)



if '__main__' == __name__:

    pages = ['BulgeHd', 'Lickourdisplay', 'trasherbangkok', 'haruehun.airry', 'Toodsdiary', 'NeeNongNa', 'overtheeyebrow', 'cutegaystory', 'gaythaigointer', 'koorakgay', 'iamgaytherabbit', 'SingleGay.th', 'GthaiMovie', 'gaybottom']

    for page in pages:
        print "Page @%s" % page

        first_page = True

        page_url = format_url(page_id = page, query = '?fields=feed{comments{message,comment_count,comments{message}}}') 

        for i in range(10):

            page_content = get_page_content(page_url, first_page)

            first_page = False

            for message in page_content:

                if 'comments' in message:

                    with open('%s-comments.txt' % page, 'aw') as message_content:
                        get_comment(message['comments']['data'], message_content)
                        message_content.close()

            page_url = page_content['paging']['next']
            time.sleep(30)

        time.sleep(30)
         
