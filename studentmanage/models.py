from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Class(models.Model):
    ClassName = models.CharField(max_length=150, null=True)
    Section = models.CharField(max_length=200, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ClassName

class Notice(models.Model):
    classs = models.ForeignKey(Class, on_delete=models.CASCADE)
    NoticeTitle = models.CharField(max_length=150, null=True)
    NoticeMsg = models.CharField(max_length=200, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NoticeTitle

class Publicnotice(models.Model):
    NoticeTitle = models.CharField(max_length=150, null=True)
    NoticeMsg = models.CharField(max_length=200, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NoticeTitle

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classs = models.ForeignKey(Class, on_delete=models.CASCADE)
    Gender = models.CharField(max_length=50, null=True)
    DOB = models.DateField(null=True)
    StuID = models.IntegerField(null=True)
    FatherName = models.CharField(max_length=150, null=True)
    MotherName = models.CharField(max_length=150, null=True)
    ContactNumber = models.CharField(max_length=150, null=True)
    AltenateNumber = models.CharField(max_length=150, null=True)
    Address = models.CharField(max_length=150, null=True)
    UserName = models.CharField(max_length=150, null=True)
    Image = models.FileField(max_length=200, null=True)
    DateofAdmission = models.DateField(null=True)

    def __str__(self):
        return self.user.first_name