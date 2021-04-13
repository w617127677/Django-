from django.db import models

class User(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    name=models.CharField(max_length=32,null=True)
    img = models.ImageField(upload_to='img',null=True)
    jianjie=models.CharField(max_length=32,null=True)
    qq=models.CharField(max_length=32,null=True)
    youxiang=models.CharField(max_length=32,null=True)
class text(models.Model):
    name=models.CharField(max_length=32)
    jianjie=models.CharField(max_length=32)
    price=models.CharField(max_length=32)
    img = models.ImageField(upload_to='.', null=True)
    data=models.DateTimeField(auto_now=True)
    pd=models.ForeignKey('User',on_delete=models.CASCADE)
class texe(models.Model):
    name=models.CharField(max_length=32)
    jianjie=models.CharField(max_length=32)
    price=models.CharField(max_length=32)
    img = models.ImageField(upload_to='.', null=True)
    data=models.DateTimeField(auto_now=True)
    pd=models.ForeignKey('User',on_delete=models.CASCADE)
class buy(models.Model):

    name=models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    lianxi=models.CharField(max_length=32)
    username=models.CharField(max_length=32)
    data=models.DateTimeField(auto_now=True)
    pd = models.ForeignKey('User', on_delete=models.CASCADE)
class sell(models.Model):
    name = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    lianxi = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    data = models.DateTimeField(auto_now=True)
    pd = models.ForeignKey('User', on_delete=models.CASCADE)
class chat(models.Model):
    user_name= models.CharField(max_length=32)
    answer = models.CharField(max_length=32)
    pd = models.ForeignKey('User', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='.', null=True)
class to_chat(models.Model):
    user_name = models.CharField(max_length=32)
    answer = models.CharField(max_length=32)
    data = models.DateTimeField(auto_now=True)
    neirong = models.CharField(max_length=32)
    pd = models.ForeignKey('User', on_delete=models.CASCADE)
