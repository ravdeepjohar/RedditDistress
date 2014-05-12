import webbrowser
import urlparse
import urllib2
import json
import sys
import time


BASE = 'http://www.reddit.com'
DEFAULT_REDDIT = 'http://www.reddit.com/r/SuicideWatch'
REDDIT = DEFAULT_REDDIT
COMMENTS = 'permalink'
URL = 'url'
WHAT_TO_GET = ''
page_cnt = 0 


def add_json(reddit):
    reddit = reddit.replace('/?', '/.json?')
    if '/.json' not in reddit:
        reddit = reddit + '/.json'
    return reddit


def get_json_text(reddit):
    page = reddit
    hdr = { 'User-Agent' : 'super happy flair bot by /u/spladug' }
    req = urllib2.Request(page, headers=hdr)
    json_text = urllib2.urlopen(req).read()
    #sock = urllib2.urlopen(page)
    #json_text = sock(req).read()
    return json_text

def find_all_pages(reddit):
    global page_cnt

    while True:
        json_url = add_json(reddit)
        json_text = get_json_text(json_url)
        decoded = json.loads(json_text)
        #print decoded
        #print "---"
        
        posts = decoded['data']['children']
        if len(posts) == 0:
            break
        print >>sys.stderr, "# page {cnt:03}: {reddit}".format(cnt=page_cnt, reddit=reddit)
        
        last_post = posts[-1]
        name = last_post['data']['name']
        print name
        reddit = "{R}/?count=25&after={name}".format(R=REDDIT, name=name)
        print reddit
        page_cnt += 1

        #time.sleep(60)
        
    


def main():

    find_all_pages(REDDIT)


if __name__ == '__main__':
    main()