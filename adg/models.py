


from django.db import models




# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="projects/")
    preview = models.URLField(null=True,blank=True)
    github = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name=models.CharField(max_length=250)
    image = models.ImageField(upload_to="members/")
    tags=models.ManyToManyField('Tag',blank=True)
    one_liner = models.CharField(max_length=500,null=True,blank=True)
    github = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)


    def __str__(self):
        return self.name

class Event(models.Model):
    name=models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="events/")
    date = models.DateField(null=True,blank=True)
    link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=500)
    body = models.TextField(null=True,blank=True, max_length=1000)
    image = models.ImageField(upload_to="blogs/",null=True,blank=True,default="default user.jpg")
    author = models.CharField(max_length=250,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title

