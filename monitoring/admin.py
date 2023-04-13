from django.contrib import admin
from . import models


class TweetsAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = ("user", "count",)


class RetweetsAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = ("user", "count")


class RepliesAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = ("user", "count",)


admin.site.register(models.Tweets, TweetsAdmin)
admin.site.register(models.Retweets, RetweetsAdmin)
admin.site.register(models.RepliesCount, RepliesAdmin)
admin.site.register(models.TweetBack)
admin.site.register(models.RetweetBack)
admin.site.register(models.RepliesBack)
admin.site.register(models.Accounts)
