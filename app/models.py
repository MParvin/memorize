from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    meaning = models.TextField()
    news = models.TextField()
    examples = models.TextField()
    thumbnail = models.ImageField(upload_to='static/images/', blank=True)
    thumbnail_alt = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_image(self):
        return self.thumbnail.url

    # get 10 random posts
    @staticmethod
    def get_random_posts():
        return Post.objects.order_by('?')[:10]
        