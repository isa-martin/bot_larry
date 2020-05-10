import tweepy
import time

def inicialize_Bot():
    auth = tweepy.OAuthHandler('lEfg29ZX4w0j6cbuZT8EDsCo9', 'AZROz3tfQ43fnod0QNlsJsaZiakhBbETV05zDL5ZVDuQSreSzP')
    auth.set_access_token('1258952388385419265-xUvOLNbN8eDyLVE06e00nU70Kh7Xh9','NvGMWAPy4zw570aKZTDIDqmbEHxW6QSc3GkXHzL04GLsZ')
    return auth

def search_For(search, n_Tweets, api):
    for tweet in tweepy.Cursor(api.search, search, result_type='recent').items(n_Tweets):
        try:
            interact_With_Tweet(tweet)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def interact_With_Tweet(tweet):
    print('Tweet Id Catched')
    tweet_id = tweet.id
    print(tweet.id)
    print('Tweet Liked')
    tweet.favorite()
    print('Tweet Replied')
    api.update_status('@' + tweet.user.screen_name + ' Larry is real!', in_reply_to_status_id=tweet_id)
    print(tweet.__dict__.keys())
    time.sleep(10) #87 seconds

auth = inicialize_Bot()
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = '@larryisreal_bot'
n_Tweets = 1
search_For(search, n_Tweets, api)
