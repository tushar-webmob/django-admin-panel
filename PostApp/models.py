from django.db import models
from Account.models import Register

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='postimages/%Y/%m/%d/', default='images/default.png')
    author = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    favourties = models.ManyToManyField(Register,related_name='favourties',default=None,blank=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(Register,related_name="person", on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='commentimages/%Y/%m/%d/', default='images/default.png')
    name = models.CharField(max_length=342)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name