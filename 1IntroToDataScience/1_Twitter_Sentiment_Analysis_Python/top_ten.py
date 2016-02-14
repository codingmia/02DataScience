import sys
import json

def find_top_ten( tweet_file):
        # Generate a list of all tweets
        tweets = []
        for line in tweet_file:
                tweets.append(json.loads(line))
        hashtag_dict = {}     
        # read json object as dictionary
        for tweet in tweets: 
                if "entities" in tweet and "hashtags" in tweet["entities"]:
                    hashtags = tweet["entities"]["hashtags"]  # a list of hashtags
                    for hashtag in hashtags:
                        if "text" in hashtag and hashtag["text"] != "":
                            tag = hashtag["text"]
                            if tag not in hashtag_dict:
                                hashtag_dict[tag] = 1
                            else:
                                hashtag_dict[tag] += 1


        for key, val in sorted(hashtag_dict.iteritems(), key=lambda x:-x[1])[:10]:
            print key, val
                        


def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    find_top_ten(tweet_file)

if __name__ == '__main__':
    main()



        