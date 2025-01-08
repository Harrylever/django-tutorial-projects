"""Blog Models"""

from django.conf import settings
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    """Custom Manager for Published Posts"""

    def get_queryset(self):
        """Set query"""
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Post Models"""

    class Status(models.TextChoices):
        """Status Field"""

        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        """Meta Fields"""

        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self):
        return str(self.title)
