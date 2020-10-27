from django.db import models

# Create your models here.

class Pi(models.Model):
    title=models.CharField('제목', max_length=200)
    desc=models.TextField('본문', blank=True)
    pic=models.ImageField('사진', blank=True, null=True) 
    created_at=models.DateTimeField('생성날짜', auto_now_add=True)
    modified_at=models.DateTimeField('수정날짜',auto_now=True)

    def __str__(self):
        return self.title