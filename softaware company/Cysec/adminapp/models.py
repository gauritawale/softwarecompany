from django.db import models

# Create your models here.
class Account(models.Model):
    admin_name=models.CharField(max_length=100)
    admin_number=models.CharField(max_length=50)
    admin_email=models.EmailField()
    admin_password=models.CharField(max_length=100)


class Slider(models.Model):
    slider_subtitle=models.CharField(max_length=100)
    slider_title=models.CharField(max_length=100)
    slider_image=models.ImageField(upload_to="static/")
    slider_video_link=models.TextField()
    slider_button1=models.CharField(max_length=100)
    slider_button1_link=models.TextField()
    slider_button2=models.CharField(max_length=100)
    slider_button2_link=models.TextField()
    slider_details = models.TextField(default='null')
