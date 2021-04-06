from datetime import datetime, timedelta

from django.db import models

from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'categories'
        

class SubCategory(models.Model):
    name     = models.CharField(max_length=20)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'subcategories'


class Difficulty(models.Model):
    level = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'difficulties'


class Hashtag(models.Model):
    tag = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'hashtags'


class Lecture(models.Model):
    title         = models.CharField(max_length=50, null=True)
    price         = models.DecimalField(max_digits=12, decimal_places=2)
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    description   = models.TextField(default='HTML')
    down_payment  = models.DecimalField(max_digits=2, decimal_places=0, default=5)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    user          = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category      = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    sub_category  = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)
    difficulty    = models.ForeignKey('Difficulty', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table        = 'lectures'
        unique_together = ('user', 'title')

        
class PendingLecture(models.Model):
    title             = models.CharField(max_length=45)
    cover_image_url   = models.CharField(max_length=2000, null=True)
    summary_image_url = models.CharField(max_length=2000, null=True)
    detailed_category = models.CharField(max_length=20, null=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    user              = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category          = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    sub_category      = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)
    difficulty        = models.ForeignKey('Difficulty', on_delete=models.SET_NULL, null=True)
    hashtags          = models.ManyToManyField('Hashtag', through='PendingLectureHashtag')
    
    class Meta:
        db_table        = 'pending_lectures'
        unique_together = ('user', 'title')

class PendingLectureHashtag(models.Model):
    pending_lecture = models.ForeignKey('PendingLecture', on_delete=models.SET_NULL, null=True)
    hashtag         = models.ForeignKey('Hashtag', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'pending_lectures_hashtags'
        unique_together = ('pending_lecture', 'hashtag')

class Introduction(models.Model):
    detail          = models.CharField(max_length=250, null=True)
    image_url       = models.CharField(max_length=250)

    pending_lecture = models.ForeignKey('PendingLecture', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table        = 'introductions'
        # unique_together = ('detail', 'image_url')


class Vote(models.Model):
    user            = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pending_lecture = models.ForeignKey('PendingLecture', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'votes'