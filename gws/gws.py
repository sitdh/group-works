# -*- coding: utf-8 -*-

import urllib2
import json
import time

import os.path

import sys

reload(sys)
sys.setdefaultencoding('utf8')

graph_url = "https://graph.facebook.com/v2.5/"

def open_json(file_name):

    json_content = None

    if os.path.isfile(file_name):

        with open(file_name, 'r') as json_handler:
            json_content = json.load(json_handler)
            json_handler.close()

    return json_content

def json_message():

    json_setting = open_json('../setting.json')

    return json_setting if json_setting == None else json_setting['credential']['facebook']

def format_url(page_id = "", query = ""):
    credential = json_message()
    return "%s%s%s&access_token=%s" % (graph_url, page_id, query, credential['access_token'])

def get_page_content(page_url, is_first_page=True, key="feed"):
    page_request = urllib2.urlopen(page_url)
    page_content_text = page_request.read()
    page_content = json.loads(page_content_text)

    return page_content['feed'] if is_first_page else page_content


def get_comments(comments, datastore):

    for comment in comments:
        if 'message' in comment:
            datastore.write("%s\n" % comment['message'])

            if 'comment_count' in comment and comment['comment_count'] > 0 and 'comment' in comment:
                get_comments(comment['comments']['data'], datastore)



if '__main__' == __name__:

    pages = open_json('../interested-page.json')

    """
    for page in pages['z']:

        print "Page @%s" % page
        first_page = True
        page_url = format_url(page_id=page,query='?fields=feed{comments{message,comment_count,comments{message}}}') 

        for i in range(10):

            print "\tStart at page number %i" % (i+1)

            page_content = get_page_content(page_url, first_page)

            for message in page_content['data']:

                if 'comments' in message:

                    with open('%s-comments.txt' % page, 'aw') as message_content:
                        get_comments(message['comments']['data'], message_content)
                        message_content.close()

            time.sleep(30)

            if 'paging' in page_content:
                page_url = page_content['paging']['next']
            else:
                break

            first_page = False


        time.sleep(30)
    """

    for page in pages['z']:

        print "Gathering @%s" % page
        first_page = True

        page_url = format_url(page_id=page, query="?fields=posts{message}")

        for i in range(30):
            print "  Start at page No. #%i" % (i+1)

            page_request = urllib2.urlopen(page_url)
            page_content_text = page_request.read()
            page_content = json.loads(page_content_text)
            page_content = page_content['posts'] if first_page else page_content

            with open("%s-comments.txt" % page, 'aw') as message_handler:
                for message in page_content['data']:
                    if 'message' in message:
                        message_handler.write("%s\n" % message['message'])

                message_handler.close()

            time.sleep(30)

            if 'paging' in page_content:
                page_url = page_content['paging']['next']
            else:
                break

            first_page = False
        time.sleep(30)
