import pandas as pd

# set of bad words to calculate degree of profanity
bad_words = set()

# function to read bad words from given file
def read_bad_words_from_file(file_path):
    words = set()
    try:
        with open(file_path, 'r') as f:
            for line in f:
                word = line.strip('\n')
                words.add(word)
    except Exception as exp:
        print(f'Error while reading bad words from file : {exp}')
        exit()
    return words

# calculate profanity of sentence using bad words
def calculate_profanity(sentence: str):
    global bad_words
    bad_words_count = 0
    all_words = sentence.split(' ')
    for word in all_words:
        if word in bad_words:
            bad_words_count += 1
    profanity_score = bad_words_count / len(all_words)
    return profanity_score

# read tweets from file
def read_tweets_from_file(tweets_file_path):
    tweets_list = []
    try:
        with open(tweets_file_path, 'r') as tweet_file:
            for tweet in tweet_file:
                tweet = tweet.strip('\n').strip(' ')
                if tweet:
                    tweets_list.append(tweet)
    except Exception as exp:
        print(f'Error while reading tweets file : {str(exp)}')
        exit()
    return tweets_list
    

# this function generate csv output with ouput having tweet and degree_of_profanity for each tweet per line
def generate_output(tweets_file_path = './tweets.txt', bad_words_file_path = './bad_words.txt', output_file_path = './tweets_degree_of_profanity'):
    global bad_words
    bad_words = read_bad_words_from_file(bad_words_file_path)
    tweets = read_tweets_from_file(tweets_file_path)
    processed_tweets = []
    for tweet in tweets:
        processed_tweets.append({
            'tweet': tweet,
            'degree_of_profanity': calculate_profanity(tweet)
        })
    
    df = pd.DataFrame(processed_tweets)
    print(df.head(10))

    df.to_csv(output_file_path + '.csv', index=False)


generate_output()

