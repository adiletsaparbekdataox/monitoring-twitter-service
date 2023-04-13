import redis
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from django.conf import settings
from . import models, serializers, bot


def validate_token(token):
    if token is None:
        raise APIException(detail='Required field [TOKEN]', code=400)

    if token != settings.TOKEN:
        raise APIException(detail='Invalid field [TOKEN]', code=400)


class TwitterAllTweet(generics.ListCreateAPIView):
    queryset = models.Tweets.objects.all()
    serializer_class = serializers.TweetCountSerializers

    def get(self, request, **kwargs):
        token = request.headers.get('TOKEN')
        validate_token(token=token)
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class TwitterAllRetweets(APIView):
    queryset = models.Retweets.objects.all()
    serializer_class = serializers.RetweetCountSerializers

    def get(self, request, **kwargs):
        token = request.headers.get('TOKEN')
        validate_token(token=token)
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class RepliesCountView(generics.ListCreateAPIView):
    queryset = models.RepliesCount.objects.all()
    serializer_class = serializers.RepliesCountSerializers

    def get(self, request, **kwargs):
        token = request.headers.get('TOKEN')
        validate_token(token=token)
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class TweetBackView(generics.ListCreateAPIView):
    queryset = models.TweetBack.objects.all()
    serializer_class = serializers.TweetBackSerializers

    def get(self, request, **kwargs):
        token = request.headers.get('TOKEN')
        validate_token(token=token)
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class RetweetBackView(generics.ListCreateAPIView):
    queryset = models.RetweetBack.objects.all()
    serializer_class = serializers.RetweetBackSerializers

    def get(self, request, **kwargs):
        token = request.headers.get('TOKEN')
        validate_token(token=token)
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class RepliesBackView(generics.ListCreateAPIView):
    queryset = models.RepliesBack.objects.all()
    serializer_class = serializers.RetweetBackSerializers

    def get(self, request, **kwargs):
        token = request.headers.get('TOKEN')
        validate_token(token=token)
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
