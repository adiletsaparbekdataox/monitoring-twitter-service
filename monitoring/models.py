from django.db import models
from django.db.models import Sum


class Tweets(models.Model):
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets Like Count"
    """Class based on tweets like counts and specific user"""
    user = models.CharField(max_length=255)
    count = models.BigIntegerField()

    def __str__(self):
        return f"User: {self.user}, Count of likes: {self.count}"


class Retweets(models.Model):
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Retweets Count"
    """Class based on retweets like counts and specific user"""
    user = models.CharField(max_length=250)
    count = models.BigIntegerField()

    def __str__(self):
        return f"User: {self.user}, Count of retweets: {self.count}"


class RepliesCount(models.Model):
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Replies Count"
    """Class based on replies counts and specific user"""
    user = models.CharField(max_length=250)
    count = models.BigIntegerField()

    def __str__(self):
        return f"User: {self.user}, Count of replies: {self.count}"


class TweetBack(models.Model):
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Your Tweets Like Count"
    """Class based on project tweet counts"""
    count = models.BigIntegerField()

    def __str__(self):
        return f'Total count of tweets like: {self.count}'


class RetweetBack(models.Model):
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Your Retweets Count"
    """Class based on project retweets counts"""
    count = models.BigIntegerField()

    def __str__(self):
        return f'Total count of retweets: {self.count}'


class RepliesBack(models.Model):
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Your Replies Count"
    """Class based on project replies counts"""
    count = models.BigIntegerField()

    def __str__(self):
        return f'Total count of replies: {self.count}'


class Accounts(models.Model):
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Accounts Monitoring"
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username
