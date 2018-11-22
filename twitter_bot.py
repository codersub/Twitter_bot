import tweepy
import time
print('Hey I am a Twitter Bot',flush=True)
CONSUMER_KEY='YbfVlXNCvXWk1Huk51K9cPRZ6'
CONSUMER_SECRET='W4ER6VI44L7VymlOfIN2sp9qB78CxKr3Tem7euzLiiNixDA5la'
ACCESS_KEY='1061228670725980160-dspvE8bWt4OnKBOS607O1vMFwythMq'
ACCESS_SECRET='sgP9YjnOajZj1SpGedkF3HdnKsl2HY3baifZxKdaDomrA'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
FILE_NAME = 'last_seen_id.text'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #hello!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#Hello back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(35)		
		
		