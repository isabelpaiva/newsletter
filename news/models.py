from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewers = models.ManyToManyField('accounts.Account', related_name = 'news', through="news.NewsReview")

class NewsReview(models.Model):
    reviewer = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    news = models.ForeignKey('news.News', on_delete=models.CASCADE)
    feedback = models.TextField()
