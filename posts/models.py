from django.db import models

# Create your models here.


class Author(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
