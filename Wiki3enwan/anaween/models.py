from django.db import models

class enwaan(models.Model):
    الأسم_والمنطقة = models.CharField(max_length=100)
    العنوان = models.CharField(max_length=255)
    الرقم = models.CharField(max_length=25, null=True, blank=True)
    مقاطعة = models.BooleanField(default=False)
    text = models.CharField(default='لا', max_length=255)
    الوصف = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True,default='default')
    