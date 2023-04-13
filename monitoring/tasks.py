import time

from django.db.models import F

from server.celery import app
from . import bot, models


def filter_username():
    user_account = models.Accounts.objects.all().first()
    user_account = str(user_account)
    if user_account[0] == "@":
        return user_account[1:]
    elif "https://twitter.com/" in user_account:
        return user_account[20:]
    else:
        return user_account


#  run celery -A data_ox_twitter worker --beat --scheduler django --loglevel=info
# redis-server --port 6360
@app.task()
def monitoring_tweet_like():
    models.Tweets.objects.all().delete()
    user_account = filter_username()
    tweet_user_list = bot.tweets_count_user(name=user_account)
    for count_number, user in zip(tweet_user_list[1], tweet_user_list[0]):
        if models.Tweets.objects.filter(user=user).exists():
            object_user = models.Tweets.objects.get(user=user)
            object_user.count = F("count") + count_number
            object_user.save()
        else:
            models.Tweets.objects.create(user=user, count=count_number)
    time.sleep(30)


@app.task()
def monitoring_retweets():
    """ Schedule Function for monitoring retweets """
    models.Retweets.objects.all().delete()
    user_account = filter_username()

    retweets = bot.retweets(name=user_account)
    for count_number, user in zip(retweets[0], retweets[1]):
        if models.Retweets.objects.filter(user=user).exists():
            object_user = models.Retweets.objects.get(user=user)
            object_user.count = F("count") + count_number
            object_user.save()

        else:
            models.Retweets.objects.create(user=user, count=count_number)


@app.task()
def monitoring_replies():
    """ Schedule Function for monitoring replies """
    models.RepliesCount.objects.all().delete()
    user_account = filter_username()
    print(user_account)
    replies = bot.replies(name=user_account)
    print(replies[0])
    print(replies[1])
    for count_number, user in zip(replies[1], replies[0]):
        # for count_number in replies[1]:
        #     for user in replies[0]:
        if models.RepliesCount.objects.filter(user=user).exists():
            object_user = models.RepliesCount.objects.get(user=user)
            object_user.count = F("count") + count_number
            object_user.save()
        else:
            models.RepliesCount.objects.create(user=user, count=count_number)
        # models.RepliesCount.objects.create(user=user, count=count_number)


@app.task()
def monitoring_tweetback():
    """ Schedule Function for monitoring tweetback from project """
    models.TweetBack.objects.all().delete()
    user_account = filter_username()

    counts = bot.tweet_back(name=user_account)

    models.TweetBack.objects.create(count=counts)
    time.sleep(30)


@app.task()
def monitoring_retweetback():
    """ Schedule Function for monitoring retweetback from project """
    models.RetweetBack.objects.all().delete()
    user_account = filter_username()

    counts = bot.retweet_back(name=user_account)
    models.RetweetBack.objects.create(count=counts)


@app.task()
def monitoring_repliesback():
    """ Schedule Function for monitoring replies from project """
    models.RepliesBack.objects.all().delete()
    user_account = filter_username()

    counts = bot.replies_back(name=user_account)
    models.RepliesBack.objects.create(count=counts)


@app.task()
def caller():
    monitoring_tweet_like.delay()
    time.sleep(30)
    monitoring_tweetback.delay()
    time.sleep(30)
    monitoring_retweets.delay()
    time.sleep(30)
    monitoring_retweetback.delay()
    time.sleep(30)
    monitoring_replies.delay()
    time.sleep(30)
    monitoring_repliesback.delay()
