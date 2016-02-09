import sys
import json

def find_happiest_state(sent_file, tweet_file):
        scores = {} # initialize an empty dictionary
        for line in sent_file:
                term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
                scores[term] = int(score)  # Convert the score to an integer.

        # constant dictionary for US states
        us_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }
        
        # Summarize the score for different state
        score_dict = {}
        tweets = []
        for line in tweet_file:
                tweets.append(json.loads(line))
                
        # read json object as dictionary
        for tweet in tweets: 
                #for key, val in tweet.iteritems():
                item_score = 0
                if "text" in tweet:
                        val = tweet["text"]                   
                        words = val.split()
                        for word in words:
                                if scores.has_key(word):
                                        item_score += scores[word]
                        if "user" in tweet and "location" in tweet["user"]:
                                if(tweet["user"]["location"] != ""):
                                        states = tweet["user"]["location"].split(',')
                                        for state in states:
                                                if state in us_states:
                                                        if state not in score_dict:
                                                                score_dict[state] = item_score
                                                        else:
                                                                score_dict[state] += item_score

        print max(score_dict, key=lambda x: score_dict[x])  


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    find_happiest_state(sent_file, tweet_file)


if __name__ == '__main__':
    main()



        