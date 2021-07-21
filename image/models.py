from django.db import models
from accounts.models import Profile


class Profileimage(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    uploader = models.ForeignKey(Profile,on_delete=models.DO_NOTHING,null=True, blank=True)

    def __str__(self):
        return self.name
