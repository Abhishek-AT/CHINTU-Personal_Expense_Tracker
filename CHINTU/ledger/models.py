from django.db import models
from account.models import User
# Create your models here.


class Group(models.Model):
    gname = models.CharField(max_length=40)
    participants = models.ManyToManyField(User)


class Transaction(models.Model):
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    # bill = models.FilePathField(null=True)
    participants = models.ForeignKey(User,on_delete=models.CASCADE,default="1")
    timestamp = models.DateTimeField(auto_now=True)


class GroupTransaction(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    own = models.CharField(max_length=40)
    amount = models.FloatField()
    owned = models.CharField(max_length=40)
