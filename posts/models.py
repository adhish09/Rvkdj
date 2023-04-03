from django.db import models
from django.contrib.auth import get_user_model


User  = get_user_model()


class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class PostStatus(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class PostAction(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE,null=True, blank=True)
    post_image = models.ImageField(upload_to="posts", blank=True)
    status = models.ForeignKey(PostStatus, on_delete=models.CASCADE)
    action = models.ForeignKey(PostAction, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("-created_at",)
