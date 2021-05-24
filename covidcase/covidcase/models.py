from django.db import models

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    symptoms = models.CharField(max_length=50)
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.username