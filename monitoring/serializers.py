from rest_framework import serializers
from .models import Tweets, Retweets, RepliesCount, TweetBack, RetweetBack, RepliesBack


class TweetCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = '__all__'


class RetweetCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Retweets
        fields = '__all__'


class RepliesCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = RepliesCount
        fields = "__all__"


class TweetBackSerializers(serializers.ModelSerializer):
    class Meta:
        model = TweetBack
        fields = "__all__"


class RetweetBackSerializers(serializers.ModelSerializer):
    class Meta:
        model = RetweetBack
        fields = "__all__"


class RepliesBackSerializers(serializers.ModelSerializer):
    class Meta:
        model = RepliesBack
        fields = "__all__"
