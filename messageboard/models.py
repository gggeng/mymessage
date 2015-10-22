# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Msg(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(User)
    ip = models.IPAddressField()
    datetime = models.DateTimeField(auto_now_add=True)
    clickcount = models.IntegerField(default=0)

    def __unicode__(self):
        return '用户%s发表的标题为%s的留言' % (self.user.username, self.title)
