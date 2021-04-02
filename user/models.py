from django.db import models


class User(models.Model):
    username     = models.CharField(max_length=20)
    email        = models.EmailField(max_length=45, unique=True)
    password     = models.CharField(max_length=300, null=True)
    kakao_id     = models.CharField(max_length=20)
    is_creator   = models.BooleanField(default=False)
    voting_power = models.IntegerField(default=20)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'


class Creator(models.Model):
    nickname          = models.CharField(max_length=20, unique=True)
    phonenumber       = models.CharField(max_length=13, unique=True)
    introduction      = models.CharField(max_length=200)
    profile_image_url = models.CharField(max_length=2000)
    image_url         = models.CharField(max_length=2000, null=True)
    user              = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'creators'