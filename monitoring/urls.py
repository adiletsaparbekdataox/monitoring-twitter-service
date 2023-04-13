from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tweets/', views.TwitterAllTweet.as_view()),
    path('replies/', views.RepliesCountView.as_view()),
    path('retweets/', views.TwitterAllRetweets.as_view()),
    path('tweets/back/', views.TweetBackView.as_view()),
    path('retweets/back/', views.RetweetBackView.as_view()),
    path('replies/back/', views.RepliesBackView.as_view()),
]
