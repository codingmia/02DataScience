import sys
import json

def find_term(sent_file, tweet_file):
	scores = {} # initialize an empty dictionary
	new_score = {}
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
				for word in words:
					if word not in scores and word not in new_score:
						new_score[word] = item_score	

	for key, val in new_score.iteritems():
		print key,val



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    find_term(sent_file, tweet_file)
   

if __name__ == '__main__':
    main()
