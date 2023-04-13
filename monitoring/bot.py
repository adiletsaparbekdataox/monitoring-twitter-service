import time

import tweepy

from decouple import config

auth = tweepy.OAuthHandler(config("CONSUMER_KEY"), config("CONSUMER_SECRET"))
auth.set_access_token(config("ACCESS_TOKEN"), config("ACCESS_TOKEN_SECRET"))
client = tweepy.Client(bearer_token=config("BEARER_TOKEN"))


def tweets_count_user(name):
    all_likes = []
    tweet_user = []
    final_list_user = {}
    api = tweepy.API(auth, wait_on_rate_limit=True)

    for like in api.get_favorites(screen_name=name):
        all_likes.append(like)

    for likes in all_likes:
        time.sleep(1)
        try:
            for tweet_info in client.get_liking_users(
                id=likes.id,
                expansions="pinned_tweet_id",
                tweet_fields=["author_id"],
                user_fields="username"
            ):
                try:
                    for i in tweet_info:
                        tweet_user.append(getattr(i, "username"))
                except AttributeError:
                    pass
        except TypeError:
            pass
    for i in tweet_user:
        final_list_user[i] = tweet_user.count(i)
    values = final_list_user.values()
    list_values = list(values)
    return tweet_user, list_values


def tweet_back(name):
    """Function count number followed users posted likes"""
    api = tweepy.API(auth, wait_on_rate_limit=True)
    ids = []
    for page in tweepy.Cursor(api.get_follower_ids, screen_name=name).pages():
        ids.extend(page)
    user_screen = api.get_user(screen_name=name)
    favourites_count = user_screen.favourites_count
    return favourites_count


def retweets(name):
    """Function count number of project's each retweets"""
    tweets = []
    res = {}
    retweet_user = []
    api = tweepy.API(auth, wait_on_rate_limit=True)
    for tweet in api.user_timeline(screen_name=f"{name}"):
        tweets.append(tweet.text)
        for reTweet in api.get_retweets(tweet.id):
            retweet_user.append(reTweet.user.screen_name)
            for i in retweet_user:
                res[i] = retweet_user.count(i)
    values = res.values()
    list_values = list(values)

    return list_values, retweet_user


def retweet_back(name):
    """Function count number followed users project's retweet"""
    retweet_back_list = []
    api = tweepy.API(auth, wait_on_rate_limit=True)
    query = f"to:@{name} filter:retweets"
    data_reply = tweepy.Cursor(api.search_tweets,
                               q=query,
                               result_type='mixed',
                               tweet_mode='extended',
                               ).items(1000)
    for tweet in data_reply:
        retweet_back_list.append(tweet.full_text)
    return len(retweet_back_list)


def replies(name):
    """Function count project's each tweet replies"""
    replies_count = []
    res = {}
    api = tweepy.API(auth, wait_on_rate_limit=True)
    query = f"@{name}"

    data_reply = tweepy.Cursor(
        api.search_tweets,
        q=query,
        result_type='mixed',
        include_entities=True,
        count=10000,
        tweet_mode='extended',

    ).items(10000)

    for tweet in data_reply:
        replies_count.append(tweet.user.screen_name)

    for user in replies_count:
        res[user] = replies_count.count(user)

    key = res.keys()
    key_list = list(key)
    values = res.values()
    values_list = list(values)

    return key_list, values_list


def replies_back(name):
    """Function count number followed users project's replies"""
    count_replies = []
    api = tweepy.API(auth, wait_on_rate_limit=True)
    query = f"from:@{name}"

    data_reply = tweepy.Cursor(
        api.search_tweets,
        q=query,
        include_entities=True,
        tweet_mode='extended',
    ).items(1000)

    for tweet in data_reply:
        count_replies.append(tweet.full_text)

    return len(count_replies)
