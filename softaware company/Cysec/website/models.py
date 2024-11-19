from django.db import models



class Account(models.Model):
    admin_name=models.CharField(max_length=100)
    admin_number=models.CharField(max_length=50)
    admin_email=models.EmailField()
    admin_password=models.CharField(max_length=100)

class Feature(models.Model):
    feature_image=models.ImageField(upload_to='static/',default='null')
    feature_title=models.CharField(max_length=100,default='null')
    feature_details=models.TextField(default='null')