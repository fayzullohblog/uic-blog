from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=128)


class Tag(models.Model):
    name=models.CharField(max_length=128)

class Post(models.Model):
    image=models.ImageField(upload_to='post/')
    
    title=models.CharField(max_length=256)
    description=models.CharField(max_length=256)
    content=models.TextField()

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag)

    published_date=models.DateTimeField(auto_now_add=True)

    comment_count=models.IntegerField(default=0)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    name=models.CharField(max_length=128)
    email=models.EmailField()
    website=models.CharField(max_length=128,blank=True)
    description=models.CharField(max_length=256)

    



