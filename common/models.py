from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    adress=models.CharField(max_length=128)
    phone=models.CharField(max_length=64)
    email=models.EmailField(max_length=128)


class ConactRequest(models.Moldel):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    sucject=models.CharField(max_length=256)
    messgae=models.TextField()


class About(models.Model):
    avator=models.ImageField(upload_to='about/')

    name=models.CharField(max_length=128)
    short_description=models.CharField(max_length=256)
    
    article_title=models.CharField(max_length=256)
    article_content=models.TextField()

    twitter_url=models.CharField(max_length=256)
    facebook_url=models.CharField(max_length=256)
    linkedin_url=models.CharField(max_length=256)
    instagram_url=models.CharField(max_length=256)
