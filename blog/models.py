import uuid

from django.db import models

from accounts.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class PostBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=1)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=1)


class Post(PostBase):
    title = models.CharField(max_length=150)
    status = models.IntegerField(choices=STATUS, default=0)
    published = PublishedManager()

class Comment(PostBase):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
