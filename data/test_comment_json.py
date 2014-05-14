import json as js
import urllib2
import time 


def main():

    #link = "http://www.reddit.com/r/SuicideWatch/comments/25flxo/oh_well_i_dunno_what_now/.json"
    #link = "http://www.reddit.com/r/SuicideWatch/comments/25fmf6/finally_going_to_do_it_i_actually_feel_at_peace/.json"
    link = "http://www.reddit.com/r/SuicideWatch/comments/25fdij/this_is_it_i_am_done_with_life/.json"
    #link = "http://www.reddit.com/r/SuicideWatch/.json"
    hdr = { 'User-Agent' : 'super happy flair bot by /u/spladug' }
    req = urllib2.Request(link, headers=hdr)
    json_te = urllib2.urlopen(req).read()
    
    decoded = js.loads(json_te)

    print len(decoded)

    # Author post and information
   
    for author in decoded[0]['data']['children']:        
        print author['data']['author']
        print author['data']['selftext']
        print time.ctime(int(author['data']['created_utc']))




if __name__ == '__main__':
    main()