from django.db import models

# Create your models here.
class Post(models.Model):
    #image
    title = models.CharField(max_length=200)
    content = models.TextField()
    # image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    # tag = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
