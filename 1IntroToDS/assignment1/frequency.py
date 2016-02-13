import sys
import json

# Compute the terms' frequency
def find_frequency(tweet_file):
	# read json file and serialize
	word_dict = {}
	tweets = []
	for line in tweet_file:
		tweets.append(json.loads(line))
		
	# read json object as dictionary
	for tweet in tweets: 
		for key, val in tweet.iteritems():
			if key == 'text':			
				words = val.split()
				for word in words:
					if word not in word_dict:
						word_dict[word] = 1
					else:
						word_dict[word] += 1


	for key, val in word_dict.iteritems():
		print "%s %.4f" % (key, val)


def main():
    tweet_file = open(sys.argv[1])
    find_frequency(tweet_file)


if __name__ == '__main__':
    main()
