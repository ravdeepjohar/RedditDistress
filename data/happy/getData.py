import webbrowser, urlparse, urllib2
import json
import sys, time, os
import pickle


BASE = 'http://www.reddit.com'
DEFAULT_REDDIT = 'http://www.reddit.com/r/happy'
REDDIT = DEFAULT_REDDIT
COMMENTS = 'permalink'
URL = 'url'
WHAT_TO_GET = ''
page_cnt = 0 

dict_link = dict()

def init():

    links = open('post_links.txt','rb')
    for link in links:
        link = link.rstrip()
        dict_link[link] = 1

    links.close()


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

def process_post(index, post):
    # indexing starts with 1 (instead of 0):
    index += 1
    url = urlparse.urljoin(BASE, post['data']['permalink'])

    try: 

        permalink = post['data']['permalink']
        print permalink
        
        if url not in dict_link:
            
            dict_link[url] = 1 
            jsonurl = add_json(url)
            jsonpost = get_json_text(jsonurl)

            filename = "jsons/"+ os.path.basename(os.path.normpath(permalink)) + ".json"

            with open(filename, "w") as text_file:
                text_file.write(jsonpost)
    except: 
        pass


def process_posts(decoded):
    posts = decoded['data']['children']
    for i, post in enumerate(posts):
        process_post(i, post)

def find_all_pages(reddit):
    global page_cnt

    while True:
        json_url = add_json(reddit)
        json_text = get_json_text(json_url)
        decoded = json.loads(json_text)
      
        posts = decoded['data']['children']
        if len(posts) == 0:
            break
        #print >>sys.stderr, "# page {cnt:03}: {reddit}".format(cnt=page_cnt, reddit=reddit)
        
        last_post = posts[-1]
        name = last_post['data']['name']
        reddit = "{R}/?count=25&after={name}".format(R=REDDIT, name=name)
        jsonlink = "{R}/.json?count=25&after={name}".format(R=REDDIT, name=name)
        jsontext =  get_json_text(jsonlink)
        decoded = json.loads(jsontext)
        process_posts(decoded)
        page_cnt += 1
        

        # if page_cnt == 4:
        #     break 
        
        
    
def close():

    links = open('post_links.txt','wb')
    for key in dict_link:
        links.write(key + "\n")
    links.close()

def main():

    init()
    find_all_pages(REDDIT)
    close()


if __name__ == '__main__':
    main()