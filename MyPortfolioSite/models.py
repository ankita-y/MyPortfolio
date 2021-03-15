from django.db import models

# Create your models here.
class Portfolio(models.Model):
    pid = models.AutoField
    thoughts = models.TextField(null=True, blank=True)
    skills = models.CharField(max_length=50,null=True, blank=True)
    skillper = models.IntegerField(default="", null=True, blank=True)
    # projects = models.TextField(null=True, blank=True)
    art_images = models.ImageField(upload_to='shop/pics',null=True, blank=True)
    img_desc = models.CharField(max_length=100,blank=True)
    

class PythonProjects(models.Model):
    pid = models.AutoField
    category = models.CharField(max_length=50)
    projectsDesc = models.TextField()
    #projectConsole = models.ImageField(upload_to='shop/pics',null=True, blank=True)
    projectlink = models.CharField(max_length = 100)
    projectOutput = models.ImageField(upload_to='shop/pics',null=True, blank=True)