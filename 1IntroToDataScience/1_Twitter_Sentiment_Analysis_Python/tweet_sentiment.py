import sys
import json

def find_sentiment(sent_file, tweet_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	
	# print scores.items() # Print every (term, score) pair in the dictionary

	# read json file and serialize
	tweets = []
	for line in tweet_file:
		tweets.append(json.loads(line))
		
	# read json object as dictionary
	for tweet in tweets: 
		for key, val in tweet.iteritems():
			item_score = 0
			if key == 'text':			
				words = val.split()
				for word in words:
					if scores.has_key(word):
						item_score += scores[word]
				print item_score	


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    find_sentiment(sent_file, tweet_file)
   # lines(sent_file)
   # lines(tweet_file)

if __name__ == '__main__':
    main()
